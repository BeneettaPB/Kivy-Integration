import os
import subprocess
import random
import string
import urllib.request
from pathlib import Path
from .import strings
from .import ui_elements

base_directory = "kivy-build/app/"
kivy_string_folder_path = base_directory + "base_strings/"
kivy_main_file_path = base_directory + "main.py"
kivy_image_folder = base_directory + "images/"
kivy_appicon_folder = base_directory + "appicon/"
kivy_video_folder = base_directory + "videos/"
kivy_audio_folder = base_directory + "audio/"

# for kivy-template string file for screen
class ScreenStringHandler:
    def __init__(self, screen):
        tab_bar_height = 0
        app_bar_height = 0
        padding_top = 0
        for element in screen['children']:
            if element['componentTypeName'] == 'TabNavigator' and element['componentTypeName'] == 'AppBar':
                padding_top = 100
            if element['componentTypeName'] == 'TabNavigator':
                tab_bar_height = 50
                padding_top = 50
            if element['componentTypeName'] == 'AppBar':
                app_bar_height = 50
                padding_top = 50

        screen_name = "screen_" + str(screen.get('id'))
        bg_image = screen['properties']['bgImage'].get('url')
        bg_file_name = screen['properties']['bgImage'].get('name')
        image_folder_path = 'images/'
        extras = ""
        if bg_image:
            file_name, _ = file_download(kivy_image_folder, bg_image, bg_file_name)
            extras = f'''source:"{image_folder_path}{file_name}"'''
        # color extracted to r,g,b,a format
        bg_color = extract_rgba(screen['properties'].get('bgColor'))
        vertical_align = screen['properties'].get('verticalAlign')
        horizontal_align = screen['properties'].get('horizontalAlign')
        screen_id = 'id_' + str(screen.get('id'))
        value_map = ui_elements.process_element_properties(screen)
        # ============================================= #
        screen_strings = f'''{screen_name}_string = """ '''
        screen_strings += strings.screen_string \
            .replace('<<<screen_id>>>', screen_id) \
            .replace('<<<bg_color>>>', str(bg_color)) \
            .replace('<<<screen_name>>>', screen_name) \
            .replace('<<<horizontal_align>>>', horizontal_align) \
            .replace('<<<vertical_align>>>', vertical_align) \
            .replace('<<<padding_left>>>', str(value_map.get('padding_left'))) \
            .replace('<<<padding_top>>>', str(padding_top)) \
            .replace('<<<padding_right>>>', str(value_map.get('padding_right'))) \
            .replace('<<<padding_bottom>>>', str(value_map.get('padding_bottom'))) \
            .replace('<<<tab_bar_height>>>', str(tab_bar_height)) \
            .replace('<<<app_bar_height>>>', str(app_bar_height)) \
            .replace('#<<<screen_background_image>>>', extras)
        screen_strings += '"""'
        path = kivy_string_folder_path + screen_name + "_strings.py"
        write_file(screen_strings, path)

    # PROCESS APP DATA


class ProcessAppData:
    def __init__(self, main_input):
        # print("app_data - ", main_input)
        screens = main_input['saved_app_settings']['components']['children']
        # print('screens - ', screens)
        Main(screens, main_input)
        for screen in screens:
            screen['name'] = 'kivy_' + str(screen['id'])
            # print('handling screen {} ...'.format(screen['name']))

            ScreenStringHandler(screen)
            elements = screen['children']
            ui_elements.Ui_Elements(elements, screen, screen)


# for python main file
class Main:
    def __init__(self, screens, main_input):
        # processing ui elements inside screen
        # print('screens - ', screens)

        # appicon &&launch screen##

        app_name = main_input['saved_app_settings']['app_settings']['appName']
        app_icon = main_input['saved_app_settings']['app_settings']['default']['appIconUrl'] or \
                   main_input['saved_app_settings']['app_settings']['moreLaunchScreenOption']['android'][
                       'appIcon']
        image_folder_path = 'images/'
        # extras = ""
        simple_launch_screen = main_input['saved_app_settings']['app_settings']['default']['launchScreenImageUrl']
        launch_screens = [{'url': simple_launch_screen}] if simple_launch_screen else \
            main_input['saved_app_settings']['app_settings']['moreLaunchScreenOption']['android']['launchScreens']
        app_icon_image = ''
        launch_screen_image = ''
        if app_icon:
            file_name, _ = file_download(kivy_image_folder, app_icon, app_name)
            app_icon_image = f'''source:"{image_folder_path}{file_name}"'''
        if simple_launch_screen:
            file_name, _ = file_download(kivy_image_folder, simple_launch_screen)
            launch_screen_image = f'''source:"{image_folder_path}{file_name}"'''
        self.main_string = ''
        self.calling_screens = ''
        self.imports = ''
        self.main = ''
        self.launch_screen = ''
        # handling imports
        screen_id_splashscreen = "screen_" + screens[0].get('id')
        screen_class_id_splashscreen = "Screen_" + screens[0].get('id')
        # print(screen_id_splashscreen)
        # strings.main_app_base_string
        imports = strings.imports
        main_string = strings.main_app_base_string.replace("#<<<imports_marking>>>>", str(imports)) \
            .replace('#<<<splash_screen_id>>>', str(screen_id_splashscreen)) \
            .replace('#<<app_icon>>', str(app_icon_image))
        splash_screen = f'''\nsplash_screen = """ '''
        splash_screen += strings.splash_screen \
            .replace('#<<<splash_screen_id>>>', str(screen_id_splashscreen)) \
            .replace('#<<launch_image>>', str(launch_screen_image)) \
            .replace('#<<<splash_screen_class_id>>>', screen_class_id_splashscreen)

        splash_screen += '"""'
        # defining all screen classes
        screen_string, calling_screens, imports = self.add_screen(screens)
        new_imports = main_string.replace("#<<<new_imports>>>", str(imports))
        main_screen_string = new_imports.replace("#<<<new_screen_marking>>>", str(screen_string))
        # calling each screen
        base_string = main_screen_string.replace('#<<<calling_screens>>>', str(calling_screens)) \
            .replace('#<<launchscreen>>', str(splash_screen))
        main_path = kivy_main_file_path
        main_file_path = Path(main_path)
        # writing main file
        if not main_file_path.exists():
            Path(os.path.dirname(main_file_path)).mkdir(exist_ok=True, parents=True)
        main_file_path.write_text(base_string, encoding='utf-8')

    # for adding each screen
    def add_screen(self, screens):
        for screen in screens:
            screen['name'] = 'af' + str(screen['id'])
            # print('handling screen {} ...'.format(screen['name']))
            screen_name = screen.get('id')
            screen_filename = "screen_" + screen_name + "_strings"
            screen_string = "screen_" + screen_name + "_string"
            self.main = strings.main_screen \
                .replace('<<<screen_id>>>', screen_name) \
                .replace('<<<screen_strings_filename>>>', screen_filename) \
                .replace('<<<screen_string>>>', screen_string)
            self.main_string += self.main
            calling_screens = f'screen_manager.add_widget(Screen_{screen_name}' \
                              f'(name="screen_{screen_name}",' \
                              f''f'size_hint=(None, None),size=(window_width, window_height)))\n        '
            self.calling_screens += calling_screens

            # imports
            imports = f'from base_strings.{screen_filename} import *\n'
            self.imports += imports
        return self.main_string, self.calling_screens, self.imports


# for creating and writing screen string files
def write_file(string_data, path):
    out_file_path = Path(path)
    if not out_file_path.exists():
        Path(os.path.dirname(out_file_path)).mkdir(exist_ok=True, parents=True)
    out_file_path.write_text(string_data, encoding='utf-8')


# extract color to rgba
def extract_rgba(hx):
    # print('hex:',hx)
    if len(hx) == 7:
        hx += "ff"
    return tuple(round(int(hx[i:i + 2], 16) / 255, 5) for i in range(1, 8, 2))


def file_download(folder_path, download_url, file_name=None):
    print("\t\t\tdownloading: " + download_url)
    with urllib.request.urlopen(download_url) as f:
        downloaded = f.read()
        ext = download_url
        if not file_name:
            file_name = ''.join(random.choices(string.ascii_lowercase, k=6))
            if "jpg" in ext.split('.'):
                ext = "jpg"
                in_file_path = folder_path + file_name + ".jpg"
            elif "svg" in ext.split('.'):
                ext = "svg"
                in_file_path = folder_path + file_name + ".svg"
        else:
            in_file_path = folder_path + file_name
        out_file_path = Path(in_file_path)
        if not out_file_path.exists():
            Path(os.path.dirname(in_file_path)).mkdir(exist_ok=True, parents=True)
            with open(in_file_path, 'wb') as wf:
                wf.write(downloaded)

        return file_name, ext

#
# with open('json_file.py') as f:
#     apps_data = json.load(f)
#     KivyApp(apps_data)
