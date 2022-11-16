import os
import shutil
from pathlib import Path
from .import strings
from .import base


class Ui_Elements:
    def __init__(self, elements, parent_element, screen):
        screen_name = 'screen_' + screen.get('id')
        screen_id = screen.get('id')
        self.screen_file_name = base.kivy_string_folder_path + screen_name + "_strings.py"

        if parent_element['componentTypeName'] == 'Screen':
            with open(self.screen_file_name, 'r') as f:
                global kivy_strings
                kivy_strings = f.read()
            with open(base.kivy_main_file_path, 'r') as f:
                global python_strings
                python_strings = f.read()

        for ui_elm in elements:
            if ui_elm['componentTypeName'] == 'HorizontalLayout':
                kivy_strings += KIVY_STRINGS.horizontal_layout_kivy(ui_elm, parent_element)
                main_strings, action_fun = PYTHON.horizontal_layout_python(ui_elm, parent_element, screen)
                marking = '#<<<adding_new_widgets>>>' + parent_element.get('id')
                action_fun_marking = '#<<<adding_action_fun_to_element>>>' + screen_id
                python_strings = python_strings.replace(marking, main_strings) \
                    .replace(action_fun_marking, action_fun)
                if ui_elm['children']:
                    Ui_Elements(ui_elm['children'], ui_elm, screen)

            if ui_elm['componentTypeName'] == 'VerticalLayout':
                kivy_strings += KIVY_STRINGS.vertical_layout_kivy(ui_elm, parent_element)
                main_strings, action_fun = PYTHON.vertical_layout_python(ui_elm, parent_element, screen)
                marking = '#<<<adding_new_widgets>>>' + parent_element.get('id')
                action_fun_marking = '#<<<adding_action_fun_to_element>>>' + screen_id
                python_strings = python_strings.replace(marking, main_strings) \
                    .replace(action_fun_marking, action_fun)
                if ui_elm['children']:
                    Ui_Elements(ui_elm['children'], ui_elm, screen)

            if ui_elm['componentTypeName'] == 'CardView':
                kivy_strings += KIVY_STRINGS.card_view_kivy(ui_elm, parent_element)
                main_strings, action_fun = PYTHON.card_view_python(ui_elm, parent_element, screen)
                marking = '#<<<adding_new_widgets>>>' + parent_element.get('id')
                action_fun_marking = '#<<<adding_action_fun_to_element>>>' + screen_id
                python_strings = python_strings.replace(marking, main_strings) \
                    .replace(action_fun_marking, action_fun)
                if ui_elm['children']:
                    Ui_Elements(ui_elm['children'], ui_elm, screen)

            if ui_elm['componentTypeName'] == 'Button':
                kivy_strings += KIVY_STRINGS.button_kivy(ui_elm, parent_element)
                main_strings, action_fun = PYTHON.button_python(ui_elm, parent_element, screen)
                marking = '#<<<adding_new_widgets>>>' + parent_element.get('id')
                action_fun_marking = '#<<<adding_action_fun_to_element>>>' + screen_id
                python_strings = python_strings.replace(marking, main_strings) \
                    .replace(action_fun_marking, action_fun)

            if ui_elm['componentTypeName'] == 'Text':
                kivy_strings += KIVY_STRINGS.text_kivy(ui_elm, parent_element)
                main_strings, action_fun = PYTHON.text_python(ui_elm, parent_element, screen)
                marking = '#<<<adding_new_widgets>>>' + parent_element.get('id')
                action_fun_marking = '#<<<adding_action_fun_to_element>>>' + screen_id
                python_strings = python_strings.replace(marking, main_strings) \
                    .replace(action_fun_marking, action_fun)
            if ui_elm['componentTypeName'] == 'TextField':
                kivy_strings += KIVY_STRINGS.text_field_kivy(ui_elm, parent_element)
                main_strings, action_fun = PYTHON.text_field_python(ui_elm, parent_element, screen)
                marking = '#<<<adding_new_widgets>>>' + parent_element.get('id')
                action_fun_marking = '#<<<adding_action_fun_to_element>>>' + screen_id
                python_strings = python_strings.replace(marking, main_strings) \
                    .replace(action_fun_marking, action_fun)

            if ui_elm['componentTypeName'] == 'ListViewer':
                kivy_strings += KIVY_STRINGS.list_viewer_kivy(ui_elm, parent_element)
                main_strings, action_fun = PYTHON.list_viewer_python(ui_elm, parent_element, screen)
                marking = '#<<<adding_new_widgets>>>' + parent_element.get('id')
                action_fun_marking = '#<<<adding_action_fun_to_element>>>' + screen_id
                python_strings = python_strings.replace(marking, main_strings) \
                    .replace(action_fun_marking, action_fun)

            if ui_elm['componentTypeName'] == 'DatePicker':
                kivy_strings += KIVY_STRINGS.date_picker_kivy(ui_elm, parent_element)
                main_strings = PYTHON.date_picker_python( ui_elm, parent_element, screen)
                marking = '#<<<adding_new_widgets>>>' + parent_element.get('id')
                action_fun_marking = '#<<<adding_action_fun_to_element>>>' + screen_id
                python_strings = python_strings.replace(marking, main_strings)

            if ui_elm['componentTypeName'] == 'ImagePicker':
                kivy_strings += KIVY_STRINGS.image_picker_kivy(ui_elm, parent_element)
                main_strings = PYTHON.image_picker_python(ui_elm, parent_element, screen)
                marking = '#<<<adding_new_widgets>>>' + parent_element.get('id')
                action_fun_marking = '#<<<adding_action_fun_to_element>>>' + screen_id
                python_strings = python_strings.replace(marking, main_strings)

            if ui_elm['componentTypeName'] == 'Image':
                kivy_strings += KIVY_STRINGS.image_view_kivy(ui_elm, parent_element)
                main_strings, action_fun = PYTHON.image_view_python(ui_elm, parent_element, screen)
                marking = '#<<<adding_new_widgets>>>' + parent_element.get('id')
                action_fun_marking = '#<<<adding_action_fun_to_element>>>' + screen_id
                python_strings = python_strings.replace(marking, main_strings) \
                    .replace(action_fun_marking, action_fun)

            if ui_elm['componentTypeName'] == 'TimePicker':
                kivy_strings += KIVY_STRINGS.time_picker_kivy(ui_elm, parent_element)
                main_strings = PYTHON.time_picker_python(ui_elm, parent_element, screen)
                marking = '#<<<adding_new_widgets>>>' + parent_element.get('id')
                action_fun_marking = '#<<<adding_action_fun_to_element>>>' + screen_id
                python_strings = python_strings.replace(marking, main_strings)

            if ui_elm['componentTypeName'] == 'TabNavigator':
                kivy_strings += KIVY_STRINGS.tab_navigator_kivy(ui_elm, parent_element)
                main_strings, action_fun = PYTHON.tab_navigator_python(ui_elm, parent_element, screen)
                marking = '#<<<new_tab_bar_marking>>>' + parent_element.get('id')
                action_fun_marking = '#<<<adding_action_fun_to_element>>>' + screen_id
                python_strings = python_strings.replace(marking, main_strings) \
                    .replace(action_fun_marking, action_fun)

            if ui_elm['componentTypeName'] == 'AppBar':
                kivy_strings += KIVY_STRINGS.app_bar_kivy(ui_elm, parent_element)
                main_strings, action_fun = PYTHON.app_bar_python(ui_elm, parent_element, screen)
                marking = '#<<<adding_new_widgets>>>' + parent_element.get('id')
                action_fun_marking = '#<<<adding_action_fun_to_element>>>' + screen_id
                python_strings = python_strings.replace(marking, main_strings) \
                    .replace(action_fun_marking, action_fun)

            if ui_elm['componentTypeName'] == 'TableLayout':
                kivy_strings += KIVY_STRINGS.table_layout_kivy(ui_elm, parent_element)
                main_strings, action_fun = PYTHON.table_layout_python(ui_elm, parent_element, screen)
                marking = '#<<<adding_new_widgets>>>' + parent_element.get('id')
                action_fun_marking = '#<<<adding_action_fun_to_element>>>' + screen_id
                python_strings = python_strings.replace(marking, main_strings) \
                    .replace(action_fun_marking, action_fun)
                if ui_elm['children']:
                    Ui_Elements(ui_elm['children'], ui_elm, screen)

            if ui_elm['componentTypeName'] == 'AudioPlayer':
                kivy_strings += KIVY_STRINGS.audio_player_kivy(ui_elm, parent_element)
                main_strings = PYTHON.audio_player_python(ui_elm, parent_element, screen)
                marking = '#<<<adding_new_widgets>>>' + parent_element.get('id')
                action_fun_marking = '#<<<adding_action_fun_to_element>>>' + screen_id
                python_strings = python_strings.replace(marking, main_strings)

            if ui_elm['componentTypeName'] == 'Checkbox':
                kivy_strings += KIVY_STRINGS.check_box_kivy(ui_elm, parent_element)
                main_strings = PYTHON.check_box_python(ui_elm, parent_element, screen)
                marking = '#<<<adding_new_widgets>>>' + parent_element.get('id')
                action_fun_marking = '#<<<adding_action_fun_to_element>>>' + screen_id
                python_strings = python_strings.replace(marking, main_strings)

            if ui_elm['componentTypeName'] == 'RatingBar':
                kivy_strings += KIVY_STRINGS.rating_bar_kivy(ui_elm, parent_element)
                main_strings = PYTHON.rating_bar_python(ui_elm, parent_element, screen)
                marking = '#<<<adding_new_widgets>>>' + parent_element.get('id')
                action_fun_marking = '#<<<adding_action_fun_to_element>>>' + screen_id
                python_strings = python_strings.replace(marking, main_strings)

            if ui_elm['componentTypeName'] == 'Switch':
                kivy_strings += KIVY_STRINGS.switch_kivy(ui_elm, parent_element)
                main_strings = PYTHON.switch_python(ui_elm, parent_element, screen)
                marking = '#<<<adding_new_widgets>>>' + parent_element.get('id')
                action_fun_marking = '#<<<adding_action_fun_to_element>>>' + screen_id
                python_strings = python_strings.replace(marking, main_strings)

            if ui_elm['componentTypeName'] == 'Radio Button':
                kivy_strings += KIVY_STRINGS.radio_button_kivy(ui_elm, parent_element)
                main_strings = PYTHON.radio_button_python(ui_elm, parent_element, screen)
                marking = '#<<<adding_new_widgets>>>' + parent_element.get('id')
                action_fun_marking = '#<<<adding_action_fun_to_element>>>' + screen_id
                python_strings = python_strings.replace(marking, main_strings)

            # if ui_elm['componentTypeName'] == 'Map':
            #     pass
            #     kivy_strings += KIVY_STRINGS.map_view_kivy(ui_elm, screen)
            #     main_strings, action_fun = PYTHON.map_view_python(ui_elm, screen)
            #     marking = '#<<<adding_new_widgets>>>' + screen.get('id')
            #     action_fun_marking = '#<<<adding_action_fun_to_element>>>' + screen.get('id')
            #     python_strings = python_strings.replace(marking, main_strings) \
            #         .replace(action_fun_marking, action_fun)

            if ui_elm['componentTypeName'] == 'Slider':
                kivy_strings += KIVY_STRINGS.slider_kivy(ui_elm, parent_element)
                main_strings = PYTHON.slider_python(ui_elm, parent_element, screen)
                marking = '#<<<adding_new_widgets>>>' + parent_element.get('id')
                action_fun_marking = '#<<<adding_action_fun_to_element>>>' + screen_id
                python_strings = python_strings.replace(marking, main_strings)

            if ui_elm['componentTypeName'] == 'Webview':
                kivy_strings += KIVY_STRINGS.web_view_kivy(ui_elm, parent_element)
                main_strings, action_fun = PYTHON.web_view_python(ui_elm, parent_element, screen)
                marking = '#<<<adding_new_widgets>>>' + parent_element.get('id')
                action_fun_marking = '#<<<adding_action_fun_to_element>>>' + screen_id
                python_strings = python_strings.replace(marking, main_strings) \
                    .replace(action_fun_marking, action_fun)

            if ui_elm['componentTypeName'] == 'AudioPicker':
                kivy_strings += KIVY_STRINGS.audio_picker_kivy(ui_elm, parent_element)
                main_strings = PYTHON.audio_picker_python(ui_elm, parent_element, screen)
                marking = '#<<<adding_new_widgets>>>' + parent_element.get('id')
                action_fun_marking = '#<<<adding_action_fun_to_element>>>' + screen_id
                python_strings = python_strings.replace(marking, main_strings)
                #
            if ui_elm['componentTypeName'] == 'VideoPicker':
                kivy_strings += KIVY_STRINGS.video_picker_kivy(ui_elm, parent_element)
                main_strings = PYTHON.video_picker_python(ui_elm, parent_element, screen)
                marking = '#<<<adding_new_widgets>>>' + parent_element.get('id')
                action_fun_marking = '#<<<adding_action_fun_to_element>>>' + screen_id
                python_strings = python_strings.replace(marking, main_strings)

            if ui_elm['componentTypeName'] == 'Checkbox':
                kivy_strings += KIVY_STRINGS.check_box_kivy(ui_elm, parent_element)
                main_strings = PYTHON.check_box_python(ui_elm, parent_element, screen)
                marking = '#<<<adding_new_widgets>>>' + parent_element.get('id')
                action_fun_marking = '#<<<adding_action_fun_to_element>>>' + screen_id
                python_strings = python_strings.replace(marking, main_strings)

            if ui_elm['componentTypeName'] == 'Camera':
                kivy_strings += KIVY_STRINGS.check_box_kivy(ui_elm, parent_element)
                main_strings, action_fun = PYTHON.check_box_python(ui_elm, parent_element, screen)
                marking = '#<<<adding_new_widgets>>>' + parent_element.get('id')
                action_fun_marking = '#<<<adding_action_fun_to_element>>>' + screen_id
                python_strings = python_strings.replace(marking, main_strings) \
                    .replace(action_fun_marking, action_fun)

            if ui_elm['componentTypeName'] == 'Rating Bar':
                kivy_strings += KIVY_STRINGS.check_box_kivy(ui_elm, parent_element)
                main_strings, action_fun = PYTHON.check_box_python(ui_elm, parent_element, screen)
                marking = '#<<<adding_new_widgets>>>' + parent_element.get('id')
                action_fun_marking = '#<<<adding_action_fun_to_element>>>' + screen_id
                python_strings = python_strings.replace(marking, main_strings) \
                    .replace(action_fun_marking, action_fun)

            if ui_elm['componentTypeName'] == 'Switch':
                kivy_strings += KIVY_STRINGS.switch_kivy(ui_elm, parent_element)
                main_strings = PYTHON.switch_python(ui_elm, parent_element, screen)
                marking = '#<<<adding_new_widgets>>>' + parent_element.get('id')
                action_fun_marking = '#<<<adding_action_fun_to_element>>>' + screen_id
                python_strings = python_strings.replace(marking, main_strings)

            if ui_elm['componentTypeName'] == 'Radio Button':
                kivy_strings += KIVY_STRINGS.radio_button_kivy(ui_elm, parent_element)
                main_strings = PYTHON.radio_button_python(ui_elm, parent_element, screen)
                marking = '#<<<adding_new_widgets>>>' + parent_element.get('id')
                action_fun_marking = '#<<<adding_action_fun_to_element>>>' + screen_id
                python_strings = python_strings.replace(marking, main_strings)

            if ui_elm['componentTypeName'] == 'Map':
                kivy_strings += KIVY_STRINGS.map_view_kivy(ui_elm, parent_element)
                main_strings = PYTHON.map_view_python(ui_elm, parent_element, screen)
                marking = '#<<<adding_new_widgets>>>' + parent_element.get('id')
                action_fun_marking = '#<<<adding_action_fun_to_element>>>' + screen_id
                python_strings = python_strings.replace(marking, main_strings)

            if ui_elm['componentTypeName'] == 'BarcodeScanner':
                kivy_strings += KIVY_STRINGS.barcode_view_kivy(ui_elm, parent_element)
                main_strings = PYTHON.barcode_view_python(ui_elm, parent_element, screen)
                marking = '#<<<adding_new_widgets>>>' + parent_element.get('id')
                action_fun_marking = '#<<<adding_action_fun_to_element>>>' + screen_id
                python_strings = python_strings.replace(marking, main_strings)

            if ui_elm['componentTypeName'] == 'Modal':
                kivy_strings += KIVY_STRINGS.modal_view_kivy(ui_elm, parent_element)
                main_strings = PYTHON.modal_view_python(ui_elm, parent_element, screen)
                marking = '#<<<adding_new_widgets>>>' + parent_element.get('id')
                action_fun_marking = '#<<<adding_action_fun_to_element>>>' + screen_id
                python_strings = python_strings.replace(marking, main_strings)

            if ui_elm['componentTypeName'] == 'SideMenu':
                kivy_strings += KIVY_STRINGS.side_menu_kivy(ui_elm, parent_element)
                main_strings, action_fun = PYTHON.side_menu_python(ui_elm, parent_element, screen)
                marking = '#<<<adding_new_widgets>>>' + parent_element.get('id')
                action_fun_marking = '#<<<adding_action_fun_to_element>>>' + ui_elm.get('id')
                python_strings = python_strings.replace(marking, main_strings) \
                    .replace(action_fun_marking, action_fun)

            if ui_elm['componentTypeName'] == 'VideoPlayer':
                kivy_strings += KIVY_STRINGS.video_player_kivy(ui_elm, parent_element)
                main_strings = PYTHON.video_player_python(ui_elm, parent_element, screen)
                marking = '#<<<adding_new_widgets>>>' + parent_element.get('id')
                action_fun_marking = '#<<<adding_action_fun_to_element>>>' + screen_id
                python_strings = python_strings.replace(marking, main_strings)
            # writing kivy file

            path = self.screen_file_name
            out_file_path = Path(path)
            if not out_file_path.exists():
                Path(os.path.dirname(out_file_path)).mkdir(exist_ok=True, parents=True)
            out_file_path.write_text(kivy_strings, encoding='utf-8')

            # writing python file
            path = base.kivy_main_file_path
            out_file_path = Path(path)
            if not out_file_path.exists():
                Path(os.path.dirname(out_file_path)).mkdir(exist_ok=True, parents=True)
            out_file_path.write_text(python_strings, encoding='utf-8')
    # ----------------KIVY STRING FILE--------------#


class KIVY_STRINGS:
    @staticmethod
    def horizontal_layout_kivy(ui_elm, parent_element):
        value_map = process_element_properties(ui_elm)
        elm_id = ui_elm.get('id')
        layout_id = 'id_' + elm_id
        horizontal_layout_strings = f'''\nhorizontal_layout_{elm_id}_string = """\n#:import utils kivy.utils\n#:import hex kivy.utils.get_color_from_hex '''
        horizontal_layout_strings += strings.horizontal_layout_kivy_string \
            .replace('<<<layout_id>>>', layout_id) \
            .replace('<<<screen_name>>>', elm_id) \
            .replace('<<<bg_color>>>', str(value_map.get('bg_color'))) \
            .replace('<<<width>>>', str(value_map.get('width'))) \
            .replace('<<<height>>>', str(value_map.get('height'))) \
            .replace('<<<margin_left>>>', str(value_map.get('margin_left'))) \
            .replace('<<<margin_top>>>', str(value_map.get('margin_top'))) \
            .replace('<<<margin_right>>>', str(value_map.get('margin_right'))) \
            .replace('<<<margin_bottom>>>', str(value_map.get('margin_bottom'))) \
            .replace('<<<padding_left>>>', str(value_map.get('padding_left'))) \
            .replace('<<<padding_top>>>', str(value_map.get('padding_top'))) \
            .replace('<<<padding_right>>>', str(value_map.get('padding_right'))) \
            .replace('<<<padding_bottom>>>', str(value_map.get('padding_bottom'))) \
            .replace('<<<horizontal_alignment>>>', str(value_map.get('h_align'))) \
            .replace('<<<vertical_alignment>>>', str(value_map.get('v_align'))) \
            .replace('<<<width_margin_adj>>>', str(value_map.get('width_margin_adjustment'))) \
            .replace('<<<height_margin_adj>>>', str(value_map.get('height_margin_adjustment')))
        horizontal_layout_strings += '"""'
        return horizontal_layout_strings

    @staticmethod
    def vertical_layout_kivy(ui_elm, parent_element):
        value_map = process_element_properties(ui_elm)
        elm_id = ui_elm.get('id')
        layout_id = 'id_' + elm_id
        vertical_layout_strings = f'''\nvertical_layout_{elm_id}_string = """\n#:import utils kivy.utils\n#:import hex kivy.utils.get_color_from_hex '''
        vertical_layout_strings += strings.vertical_layout_kivy_string \
            .replace('<<<layout_id>>>', layout_id) \
            .replace('<<<screen_name>>>', elm_id) \
            .replace('<<<bg_color>>>', str(value_map.get('bg_color'))) \
            .replace('<<<width>>>', str(value_map.get('width'))) \
            .replace('<<<height>>>', str(value_map.get('height'))) \
            .replace('<<<margin_left>>>', str(value_map.get('margin_left'))) \
            .replace('<<<margin_top>>>', str(value_map.get('margin_top'))) \
            .replace('<<<margin_right>>>', str(value_map.get('margin_right'))) \
            .replace('<<<margin_bottom>>>', str(value_map.get('margin_bottom'))) \
            .replace('<<<padding_left>>>', str(value_map.get('padding_left'))) \
            .replace('<<<padding_top>>>', str(value_map.get('padding_top'))) \
            .replace('<<<padding_right>>>', str(value_map.get('padding_right'))) \
            .replace('<<<padding_bottom>>>', str(value_map.get('padding_bottom'))) \
            .replace('<<<horizontal_alignment>>>', str(value_map.get('h_align'))) \
            .replace('<<<vertical_alignment>>>', str(value_map.get('v_align'))) \
            .replace('<<<width_margin_adj>>>', str(value_map.get('width_margin_adjustment'))) \
            .replace('<<<height_margin_adj>>>', str(value_map.get('height_margin_adjustment')))
        vertical_layout_strings += '"""'
        return vertical_layout_strings

    @staticmethod
    def card_view_kivy(ui_elm, parent_element):
        value_map = process_element_properties(ui_elm)
        elm_id = ui_elm.get('id')
        layout_id = 'id_' + elm_id
        action_id = 'action_id_' + elm_id
        padding_bottom = int(value_map.get('padding_bottom')) + int(value_map.get('border_size'))
        card_view_strings = f'''\ncard_view_{elm_id}_string = """\n#:import utils kivy.utils\n#:import hex kivy.utils.get_color_from_hex '''
        card_view_strings += strings.card_view_kivy_string \
            .replace('<<<action_id>>>', action_id) \
            .replace('<<<screen_name>>>', elm_id) \
            .replace('<<<layout_id>>>', layout_id) \
            .replace('<<<width>>>', str(value_map.get('width'))) \
            .replace('<<<height>>>', str(value_map.get('height'))) \
            .replace('<<<bg_color>>>', str(value_map.get('bg_color'))) \
            .replace('<<<padding_left>>>', str(value_map.get('padding_left'))) \
            .replace('<<<padding_top>>>', str(value_map.get('padding_top'))) \
            .replace('<<<padding_right>>>', str(value_map.get('padding_right'))) \
            .replace('<<<padding_bottom>>>', str(padding_bottom)) \
            .replace('<<<margin_left>>>', str(value_map.get('margin_left'))) \
            .replace('<<<margin_top>>>', str(value_map.get('margin_top'))) \
            .replace('<<<margin_right>>>', str(value_map.get('margin_right'))) \
            .replace('<<<margin_bottom>>>', str(value_map.get('margin_bottom'))) \
            .replace('<<<border_color>>>', str(value_map.get('border_color'))) \
            .replace('<<<border_size>>>', str(value_map.get('border_size'))) \
            .replace('<<<border_radius>>>', str(value_map.get('border_radius'))) \
            .replace('<<<horizontal_alignment>>>', str(value_map.get('h_align'))) \
            .replace('<<<vertical_alignment>>>', str(value_map.get('v_align'))) \
            .replace('<<<width_margin_adj>>>', str(value_map.get('width_margin_adjustment'))) \
            .replace('<<<height_margin_adj>>>', str(value_map.get('height_margin_adjustment')))

        card_view_strings += '"""'
        return card_view_strings

    @staticmethod
    def text_kivy(ui_elm, parent_element):
        value_map = process_element_properties(ui_elm)
        elm_id = ui_elm.get('id')
        action_id = "action_id_" + elm_id
        font_type = ui_elm['properties'].get("font", {})["family"]
        font_family = set_font_family(font_type)
        text_strings = f'''\ntext_{elm_id}_string = """\n#:import utils kivy.utils\n#:import hex kivy.utils.get_color_from_hex '''
        text_strings += strings.text_kivy_string \
            .replace('<<<screen_name>>>', elm_id) \
            .replace('<<<action_id>>>', action_id) \
            .replace('<<<text>>>', str(value_map.get('text'))) \
            .replace('<<<font_type>>>', font_family) \
            .replace('<<<font_size>>>', str(value_map.get('font_size'))) \
            .replace('<<<font_color>>>', str(value_map.get('font_color'))) \
            .replace('<<<bg_color>>>', str(value_map.get('bg_color'))) \
            .replace('<<<text_alignment>>>', str(value_map.get('text_align'))) \
            .replace('<<<width>>>', str(value_map.get('width'))) \
            .replace('<<<height>>>', str(value_map.get('height'))) \
            .replace('<<<margin_left>>>', str(value_map.get('margin_left'))) \
            .replace('<<<margin_top>>>', str(value_map.get('margin_top'))) \
            .replace('<<<margin_right>>>', str(value_map.get('margin_right'))) \
            .replace('<<<margin_bottom>>>', str(value_map.get('margin_bottom'))) \
            .replace('<<<padding_left>>>', str(value_map.get('padding_left'))) \
            .replace('<<<padding_top>>>', str(value_map.get('padding_top'))) \
            .replace('<<<padding_right>>>', str(value_map.get('padding_right'))) \
            .replace('<<<padding_bottom>>>', str(value_map.get('padding_bottom'))) \
            .replace('<<<width_margin_adj>>>', str(value_map.get('width_margin_adjustment'))) \
            .replace('<<<height_margin_adj>>>', str(value_map.get('height_margin_adjustment')))

        text_strings += '"""'
        return text_strings
        # font type pending

    @staticmethod
    def button_kivy(ui_elm, parent_element):
        value_map = process_element_properties(ui_elm)
        elm_id = ui_elm.get('id')
        border_color = ui_elm['properties'].get("borderColor") or "ffffff"
        action_id = 'action_id_' + elm_id
        pos_hint = f'''pos_hint: {{'center_x': .5, 'center_y': .5}}'''
        if parent_element['componentTypeName'] == 'Screen':
            pos_hint = f'''pos_hint: {{'x': 0, 'top': 1}}'''
        button_strings = f'''\nbutton_{elm_id}_string = """\n#:import utils kivy.utils '''
        button_strings += strings.button_kivy_string \
            .replace('<<<bg_image>>>', value_map['button_image']) \
            .replace('<<<action_id>>>', action_id) \
            .replace('<<<screen_name>>>', elm_id) \
            .replace('<<<border_color>>>', border_color) \
            .replace('<<<text>>>', str(value_map.get('text'))) \
            .replace('<<<font_type>>>', str(value_map.get('font_family'))) \
            .replace('<<<font_size>>>', str(value_map.get('font_size'))) \
            .replace('<<<font_color>>>', str(value_map.get('font_color'))) \
            .replace('<<<bg_color>>>', str(value_map.get('bg_color'))) \
            .replace('<<<text_alignment>>>', str(value_map.get('text_align'))) \
            .replace('<<<width>>>', str(value_map.get('width'))) \
            .replace('<<<height>>>', str(value_map.get('height'))) \
            .replace('<<<margin_left>>>', str(value_map.get('margin_left'))) \
            .replace('<<<margin_top>>>', str(value_map.get('margin_top'))) \
            .replace('<<<margin_right>>>', str(value_map.get('margin_right'))) \
            .replace('<<<margin_bottom>>>', str(value_map.get('margin_bottom'))) \
            .replace('<<<padding_left>>>', str(value_map.get('padding_left'))) \
            .replace('<<<padding_top>>>', str(value_map.get('padding_top'))) \
            .replace('<<<padding_right>>>', str(value_map.get('padding_right'))) \
            .replace('<<<padding_bottom>>>', str(value_map.get('padding_bottom'))) \
            .replace('<<<border_radius>>>', str(value_map.get('border_radius'))) \
            .replace('<<<shadow_x>>>', str(value_map.get('shadow_x'))) \
            .replace('<<<shadow_y>>>', str(value_map.get('shadow_y'))) \
            .replace('<<<shadow_blur>>>', str(value_map.get('blur'))) \
            .replace('<<<shadow_color>>>', str(value_map.get('shadow_color'))) \
            .replace('<<<width_margin_adj>>>', str(value_map.get('width_margin_adjustment'))) \
            .replace('<<<height_margin_adj>>>', str(value_map.get('height_margin_adjustment'))) \
            .replace('#<<<pos_hint_marking>>>', pos_hint)

        button_strings += '"""'
        return button_strings


    @staticmethod
    def text_field_kivy(ui_elm, parent_element):
        value_map = process_element_properties(ui_elm)
        elm_id = ui_elm.get('id')
        action_id = "action_id_" + elm_id
        hint_text = ui_elm['properties'].get("hintText")
        hint_text_color = ui_elm['properties'].get("hintColor")
        input_type = ui_elm['properties'].get("type")
        font_type = ui_elm['properties'].get("font", {})["family"]
        font_family = set_font_family(font_type)
        text_field_strings = f'''\ntext_field_{elm_id}_string = """\n#:import utils kivy.utils\n#:import hex kivy.utils.get_color_from_hex '''
        text_field_strings += strings.text_field_kivy_string \
            .replace('<<<screen_name>>>', elm_id) \
            .replace('<<<action_id>>>', action_id) \
            .replace('<<<text>>>', str(value_map.get('text'))) \
            .replace('<<<hint_text>>>', hint_text) \
            .replace('<<<hint_text_color>>>', hint_text_color) \
            .replace('<<<input_type>>>', input_type) \
            .replace('<<<font_type>>>', font_family) \
            .replace('<<<font_size>>>', str(value_map.get('font_size'))) \
            .replace('<<<font_color>>>', str(value_map.get('font_color'))) \
            .replace('<<<bg_color>>>', str(value_map.get('bg_color'))) \
            .replace('<<<text_alignment>>>', str(value_map.get('text_align'))) \
            .replace('<<<width>>>', str(value_map.get('width'))) \
            .replace('<<<height>>>', str(value_map.get('height'))) \
            .replace('<<<margin_left>>>', str(value_map.get('margin_left'))) \
            .replace('<<<margin_top>>>', str(value_map.get('margin_top'))) \
            .replace('<<<margin_right>>>', str(value_map.get('margin_right'))) \
            .replace('<<<margin_bottom>>>', str(value_map.get('margin_bottom'))) \
            .replace('<<<padding_left>>>', str(value_map.get('padding_left'))) \
            .replace('<<<padding_top>>>', str(value_map.get('padding_top'))) \
            .replace('<<<padding_right>>>', str(value_map.get('padding_right'))) \
            .replace('<<<padding_bottom>>>', str(value_map.get('padding_bottom'))) \
            .replace('<<<border_radius>>>', str(value_map.get('border_radius'))) \
            .replace('<<<border_color>>>', str(value_map.get('border_color'))) \
            .replace('<<<border_size>>>', str(value_map.get('border_size'))) \
            .replace('<<<shadow_x>>>', str(value_map.get('shadow_x'))) \
            .replace('<<<shadow_y>>>', str(value_map.get('shadow_y'))) \
            .replace('<<<shadow_blur>>>', str(value_map.get('blur'))) \
            .replace('<<<shadow_color>>>', str(value_map.get('shadow_color'))) \
            .replace('<<<width_margin_adj>>>', str(value_map.get('width_margin_adjustment'))) \
            .replace('<<<height_margin_adj>>>', str(value_map.get('height_margin_adjustment')))
        text_field_strings += '"""'
        return text_field_strings
        # font type pending

    @staticmethod
    def tab_navigator_kivy(ui_elm, parent_element):
        value_map = process_element_properties(ui_elm)
        elm_id = ui_elm.get('id')
        font_type = ui_elm['properties'].get("font", {})["family"]
        font_family = set_font_family(font_type)
        tab_list = ui_elm['properties'].get('list')
        tab_strings = ''
        # active_tab_color = ui_elm['properties'].get('tabActiveColor')
        # inactive_tab_color = ui_elm['properties'].get('tabInactiveColor')
        bg_color = base.extract_rgba(ui_elm['properties'].get("tabBgColor") or "ffffff")

        count = 0
        for tab in tab_list:
            count += 1
            text = tab.get('text')
            tab_id = 'tab' + str(count) + "_id"
            tab_bar_id = 'tab_bar' + str(count) + "_id"
            tab_strings += strings.tab_string \
                .replace('<<<tab_bar_id>>>', tab_bar_id) \
                .replace('<<<tab_id>>>', tab_id) \
                .replace('<<<text>>>', text) \
                .replace('<<<font_type>>>', font_family) \
                .replace('<<<font_size>>>', str(value_map.get('font_size'))) \
                .replace('<<<font_color>>>', str(ui_elm['properties'].get("font", {})["color"]))

        tab_navigator_strings = f'''\ntab_navigator_{elm_id}_string = """\n#:import utils kivy.utils '''
        tab_navigator_strings += strings.tab_navigator_kivy_string \
            .replace('<<<bg_color>>>', str(bg_color)) \
            .replace('#<<<new_tab_marking>>>', tab_strings)
        tab_navigator_strings += '"""'
        return tab_navigator_strings

    @staticmethod
    def image_view_kivy(ui_elm, parent_element):
        value_map = process_element_properties(ui_elm)
        elm_id = ui_elm.get('id')
        bg_image = ui_elm['properties'].get("file", {})["name"]
        bg_image_url = ui_elm['properties'].get("file", {})["url"]

        if bg_image.startswith('https'):
            a = urlparse(bg_image_url)
            bg_image = os.path.basename(a.path)
        bg_image_string = ''
        if bg_image:
            file_name, _ = base.file_download(base.kivy_image_folder, bg_image_url, bg_image)

        image_fit = ui_elm['properties'].get("imageFit")
        image_view_strings = f'''\nimage_view_{elm_id}_string = """\n#:import utils kivy.utils '''
        if image_fit == 'auto':
            bg_image_string = 'background:"images/' + str(bg_image) + '"'
            image_strings = strings.image_auto_kivy_string
        elif image_fit == 'contain':
            bg_image_string = 'source:"images/' + str(bg_image) + '"'
            image_strings = strings.image_contain_kivy_string
        else:
            bg_image_string = 'source:"images/' + str(bg_image) + '"'
            image_strings = strings.image_cover_kivy_string
        image_view_strings += image_strings \
            .replace('<<<screen_name>>>', elm_id) \
            .replace('<<<width>>>', str(value_map.get('width'))) \
            .replace('<<<height>>>', str(value_map.get('height'))) \
            .replace('<<<margin_left>>>', str(value_map.get('margin_left'))) \
            .replace('<<<margin_top>>>', str(value_map.get('margin_top'))) \
            .replace('<<<margin_right>>>', str(value_map.get('margin_right'))) \
            .replace('<<<margin_bottom>>>', str(value_map.get('margin_bottom'))) \
            .replace('<<<padding_left>>>', str(value_map.get('padding_left'))) \
            .replace('<<<padding_top>>>', str(value_map.get('padding_top'))) \
            .replace('<<<padding_right>>>', str(value_map.get('padding_right'))) \
            .replace('<<<padding_bottom>>>', str(value_map.get('padding_bottom'))) \
            .replace('<<<border_radius>>>', str(value_map.get('border_radius'))) \
            .replace('<<<bg_image>>>', bg_image) \
            .replace('<<<shadow_x>>>', str(value_map.get('shadow_x'))) \
            .replace('<<<shadow_y>>>', str(value_map.get('shadow_y'))) \
            .replace('<<<shadow_blur>>>', str(value_map.get('blur'))) \
            .replace('<<<shadow_color>>>', str(value_map.get('shadow_color'))) \
            .replace('<<<width_margin_adj>>>', str(value_map.get('width_margin_adjustment'))) \
            .replace('<<<height_margin_adj>>>', str(value_map.get('height_margin_adjustment'))) \
            .replace('#<<<image-marking>>>', bg_image_string)
        image_view_strings += '"""'
        return image_view_strings

    @staticmethod
    def app_bar_kivy(ui_elm, parent_element):
        value_map = process_element_properties(ui_elm)
        elm_id = ui_elm.get('id')
        action_id = "action_id_" + elm_id
        app_bar_strings = f'''\napp_bar_{elm_id}_string = """\n#:import utils kivy.utils\n#:import hex kivy.utils.get_color_from_hex '''
        app_bar_strings += strings.app_bar_kivy_string \
            .replace('<<<screen_name>>>', elm_id) \
            .replace('<<<action_id>>>', action_id) \
            .replace('<<<text>>>', str(value_map.get('title'))) \
            .replace('<<<font_family>>>', str(value_map.get('font_family'))) \
            .replace('<<<font_size>>>', str(value_map.get('font_size'))) \
            .replace('<<<font_color>>>', str(ui_elm['properties'].get("font", {})["color"])) \
            .replace('<<<text_alignment>>>', str(value_map.get('text_align'))) \
            .replace('<<<bg_color>>>', str(value_map.get('bg_color')))
        app_bar_strings += '"""'
        return app_bar_strings


    @staticmethod
    def image_picker_kivy(ui_elm, parent_element):
        value_map = process_element_properties(ui_elm)
        elm_id = ui_elm.get('id')
        font_type = ui_elm['properties'].get("font", {})["family"]
        font_family = set_font_family(font_type)
        image_picker_strings = f'''\nimage_picker_{elm_id}_string = """\n#:import utils kivy.utils\n#:import hex kivy.utils.get_color_from_hex '''
        image_picker_strings += strings.image_picker_kivy_string \
            .replace('<<<screen_name>>>', elm_id) \
            .replace('<<<border_color>>>', str(value_map.get('border_color'))) \
            .replace('<<<border_radius>>>', str(value_map.get('border_radius'))) \
            .replace('<<<border_size>>>', str(value_map.get('border_size'))) \
            .replace('<<<text>>>', str(value_map.get('text'))) \
            .replace('<<<font_type>>>', font_family) \
            .replace('<<<font_size>>>', str(value_map.get('font_size'))) \
            .replace('<<<font_color>>>', str(value_map.get('font_color'))) \
            .replace('<<<bg_color>>>', str(value_map.get('bg_color'))) \
            .replace('<<<width>>>', str(value_map.get('width'))) \
            .replace('<<<height>>>', str(value_map.get('height'))) \
            .replace('<<<margin_left>>>', str(value_map.get('margin_left'))) \
            .replace('<<<margin_top>>>', str(value_map.get('margin_top'))) \
            .replace('<<<margin_right>>>', str(value_map.get('margin_right'))) \
            .replace('<<<margin_bottom>>>', str(value_map.get('margin_bottom'))) \
            .replace('<<<padding_left>>>', str(value_map.get('padding_left'))) \
            .replace('<<<padding_top>>>', str(value_map.get('padding_top'))) \
            .replace('<<<padding_right>>>', str(value_map.get('padding_right'))) \
            .replace('<<<padding_bottom>>>', str(value_map.get('padding_bottom'))) \
            .replace('<<<shadow_x>>>', str(value_map.get('shadow_x'))) \
            .replace('<<<shadow_y>>>', str(value_map.get('shadow_y'))) \
            .replace('<<<shadow_blur>>>', str(value_map.get('blur'))) \
            .replace('<<<shadow_color>>>', str(value_map.get('shadow_color'))) \
            .replace('<<<width_margin_adj>>>', str(value_map.get('width_margin_adjustment'))) \
            .replace('<<<height_margin_adj>>>', str(value_map.get('height_margin_adjustment')))
        image_picker_strings += '"""'
        return image_picker_strings

    @staticmethod
    def date_picker_kivy(ui_elm, parent_element):
        value_map = process_element_properties(ui_elm)
        elm_id = ui_elm.get('id')
        font_type = ui_elm['properties'].get("font", {})["family"]
        font_family = set_font_family(font_type)
        date_picker_strings = f'''\ndate_picker_{elm_id}_string = """\n#:import utils kivy.utils\n#:import hex kivy.utils.get_color_from_hex '''
        date_picker_strings += strings.date_picker_kivy_string \
            .replace('<<<screen_name>>>', elm_id) \
            .replace('<<<border_color>>>', str(value_map.get('border_color'))) \
            .replace('<<<border_radius>>>', str(value_map.get('border_radius'))) \
            .replace('<<<border_size>>>', str(value_map.get('border_size'))) \
            .replace('<<<text>>>', str(value_map.get('text'))) \
            .replace('<<<font_type>>>', font_family) \
            .replace('<<<font_size>>>', str(value_map.get('font_size'))) \
            .replace('<<<font_color>>>', str(value_map.get('font_color'))) \
            .replace('<<<bg_color>>>', str(value_map.get('bg_color'))) \
            .replace('<<<width>>>', str(value_map.get('width'))) \
            .replace('<<<height>>>', str(value_map.get('height'))) \
            .replace('<<<margin_left>>>', str(value_map.get('margin_left'))) \
            .replace('<<<margin_top>>>', str(value_map.get('margin_top'))) \
            .replace('<<<margin_right>>>', str(value_map.get('margin_right'))) \
            .replace('<<<margin_bottom>>>', str(value_map.get('margin_bottom'))) \
            .replace('<<<padding_left>>>', str(value_map.get('padding_left'))) \
            .replace('<<<padding_top>>>', str(value_map.get('padding_top'))) \
            .replace('<<<padding_right>>>', str(value_map.get('padding_right'))) \
            .replace('<<<padding_bottom>>>', str(value_map.get('padding_bottom'))) \
            .replace('<<<shadow_x>>>', str(value_map.get('shadow_x'))) \
            .replace('<<<shadow_y>>>', str(value_map.get('shadow_y'))) \
            .replace('<<<shadow_blur>>>', str(value_map.get('blur'))) \
            .replace('<<<shadow_color>>>', str(value_map.get('shadow_color'))) \
            .replace('<<<width_margin_adj>>>', str(value_map.get('width_margin_adjustment'))) \
            .replace('<<<height_margin_adj>>>', str(value_map.get('height_margin_adjustment')))
        date_picker_strings += '"""'
        return date_picker_strings

    @staticmethod
    def time_picker_kivy(ui_elm, parent_element):
        value_map = process_element_properties(ui_elm)
        elm_id = ui_elm.get('id')
        font_type = ui_elm['properties'].get("font", {})["family"]
        font_family = set_font_family(font_type)
        time_picker_strings = f'''\ntime_picker_{elm_id}_string = """\n#:import utils kivy.utils\n#:import hex kivy.utils.get_color_from_hex '''
        time_picker_strings += strings.time_picker_kivy_string \
            .replace('<<<screen_name>>>', elm_id) \
            .replace('<<<border_color>>>', str(value_map.get('border_color'))) \
            .replace('<<<border_radius>>>', str(value_map.get('border_radius'))) \
            .replace('<<<border_size>>>', str(value_map.get('border_size'))) \
            .replace('<<<text>>>', str(value_map.get('text'))) \
            .replace('<<<font_type>>>', font_family) \
            .replace('<<<font_size>>>', str(value_map.get('font_size'))) \
            .replace('<<<font_color>>>', str(value_map.get('font_color'))) \
            .replace('<<<bg_color>>>', str(value_map.get('bg_color'))) \
            .replace('<<<width>>>', str(value_map.get('width'))) \
            .replace('<<<height>>>', str(value_map.get('height'))) \
            .replace('<<<margin_left>>>', str(value_map.get('margin_left'))) \
            .replace('<<<margin_top>>>', str(value_map.get('margin_top'))) \
            .replace('<<<margin_right>>>', str(value_map.get('margin_right'))) \
            .replace('<<<margin_bottom>>>', str(value_map.get('margin_bottom'))) \
            .replace('<<<padding_left>>>', str(value_map.get('padding_left'))) \
            .replace('<<<padding_top>>>', str(value_map.get('padding_top'))) \
            .replace('<<<padding_right>>>', str(value_map.get('padding_right'))) \
            .replace('<<<padding_bottom>>>', str(value_map.get('padding_bottom'))) \
            .replace('<<<shadow_x>>>', str(value_map.get('shadow_x'))) \
            .replace('<<<shadow_y>>>', str(value_map.get('shadow_y'))) \
            .replace('<<<shadow_blur>>>', str(value_map.get('blur'))) \
            .replace('<<<shadow_color>>>', str(value_map.get('shadow_color'))) \
            .replace('<<<width_margin_adj>>>', str(value_map.get('width_margin_adjustment'))) \
            .replace('<<<height_margin_adj>>>', str(value_map.get('height_margin_adjustment')))

        time_picker_strings += '"""'
        return time_picker_strings

    @staticmethod
    def list_viewer_kivy(ui_elm, parent_element):
        value_map = process_element_properties(ui_elm)
        elm_id = ui_elm.get('id')
        font_type = ui_elm['properties'].get("font", {})["family"]
        font_family = set_font_family(font_type)
        list_items = ui_elm['properties'].get("list")
        bg_color = ui_elm['properties'].get("bgcolor")
        list_item_strings = ''
        count = 0
        for list_item in list_items:
            count += 1
            list_item_strings += strings.list_item_kivy_string \
                .replace('<<<text>>>', list_item.get('name')) \
                .replace('<<<font_type>>>', font_family) \
                .replace('<<<font_size>>>', str(value_map.get('font_size'))) \
                .replace('<<<font_color>>>', str(value_map.get('font_color'))) \
                .replace('<<<bg_color>>>', str(bg_color)) \
                .replace('<<<width>>>', str(value_map.get('width'))) \
                .replace('<<<height>>>', str(value_map.get('height'))) \
                .replace('<<<padding_left>>>', str(value_map.get('padding_left'))) \
                .replace('<<<padding_top>>>', str(value_map.get('padding_top'))) \
                .replace('<<<padding_right>>>', str(value_map.get('padding_right'))) \
                .replace('<<<padding_bottom>>>', str(value_map.get('padding_bottom'))) \
                .replace('<<<count>>>', str(count))
        list_viewer_strings = f'''\nlist_viewer_{elm_id}_string = """\n#:import utils kivy.utils\n#:import hex kivy.utils.get_color_from_hex '''
        list_viewer_strings += strings.list_viewer_kivy_string \
            .replace('<<<screen_name>>>', elm_id) \
            .replace('<<<margin_left>>>', str(value_map.get('margin_left'))) \
            .replace('<<<margin_top>>>', str(value_map.get('margin_top'))) \
            .replace('<<<margin_right>>>', str(value_map.get('margin_right'))) \
            .replace('<<<margin_bottom>>>', str(value_map.get('margin_bottom'))) \
            .replace('#<<<new_list_item_marking>>>', list_item_strings)

        list_viewer_strings += '"""'
        return list_viewer_strings

    @staticmethod
    def web_view_kivy(ui_elm, parent_element, screen_file):
        value_map = process_element_properties(ui_elm)
        elm_id = ui_elm.get('id')
        webview_strings = f'''\nweb_view_{elm_id}_string = """\n#:import utils kivy.utils\n#:import hex kivy.utils.get_color_from_hex '''
        webview_strings += strings.webview_kivy_string \
            .replace('<<<screen_name>>>', elm_id) \
            .replace('<<<width>>>', str(value_map.get('width'))) \
            .replace('<<<height>>>', str(value_map.get('height'))) \
            .replace('<<<margin_left>>>', str(value_map.get('margin_left'))) \
            .replace('<<<margin_top>>>', str(value_map.get('margin_top'))) \
            .replace('<<<margin_right>>>', str(value_map.get('margin_right'))) \
            .replace('<<<margin_bottom>>>', str(value_map.get('margin_bottom'))) \
            .replace('<<<padding_left>>>', str(value_map.get('padding_left'))) \
            .replace('<<<padding_top>>>', str(value_map.get('padding_top'))) \
            .replace('<<<padding_right>>>', str(value_map.get('padding_right'))) \
            .replace('<<<padding_bottom>>>', str(value_map.get('padding_bottom')))
        webview_strings += '"""'
        return webview_strings

    @staticmethod
    def table_layout_kivy(ui_elm, parent_element):
        value_map = process_element_properties(ui_elm)
        elm_id = ui_elm.get('id')
        layout_id = 'id_' + elm_id
        table_layout_strings = f'''\ntable_layout_{elm_id}_string = """\n#:import utils kivy.utils\n#:import hex kivy.utils.get_color_from_hex '''
        table_layout_strings += strings.table_layout_kivy_string \
            .replace('<<<layout_id>>>', layout_id) \
            .replace('<<<screen_name>>>', elm_id) \
            .replace('<<<row>>>', ui_elm['properties'].get('columns')) \
            .replace('<<<col>>>', ui_elm['properties'].get('rows')) \
            .replace('<<<bg_color>>>', str(value_map.get('bg_color'))) \
            .replace('<<<width>>>', str(value_map.get('width'))) \
            .replace('<<<height>>>', str(value_map.get('height'))) \
            .replace('<<<margin_left>>>', str(value_map.get('margin_left'))) \
            .replace('<<<margin_top>>>', str(value_map.get('margin_top'))) \
            .replace('<<<margin_right>>>', str(value_map.get('margin_right'))) \
            .replace('<<<margin_bottom>>>', str(value_map.get('margin_bottom'))) \
            .replace('<<<padding_left>>>', str(value_map.get('padding_left'))) \
            .replace('<<<padding_top>>>', str(value_map.get('padding_top'))) \
            .replace('<<<padding_right>>>', str(value_map.get('padding_right'))) \
            .replace('<<<padding_bottom>>>', str(value_map.get('padding_bottom'))) \
            .replace('<<<horizontal_alignment>>>', str(value_map.get('h_align'))) \
            .replace('<<<vertical_alignment>>>', str(value_map.get('v_align'))) \
            .replace('<<<width_margin_adj>>>', str(value_map.get('width_margin_adjustment'))) \
            .replace('<<<height_margin_adj>>>', str(value_map.get('height_margin_adjustment')))
        table_layout_strings += '"""'
        return table_layout_strings

    @staticmethod
    def audio_player_kivy(ui_elm, parent_element):
        value_map = process_element_properties(ui_elm)
        elm_id = ui_elm.get('id')
        layout_id = 'id_' + elm_id
        audio_file_name = ui_elm['properties'].get("file", {})["name"]
        audio_file_url = ui_elm['properties'].get("file", {})["url"]
        if audio_file_name.startswith('http'):
            a = urlparse(audio_file_url)
            audio_file_name = os.path.basename(a.path)
        if audio_file_name:
            audio_file_name, _ = base.file_download(base.kivy_audio_folder, audio_file_url, audio_file_name)

        audio_player_strings = f'''\naudio_player_{elm_id}_string = """\n#:import utils kivy.utils\n#:import hex kivy.utils.get_color_from_hex '''
        audio_player_strings += strings.audio_player_kivy_string \
            .replace('<<<layout_id>>>', layout_id) \
            .replace('<<<screen_name>>>', elm_id) \
            .replace('<<<width>>>', str(value_map.get('width'))) \
            .replace('<<<height>>>', str(value_map.get('height'))) \
            .replace('<<<margin_left>>>', str(value_map.get('margin_left'))) \
            .replace('<<<margin_top>>>', str(value_map.get('margin_top'))) \
            .replace('<<<margin_right>>>', str(value_map.get('margin_right'))) \
            .replace('<<<margin_bottom>>>', str(value_map.get('margin_bottom'))) \
            .replace('<<<padding_left>>>', str(value_map.get('padding_left'))) \
            .replace('<<<padding_top>>>', str(value_map.get('padding_top'))) \
            .replace('<<<padding_right>>>', str(value_map.get('padding_right'))) \
            .replace('<<<padding_bottom>>>', str(value_map.get('padding_bottom'))) \
            .replace('<<<border_radius>>>', str(value_map.get('border_radius'))) \
            .replace('<<<shadow_x>>>', str(value_map.get('shadow_x'))) \
            .replace('<<<shadow_y>>>', str(value_map.get('shadow_y'))) \
            .replace('<<<shadow_blur>>>', str(value_map.get('blur'))) \
            .replace('<<<shadow_color>>>', str(value_map.get('shadow_color'))) \
            .replace('<<<width_margin_adj>>>', str(value_map.get('width_margin_adjustment'))) \
            .replace('<<<height_margin_adj>>>', str(value_map.get('height_margin_adjustment')))
        audio_player_strings += '"""'
        return audio_player_strings

    @staticmethod
    def video_player_kivy(ui_elm, parent_element):
        value_map = process_element_properties(ui_elm)
        elm_id = ui_elm.get('id')
        layout_id = 'id_' + elm_id

        video_file_name = ui_elm['properties'].get("file", {})["name"]
        video_file_url = ui_elm['properties'].get("file", {})["url"]
        if video_file_name.startswith('http'):
            a = urlparse(video_file_url)
            video_file_name = os.path.basename(a.path)
        if video_file_name:
            video_file_name, _ = base.file_download(base.kivy_video_folder, video_file_url, video_file_name)
        video_player_strings = f'''\nvideo_player_{elm_id}_string = """\n#:import utils kivy.utils\n#:import hex kivy.utils.get_color_from_hex '''
        video_player_strings += strings.video_player_kivy_string \
            .replace('<<<layout_id>>>', layout_id) \
            .replace('<<<screen_name>>>', elm_id) \
            .replace('<<<video_file>>>',video_file_name) \
            .replace('<<<width>>>', str(value_map.get('width'))) \
            .replace('<<<height>>>', str(value_map.get('height'))) \
            .replace('<<<margin_left>>>', str(value_map.get('margin_left'))) \
            .replace('<<<margin_top>>>', str(value_map.get('margin_top'))) \
            .replace('<<<margin_right>>>', str(value_map.get('margin_right'))) \
            .replace('<<<margin_bottom>>>', str(value_map.get('margin_bottom'))) \
            .replace('<<<padding_left>>>', str(value_map.get('padding_left'))) \
            .replace('<<<padding_top>>>', str(value_map.get('padding_top'))) \
            .replace('<<<padding_right>>>', str(value_map.get('padding_right'))) \
            .replace('<<<padding_bottom>>>', str(value_map.get('padding_bottom'))) \
            .replace('<<<border_radius>>>', str(value_map.get('border_radius'))) \
            .replace('<<<shadow_x>>>', str(value_map.get('shadow_x'))) \
            .replace('<<<shadow_y>>>', str(value_map.get('shadow_y'))) \
            .replace('<<<shadow_blur>>>', str(value_map.get('blur'))) \
            .replace('<<<shadow_color>>>', str(value_map.get('shadow_color'))) \
            .replace('<<<width_margin_adj>>>', str(value_map.get('width_margin_adjustment'))) \
            .replace('<<<height_margin_adj>>>', str(value_map.get('height_margin_adjustment')))
        video_player_strings += '"""'
        return video_player_strings

    @staticmethod
    def switch_kivy(ui_elm, parent_element):
        value_map = process_element_properties(ui_elm)
        elm_id = ui_elm.get('id')
        action_id = 'action_id_' + elm_id
        width_margin_adjustment = int(value_map.get('margin_left')) + int(value_map.get('margin_right')) + 200
        height_margin_adjustment = int(value_map.get('margin_top')) + int(value_map.get('margin_bottom')) + 50
        switch_strings = f'''\nswitch_{elm_id}_string = """\n#:import utils kivy.utils '''
        switch_strings += strings.switch_kivy_string \
            .replace('<<<action_id>>>', action_id) \
            .replace('<<<screen_name>>>', elm_id) \
            .replace('<<<width>>>', str(value_map.get('width'))) \
            .replace('<<<height>>>', str(value_map.get('height'))) \
            .replace('<<<text>>>', str(value_map.get('text'))) \
            .replace('<<<font_type>>>', str(value_map.get('font_family'))) \
            .replace('<<<font_size>>>', str(value_map.get('font_size'))) \
            .replace('<<<font_color>>>', str(value_map.get('font_color'))) \
            .replace('<<<active_color>>>', str(value_map.get('active_color'))) \
            .replace('<<<inactive_color>>>', str(value_map.get('inactive_color'))) \
            .replace('<<<margin_left>>>', str(value_map.get('margin_left'))) \
            .replace('<<<margin_top>>>', str(value_map.get('margin_top'))) \
            .replace('<<<margin_right>>>', str(value_map.get('margin_right'))) \
            .replace('<<<margin_bottom>>>', str(value_map.get('margin_bottom'))) \
            .replace('<<<padding_left>>>', str(value_map.get('padding_left'))) \
            .replace('<<<padding_top>>>', str(value_map.get('padding_top'))) \
            .replace('<<<padding_right>>>', str(value_map.get('padding_right'))) \
            .replace('<<<padding_bottom>>>', str(value_map.get('padding_bottom'))) \
            .replace('<<<width_margin_adj>>>', str(width_margin_adjustment)) \
            .replace('<<<height_margin_adj>>>', str(height_margin_adjustment))

        switch_strings += '"""'
        return switch_strings

    @staticmethod
    def check_box_kivy(ui_elm, parent_element):
        value_map = process_element_properties(ui_elm)
        elm_id = ui_elm.get('id')
        action_id = 'action_id_' + elm_id
        width_margin_adjustment = int(value_map.get('margin_left')) + int(value_map.get('margin_right')) + 200
        height_margin_adjustment = int(value_map.get('margin_top')) + int(value_map.get('margin_bottom')) + 50
        check_box_strings = f'''\ncheck_box_{elm_id}_string = """\n#:import utils kivy.utils '''
        check_box_strings += strings.check_box_kivy_string \
            .replace('<<<action_id>>>', action_id) \
            .replace('<<<screen_name>>>', elm_id) \
            .replace('<<<width>>>', str(value_map.get('width'))) \
            .replace('<<<height>>>', str(value_map.get('height'))) \
            .replace('<<<text>>>', str(value_map.get('text'))) \
            .replace('<<<font_type>>>', str(value_map.get('font_family'))) \
            .replace('<<<font_size>>>', str(value_map.get('font_size'))) \
            .replace('<<<font_color>>>', str(value_map.get('font_color'))) \
            .replace('<<<active_color>>>', str(value_map.get('active_color'))) \
            .replace('<<<inactive_color>>>', str(value_map.get('inactive_color'))) \
            .replace('<<<margin_left>>>', str(value_map.get('margin_left'))) \
            .replace('<<<margin_top>>>', str(value_map.get('margin_top'))) \
            .replace('<<<margin_right>>>', str(value_map.get('margin_right'))) \
            .replace('<<<margin_bottom>>>', str(value_map.get('margin_bottom'))) \
            .replace('<<<padding_left>>>', str(value_map.get('padding_left'))) \
            .replace('<<<padding_top>>>', str(value_map.get('padding_top'))) \
            .replace('<<<padding_right>>>', str(value_map.get('padding_right'))) \
            .replace('<<<padding_bottom>>>', str(value_map.get('padding_bottom'))) \
            .replace('<<<width_margin_adj>>>', str(width_margin_adjustment)) \
            .replace('<<<height_margin_adj>>>', str(height_margin_adjustment))

        check_box_strings += '"""'
        return check_box_strings

    @staticmethod
    def radio_button_kivy(ui_elm, parent_element):
        value_map = process_element_properties(ui_elm)
        elm_id = ui_elm.get('id')
        action_id = 'action_id_' + elm_id
        width_margin_adjustment = int(value_map.get('margin_left')) + int(value_map.get('margin_right')) + 200
        height_margin_adjustment = int(value_map.get('margin_top')) + int(value_map.get('margin_bottom')) + 50
        radio_button_strings = f'''\nradio_button_{elm_id}_string = """\n#:import utils kivy.utils '''
        radio_button_strings += strings.radio_button_kivy_string \
            .replace('<<<action_id>>>', action_id) \
            .replace('<<<screen_name>>>', elm_id) \
            .replace('<<<width>>>', str(value_map.get('width'))) \
            .replace('<<<height>>>', str(value_map.get('height'))) \
            .replace('<<<text>>>', str(value_map.get('text'))) \
            .replace('<<<font_type>>>', str(value_map.get('font_family'))) \
            .replace('<<<font_size>>>', str(value_map.get('font_size'))) \
            .replace('<<<font_color>>>', str(value_map.get('font_color'))) \
            .replace('<<<active_color>>>', str(value_map.get('active_color'))) \
            .replace('<<<inactive_color>>>', str(value_map.get('inactive_color'))) \
            .replace('<<<margin_left>>>', str(value_map.get('margin_left'))) \
            .replace('<<<margin_top>>>', str(value_map.get('margin_top'))) \
            .replace('<<<margin_right>>>', str(value_map.get('margin_right'))) \
            .replace('<<<margin_bottom>>>', str(value_map.get('margin_bottom'))) \
            .replace('<<<padding_left>>>', str(value_map.get('padding_left'))) \
            .replace('<<<padding_top>>>', str(value_map.get('padding_top'))) \
            .replace('<<<padding_right>>>', str(value_map.get('padding_right'))) \
            .replace('<<<padding_bottom>>>', str(value_map.get('padding_bottom'))) \
            .replace('<<<width_margin_adj>>>', str(width_margin_adjustment)) \
            .replace('<<<height_margin_adj>>>', str(height_margin_adjustment))
        radio_button_strings += '"""'
        return radio_button_strings

    @staticmethod
    def rating_bar_kivy(ui_elm, parent_element):
        value_map = process_element_properties(ui_elm)
        elm_id = ui_elm.get('id')
        action_id = 'action_id_' + elm_id
        width = 250
        width_margin_adjustment = int(value_map.get('margin_left')) + int(value_map.get('margin_right')) + int(
            value_map.get('width'))
        height_margin_adjustment = int(value_map.get('margin_top')) + int(value_map.get('margin_bottom')) + 50
        rating_bar_strings = f'''\nrating_bar_{elm_id}_string = """\n#:import utils kivy.utils '''
        rating_bar_strings += strings.rating_bar_kivy_string \
            .replace('<<<action_id>>>', action_id) \
            .replace('<<<screen_name>>>', elm_id) \
            .replace('<<<width>>>', str(width)) \
            .replace('<<<active_color>>>', str(value_map.get('active_color'))) \
            .replace('<<<inactive_color>>>', str(value_map.get('inactive_color'))) \
            .replace('<<<margin_left>>>', str(value_map.get('margin_left'))) \
            .replace('<<<margin_top>>>', str(value_map.get('margin_top'))) \
            .replace('<<<margin_right>>>', str(value_map.get('margin_right'))) \
            .replace('<<<margin_bottom>>>', str(value_map.get('margin_bottom'))) \
            .replace('<<<padding_left>>>', str(value_map.get('padding_left'))) \
            .replace('<<<padding_top>>>', str(value_map.get('padding_top'))) \
            .replace('<<<padding_right>>>', str(value_map.get('padding_right'))) \
            .replace('<<<padding_bottom>>>', str(value_map.get('padding_bottom'))) \
            .replace('<<<width_margin_adj>>>', str(width_margin_adjustment)) \
            .replace('<<<height_margin_adj>>>', str(height_margin_adjustment))
        rating_bar_strings += '"""'
        return rating_bar_strings

    @staticmethod
    def map_view_kivy(ui_elm, parent_element):
        props = ui_elm['properties']
        width, height, margin, padding = common_height_width_margin_padding(props)
        value_map = process_element_properties(props)
        elm_id = ui_elm.get('id')
        bg_color = (value_map.get('bg_color'))
        h_align = props.get('horizontalAlign')
        v_align = props.get('verticalAlign')
        # font_size, font_color, font_family = common_font_props(props['font'])
        map_view_strings = f'''\nmap_view_{elm_id}_string = """\n#:import utils kivy.utils '''
        map_view_strings += strings.map_view_kivy_string \
            .replace('<<<screen_name>>>', elm_id) \
            .replace('<<<width>>>', str(width)) \
            .replace('<<<height>>>', str(height)) \
            .replace('<<<margin_left>>>', str(value_map.get('margin_left'))) \
            .replace('<<<margin_top>>>', str(value_map.get('margin_top'))) \
            .replace('<<<margin_right>>>', str(value_map.get('margin_right'))) \
            .replace('<<<margin_bottom>>>', str(value_map.get('margin_bottom'))) \
            .replace('<<<padding_left>>>', str(value_map.get('padding_left'))) \
            .replace('<<<padding_top>>>', str(value_map.get('padding_top'))) \
            .replace('<<<padding_right>>>', str(value_map.get('padding_right'))) \
            .replace('<<<padding_bottom>>>', str(value_map.get('padding_bottom')))
        map_view_strings += '"""'
        return map_view_strings
        # font type pending

    @staticmethod
    def audio_picker_kivy(ui_elm, parent_element):
        value_map = process_element_properties(ui_elm)
        elm_id = ui_elm.get('id')
        font_type = ui_elm['properties'].get("font", {})["family"]
        font_family = set_font_family(font_type)
        audio_picker_strings = f'''\naudio_picker_{elm_id}_string = """\n#:import utils kivy.utils\n#:import hex kivy.utils.get_color_from_hex '''
        audio_picker_strings += strings.audio_picker_kivy_string \
            .replace('<<<screen_name>>>', elm_id) \
            .replace('<<<border_color>>>', str(value_map.get('border_color'))) \
            .replace('<<<border_radius>>>', str(value_map.get('border_radius'))) \
            .replace('<<<text>>>', str(value_map.get('text'))) \
            .replace('<<<font_type>>>', font_family) \
            .replace('<<<font_size>>>', str(value_map.get('font_size'))) \
            .replace('<<<font_color>>>', str(value_map.get('font_color'))) \
            .replace('<<<bg_color>>>', str(value_map.get('bg_color'))) \
            .replace('<<<width>>>', str(value_map.get('width'))) \
            .replace('<<<height>>>', str(value_map.get('height'))) \
            .replace('<<<margin_left>>>', str(value_map.get('margin_left'))) \
            .replace('<<<margin_top>>>', str(value_map.get('margin_top'))) \
            .replace('<<<margin_right>>>', str(value_map.get('margin_right'))) \
            .replace('<<<margin_bottom>>>', str(value_map.get('margin_bottom'))) \
            .replace('<<<padding_left>>>', str(value_map.get('padding_left'))) \
            .replace('<<<padding_top>>>', str(value_map.get('padding_top'))) \
            .replace('<<<padding_right>>>', str(value_map.get('padding_right'))) \
            .replace('<<<padding_bottom>>>', str(value_map.get('padding_bottom'))) \
            .replace('<<<shadow_x>>>', str(value_map.get('shadow_x'))) \
            .replace('<<<shadow_y>>>', str(value_map.get('shadow_y'))) \
            .replace('<<<shadow_blur>>>', str(value_map.get('blur'))) \
            .replace('<<<shadow_color>>>', str(value_map.get('shadow_color'))) \
            .replace('<<<width_margin_adj>>>', str(value_map.get('width_margin_adjustment'))) \
            .replace('<<<height_margin_adj>>>', str(value_map.get('height_margin_adjustment')))
        audio_picker_strings += '"""'
        return audio_picker_strings

    @staticmethod
    def video_picker_kivy(ui_elm, parent_element):
        value_map = process_element_properties(ui_elm)
        elm_id = ui_elm.get('id')
        font_type = ui_elm['properties'].get("font", {})["family"]
        font_family = set_font_family(font_type)
        video_picker_strings = f'''\nvideo_picker_{elm_id}_string = """\n#:import utils kivy.utils\n#:import hex kivy.utils.get_color_from_hex '''
        video_picker_strings += strings.video_picker_kivy_string \
            .replace('<<<screen_name>>>', elm_id) \
            .replace('<<<border_color>>>', str(value_map.get('border_color'))) \
            .replace('<<<border_radius>>>', str(value_map.get('border_radius'))) \
            .replace('<<<border_size>>>', str(value_map.get('border_size'))) \
            .replace('<<<text>>>', str(value_map.get('text'))) \
            .replace('<<<font_type>>>', font_family) \
            .replace('<<<font_size>>>', str(value_map.get('font_size'))) \
            .replace('<<<font_color>>>', str(value_map.get('font_color'))) \
            .replace('<<<bg_color>>>', str(value_map.get('bg_color'))) \
            .replace('<<<width>>>', str(value_map.get('width'))) \
            .replace('<<<height>>>', str(value_map.get('height'))) \
            .replace('<<<margin_left>>>', str(value_map.get('margin_left'))) \
            .replace('<<<margin_top>>>', str(value_map.get('margin_top'))) \
            .replace('<<<margin_right>>>', str(value_map.get('margin_right'))) \
            .replace('<<<margin_bottom>>>', str(value_map.get('margin_bottom'))) \
            .replace('<<<padding_left>>>', str(value_map.get('padding_left'))) \
            .replace('<<<padding_top>>>', str(value_map.get('padding_top'))) \
            .replace('<<<padding_right>>>', str(value_map.get('padding_right'))) \
            .replace('<<<padding_bottom>>>', str(value_map.get('padding_bottom'))) \
            .replace('<<<shadow_x>>>', str(value_map.get('shadow_x'))) \
            .replace('<<<shadow_y>>>', str(value_map.get('shadow_y'))) \
            .replace('<<<shadow_blur>>>', str(value_map.get('blur'))) \
            .replace('<<<shadow_color>>>', str(value_map.get('shadow_color'))) \
            .replace('<<<width_margin_adj>>>', str(value_map.get('width_margin_adjustment'))) \
            .replace('<<<height_margin_adj>>>', str(value_map.get('height_margin_adjustment')))
        video_picker_strings += '"""'
        return video_picker_strings

    @staticmethod
    def slider_kivy(ui_elm, parent_element):
        value_map = process_element_properties(ui_elm)
        elm_id = ui_elm.get('id')
        action_id = 'action_id_' + elm_id
        active_thumb_color = ui_elm['properties'].get('thumbColor')
        active_track_color = ui_elm['properties'].get('colorLeft')
        inactive_track_color = ui_elm['properties'].get('colorRight')
        width_margin_adjustment = int(value_map.get('margin_left')) + int(value_map.get('margin_right')) + 200
        height_margin_adjustment = int(value_map.get('margin_top')) + int(value_map.get('margin_bottom')) + 50
        slider_strings = f'''\nslider_{elm_id}_string = """\n#:import utils kivy.utils '''
        slider_strings += strings.slider_kivy_string \
            .replace('<<<action_id>>>', action_id) \
            .replace('<<<screen_name>>>', elm_id) \
            .replace('<<<width>>>', str(value_map.get('width'))) \
            .replace('<<<height>>>', str(value_map.get('height'))) \
            .replace('<<<active_thumb_color>>>', active_thumb_color) \
            .replace('<<<active_track_color>>>', active_track_color) \
            .replace('<<<inactive_track_color>>>', inactive_track_color) \
            .replace('<<<margin_left>>>', str(value_map.get('margin_left'))) \
            .replace('<<<margin_top>>>', str(value_map.get('margin_top'))) \
            .replace('<<<margin_right>>>', str(value_map.get('margin_right'))) \
            .replace('<<<margin_bottom>>>', str(value_map.get('margin_bottom'))) \
            .replace('<<<padding_left>>>', str(value_map.get('padding_left'))) \
            .replace('<<<padding_top>>>', str(value_map.get('padding_top'))) \
            .replace('<<<padding_right>>>', str(value_map.get('padding_right'))) \
            .replace('<<<padding_bottom>>>', str(value_map.get('padding_bottom'))) \
            .replace('<<<width_margin_adj>>>', str(width_margin_adjustment)) \
            .replace('<<<height_margin_adj>>>', str(height_margin_adjustment))
        slider_strings += '"""'
        return slider_strings

    @staticmethod
    def barcode_scanner_kivy(ui_elm, parent_element):
        value_map = process_element_properties(ui_elm)
        elm_id = ui_elm.get('id')
        font_type = ui_elm['properties'].get("font", {})["family"]
        font_family = set_font_family(font_type)
        barcode_scanner_strings = f'''\nbarcode_scanner_{elm_id}_string = """\n#:import utils kivy.utils\n#:import hex kivy.utils.get_color_from_hex '''
        barcode_scanner_strings += strings.barcode_scanner_kivy_string \
            .replace('<<<screen_name>>>', elm_id) \
            .replace('<<<border_color>>>', str(value_map.get('border_color'))) \
            .replace('<<<border_radius>>>', str(value_map.get('border_radius'))) \
            .replace('<<<border_size>>>', str(value_map.get('border_size'))) \
            .replace('<<<text>>>', str(value_map.get('text'))) \
            .replace('<<<font_type>>>', font_family) \
            .replace('<<<font_size>>>', str(value_map.get('font_size'))) \
            .replace('<<<font_color>>>', str(value_map.get('font_color'))) \
            .replace('<<<bg_color>>>', str(value_map.get('bg_color'))) \
            .replace('<<<width>>>', str(value_map.get('width'))) \
            .replace('<<<height>>>', str(value_map.get('height'))) \
            .replace('<<<margin_left>>>', str(value_map.get('margin_left'))) \
            .replace('<<<margin_top>>>', str(value_map.get('margin_top'))) \
            .replace('<<<margin_right>>>', str(value_map.get('margin_right'))) \
            .replace('<<<margin_bottom>>>', str(value_map.get('margin_bottom'))) \
            .replace('<<<padding_left>>>', str(value_map.get('padding_left'))) \
            .replace('<<<padding_top>>>', str(value_map.get('padding_top'))) \
            .replace('<<<padding_right>>>', str(value_map.get('padding_right'))) \
            .replace('<<<padding_bottom>>>', str(value_map.get('padding_bottom'))) \
            .replace('<<<shadow_x>>>', str(value_map.get('shadow_x'))) \
            .replace('<<<shadow_y>>>', str(value_map.get('shadow_y'))) \
            .replace('<<<shadow_blur>>>', str(value_map.get('blur'))) \
            .replace('<<<shadow_color>>>', str(value_map.get('shadow_color'))) \
            .replace('<<<width_margin_adj>>>', str(value_map.get('width_margin_adjustment'))) \
            .replace('<<<height_margin_adj>>>', str(value_map.get('height_margin_adjustment')))
        barcode_scanner_strings += '"""'
        return barcode_scanner_strings

    @staticmethod
    def camera_button_kivy(ui_elm, parent_element):
        value_map = process_element_properties(ui_elm)
        elm_id = ui_elm.get('id')
        font_type = ui_elm['properties'].get("font", {})["family"]
        font_family = set_font_family(font_type)
        switch_button_strings = f'''\nswitch_button_{elm_id}_string = """\n#:import utils kivy.utils\n#:import hex kivy.utils.get_color_from_hex '''
        switch_button_strings += strings.switch_button_kivy_string \
            .replace('<<<screen_name>>>', elm_id) \
            .replace('<<<border_color>>>', str(value_map.get('border_color'))) \
            .replace('<<<border_radius>>>', str(value_map.get('border_radius'))) \
            .replace('<<<border_size>>>', str(value_map.get('border_size'))) \
            .replace('<<<text>>>', str(value_map.get('text'))) \
            .replace('<<<font_type>>>', font_family) \
            .replace('<<<font_size>>>', str(value_map.get('font_size'))) \
            .replace('<<<font_color>>>', str(value_map.get('font_color'))) \
            .replace('<<<bg_color>>>', str(value_map.get('bg_color'))) \
            .replace('<<<width>>>', str(value_map.get('width'))) \
            .replace('<<<height>>>', str(value_map.get('height'))) \
            .replace('<<<margin_left>>>', str(value_map.get('margin_left'))) \
            .replace('<<<margin_top>>>', str(value_map.get('margin_top'))) \
            .replace('<<<margin_right>>>', str(value_map.get('margin_right'))) \
            .replace('<<<margin_bottom>>>', str(value_map.get('margin_bottom'))) \
            .replace('<<<padding_left>>>', str(value_map.get('padding_left'))) \
            .replace('<<<padding_top>>>', str(value_map.get('padding_top'))) \
            .replace('<<<padding_right>>>', str(value_map.get('padding_right'))) \
            .replace('<<<padding_bottom>>>', str(value_map.get('padding_bottom'))) \
            .replace('<<<shadow_x>>>', str(value_map.get('shadow_x'))) \
            .replace('<<<shadow_y>>>', str(value_map.get('shadow_y'))) \
            .replace('<<<shadow_blur>>>', str(value_map.get('blur'))) \
            .replace('<<<shadow_color>>>', str(value_map.get('shadow_color'))) \
            .replace('<<<width_margin_adj>>>', str(value_map.get('width_margin_adjustment'))) \
            .replace('<<<height_margin_adj>>>', str(value_map.get('height_margin_adjustment')))

        switch_button_strings += '"""'
        return switch_button_strings

    @staticmethod
    def rating_star_kivy(ui_elm, parent_element):
        value_map = process_element_properties(ui_elm)
        elm_id = ui_elm.get('id')
        font_type = ui_elm['properties'].get("font", {})["family"]
        font_family = set_font_family(font_type)
        rating_star_strings = f'''\nrating_star_{elm_id}_string = """\n#:import utils kivy.utils\n#:import hex kivy.utils.get_color_from_hex '''
        rating_star_strings += strings.rating_bar_kivy_string \
            .replace('<<<screen_name>>>', elm_id) \
            .replace('<<<border_color>>>', str(value_map.get('border_color'))) \
            .replace('<<<border_radius>>>', str(value_map.get('border_radius'))) \
            .replace('<<<border_size>>>', str(value_map.get('border_size'))) \
            .replace('<<<text>>>', str(value_map.get('text'))) \
            .replace('<<<font_type>>>', font_family) \
            .replace('<<<font_size>>>', str(value_map.get('font_size'))) \
            .replace('<<<font_color>>>', str(value_map.get('font_color'))) \
            .replace('<<<bg_color>>>', str(value_map.get('bg_color'))) \
            .replace('<<<width>>>', str(value_map.get('width'))) \
            .replace('<<<height>>>', str(value_map.get('height'))) \
            .replace('<<<margin_left>>>', str(value_map.get('margin_left'))) \
            .replace('<<<margin_top>>>', str(value_map.get('margin_top'))) \
            .replace('<<<margin_right>>>', str(value_map.get('margin_right'))) \
            .replace('<<<margin_bottom>>>', str(value_map.get('margin_bottom'))) \
            .replace('<<<padding_left>>>', str(value_map.get('padding_left'))) \
            .replace('<<<padding_top>>>', str(value_map.get('padding_top'))) \
            .replace('<<<padding_right>>>', str(value_map.get('padding_right'))) \
            .replace('<<<padding_bottom>>>', str(value_map.get('padding_bottom'))) \
            .replace('<<<shadow_x>>>', str(value_map.get('shadow_x'))) \
            .replace('<<<shadow_y>>>', str(value_map.get('shadow_y'))) \
            .replace('<<<shadow_blur>>>', str(value_map.get('blur'))) \
            .replace('<<<shadow_color>>>', str(value_map.get('shadow_color'))) \
            .replace('<<<width_margin_adj>>>', str(value_map.get('width_margin_adjustment'))) \
            .replace('<<<height_margin_adj>>>', str(value_map.get('height_margin_adjustment')))

        rating_star_strings += '"""'
        return rating_star_strings

    @staticmethod
    def modal_view_kivy(ui_elm, parent_element):
        modal_type=" "
        modal_type=ui_elm['properties']['modalType']
        if modal_type == 'normal':
            value_map = process_element_properties(ui_elm)
            elm_id = ui_elm.get('id')
            font_type = ui_elm['properties'].get("font", {})["family"]
            font_family = set_font_family(font_type)
            modal_view_strings = f'''\nmodal_view_{elm_id}_string = """\n#:import utils kivy.utils\n#:import hex kivy.utils.get_color_from_hex '''
            modal_view_strings += strings.normal_modal_kivy_string \
                .replace('<<<screen_name>>>', elm_id) \
                .replace('<<<border_color>>>', str(value_map.get('border_color'))) \
                .replace('<<<border_radius>>>', str(value_map.get('border_radius'))) \
                .replace('<<<border_size>>>', str(value_map.get('border_size'))) \
                .replace('<<<bg_color>>>', str(value_map.get('bg_color'))) \
                .replace('<<<width>>>', str(value_map.get('width'))) \
                .replace('<<<height>>>', str(value_map.get('height'))) \
                .replace('<<<margin_left>>>', str(value_map.get('margin_left'))) \
                .replace('<<<margin_top>>>', str(value_map.get('margin_top'))) \
                .replace('<<<margin_right>>>', str(value_map.get('margin_right'))) \
                .replace('<<<margin_bottom>>>', str(value_map.get('margin_bottom'))) \
                .replace('<<<padding_left>>>', str(value_map.get('padding_left'))) \
                .replace('<<<padding_top>>>', str(value_map.get('padding_top'))) \
                .replace('<<<padding_right>>>', str(value_map.get('padding_right'))) \
                .replace('<<<padding_bottom>>>', str(value_map.get('padding_bottom'))) \
                .replace('<<<width_margin_adj>>>', str(value_map.get('width_margin_adjustment'))) \
                .replace('<<<height_margin_adj>>>', str(value_map.get('height_margin_adjustment')))
        else:
            value_map = process_element_properties(ui_elm)
            elm_id = ui_elm.get('id')
            font_type = ui_elm['properties'].get("font", {})["family"]
            font_family = set_font_family(font_type)
            modal_view_strings = f'''\nmodal_view_{elm_id}_string = """\n#:import utils kivy.utils\n#:import hex kivy.utils.get_color_from_hex '''
            modal_view_strings += strings.bottom_modal_string \
                .replace('<<<screen_name>>>', elm_id) \
                .replace('<<<border_color>>>', str(value_map.get('border_color'))) \
                .replace('<<<border_radius>>>', str(value_map.get('border_radius'))) \
                .replace('<<<border_size>>>', str(value_map.get('border_size'))) \
                .replace('<<<text>>>', str(value_map.get('text'))) \
                .replace('<<<font_type>>>', font_family) \
                .replace('<<<font_size>>>', str(value_map.get('font_size'))) \
                .replace('<<<font_color>>>', str(value_map.get('font_color'))) \
                .replace('<<<bg_color>>>', str(value_map.get('bg_color'))) \
                .replace('<<<width>>>', str(value_map.get('width'))) \
                .replace('<<<height>>>', str(value_map.get('height'))) \
                .replace('<<<margin_left>>>', str(value_map.get('margin_left'))) \
                .replace('<<<margin_top>>>', str(value_map.get('margin_top'))) \
                .replace('<<<margin_right>>>', str(value_map.get('margin_right'))) \
                .replace('<<<margin_bottom>>>', str(value_map.get('margin_bottom'))) \
                .replace('<<<padding_left>>>', str(value_map.get('padding_left'))) \
                .replace('<<<padding_top>>>', str(value_map.get('padding_top'))) \
                .replace('<<<padding_right>>>', str(value_map.get('padding_right'))) \
                .replace('<<<padding_bottom>>>', str(value_map.get('padding_bottom'))) \
                .replace('<<<shadow_x>>>', str(value_map.get('shadow_x'))) \
                .replace('<<<shadow_y>>>', str(value_map.get('shadow_y'))) \
                .replace('<<<shadow_blur>>>', str(value_map.get('blur'))) \
                .replace('<<<shadow_color>>>', str(value_map.get('shadow_color'))) \
                .replace('<<<width_margin_adj>>>', str(value_map.get('width_margin_adjustment'))) \
                .replace('<<<height_margin_adj>>>', str(value_map.get('height_margin_adjustment')))

        modal_view_strings += '"""'
        return modal_view_strings

    @staticmethod
    def side_menu_kivy(ui_elm, parent_element):
        value_map = process_element_properties(ui_elm)
        elm_id = ui_elm.get('id')
        font_type = ui_elm['properties'].get("font", {})["family"]
        font_family = set_font_family(font_type)
        active_tab_color = ui_elm['properties'].get("tabActiveColor")
        inactive_tab_color = ui_elm['properties'].get("tabBgColor")
        active_text_color = ui_elm['properties'].get("tabIndicatorColor")
        inactive_text_color = ui_elm['properties'].get("tabInactiveColor")
        side_menu_tabs = ui_elm['properties'].get('list')
        side_menu_tab = ''
        count = 0
        for tab in side_menu_tabs:
            count += 1
            tab_bar_id = 'side_menu' + str(count) + "_id"
            side_menu_tab_strings = strings.side_menu_tabs_kivy_string \
                .replace('<<<text>>>', tab.get('text')) \
                .replace('<<<inactive_tab_color>>>', inactive_tab_color) \
                .replace('<<<font_type>>>', font_family) \
                .replace('<<<font_size>>>', str(value_map.get('font_size'))) \
                .replace('<<<tab_bar_id>>>', tab_bar_id)
            side_menu_tab += side_menu_tab_strings
            # .replace('<<<active_tab_color>>>', active_tab_color) \
            # .replace('<<<active_text_color>>>', active_text_color) \
            # .replace('<<<inactive_text_color>>>', inactive_text_color)
        side_menu_strings = f'''\nside_menu_{elm_id}_string = """\n#:import utils kivy.utils\n#:import hex kivy.utils.get_color_from_hex '''
        side_menu_strings += strings.side_menu_kivy_string \
            .replace('<<<screen_name>>>', elm_id) \
            .replace('#<<<side_menu_tab_marking>>>', side_menu_tab)
        side_menu_strings += '"""'
        return side_menu_strings


def common_height_width_margin_padding(props):
    width = (props['width']['value'])
    height = (props['height']['value'])
    screen_margin = list(props.get('margin').values())
    margin = ('[%s]' % ', '.join(map(str, screen_margin)))
    screen_padding = list(props.get('padding').values())
    padding = ('[%s]' % ', '.join(map(str, screen_padding)))
    return width, height, margin, padding


def common_font_props(font):
    font_size = font.get('size')
    color = font.get('color')
    font_color = base.extract_rgba(color)
    font_family = font.get('family')
    list = [font_size, font_color, font_family]
    return list

    # ----------------PYTHON MAIN FILE--------------#
    # Adding ui elements inside screen


class PYTHON:
    @staticmethod
    def horizontal_layout_python(ui_elm, parent_element, screen):
        elm_id = ui_elm.get('id')
        elm_name = 'horizontal_layout_' + str(elm_id) + '_string'
        element_name = ui_elm.get('componentTypeName')
        parent_id = 'id_' + parent_element.get('id')
        screen_id = screen.get('id')
        parent_name = parent_element.get('componentTypeName')
        # adding widget to screen
        marking = '#<<<adding_new_widgets>>>' + parent_element.get('id')
        new_child_marking = '#<<<adding_new_widgets>>>' + elm_id
        action_marking = '#<<<adding_actions_to_element>>>' + elm_id
        # action_fun_marking = '#<<<adding_action_fun_to_element>>>' + screen_id
        action_id = ''
        horizontal_layout_strings = f'''\n        {element_name}{elm_id} = Builder.load_string({elm_name})
        {parent_name}{parent_element.get('id')}.ids.{parent_id}.add_widget({element_name}{elm_id})\n        {marking}
        \n        {new_child_marking}\n        {action_marking}'''

        # setting action
        horizontal_layout = ''
        action_req = ui_elm['properties'].get('actions', {}).get('link')
        if action_req != 0:
            action, action_destination, action_req, action_fun = PYTHON.element_actions(ui_elm, element_name,
                                                                                        parent_element, screen,
                                                                                        action_id)
            horizontal_layout = horizontal_layout_strings.replace(action_marking, action)
        else:
            action_fun_marking = '#<<<adding_action_fun_to_element>>>' + screen_id
            action_fun = action_fun_marking
        return horizontal_layout, action_fun

    @staticmethod
    def vertical_layout_python(ui_elm, parent_element, screen):
        elm_id = ui_elm.get('id')
        elm_name = 'vertical_layout_' + str(elm_id) + '_string'
        element_name = ui_elm.get('componentTypeName')
        parent_id = 'id_' + parent_element.get('id')
        screen_id = screen.get('id')
        parent_name = parent_element.get('componentTypeName')
        # adding widget to screen
        marking = '#<<<adding_new_widgets>>>' + parent_element.get('id')
        new_child_marking = '#<<<adding_new_widgets>>>' + elm_id
        action_marking = '#<<<adding_actions_to_element>>>' + elm_id
        # action_fun_marking = '#<<<adding_action_fun_to_element>>>' + screen_id
        action_id = ''
        vertical_layout_strings = f'''\n        {element_name}{elm_id} = Builder.load_string({elm_name})
        {parent_name}{parent_element.get('id')}.ids.{parent_id}.add_widget({element_name}{elm_id})\n        {marking}
        \n        {new_child_marking}\n        {action_marking}'''

        # setting action
        vertical_layout = ''
        action_req = ui_elm['properties'].get('actions', {}).get('link')
        if action_req != 0:
            action, action_destination, action_req, action_fun = PYTHON.element_actions(ui_elm, element_name,
                                                                                        parent_element, screen,
                                                                                        action_id)
            vertical_layout = vertical_layout_strings.replace(action_marking, action)
        else:
            action_fun_marking = '#<<<adding_action_fun_to_element>>>' + screen_id
            action_fun = action_fun_marking
        return vertical_layout, action_fun

    @staticmethod
    def card_view_python(ui_elm, parent_element, screen):
        elm_id = ui_elm.get('id')
        elm_name = 'card_view_' + str(elm_id) + '_string'
        element_name = ui_elm.get('componentTypeName')
        parent_id = 'id_' + parent_element.get('id')
        screen_id = screen.get('id')
        parent_name = parent_element.get('componentTypeName')
        # adding widget to screen
        marking = '#<<<adding_new_widgets>>>' + parent_element.get('id')
        new_child_marking = '#<<<adding_new_widgets>>>' + elm_id
        action_marking = '#<<<adding_actions_to_element>>>' + elm_id
        # action_fun_marking = '#<<<adding_action_fun_to_element>>>' + screen_id
        action_id = '.ids.action_id_' + elm_id
        card_view_strings = f'''\n        {element_name}{elm_id} = Builder.load_string({elm_name})
        {parent_name}{parent_element.get('id')}.ids.{parent_id}.add_widget({element_name}{elm_id})\n        {marking}
        \n        {new_child_marking}\n        {action_marking}'''

        # setting action
        action_req = ui_elm['properties'].get('actions', {}).get('link')
        if action_req != 0:
            action, action_destination, action_req, action_fun = PYTHON.element_actions(ui_elm, element_name,
                                                                                        parent_element, screen,
                                                                                        action_id)
            card_view = card_view_strings.replace(action_marking, action)
        else:
            action_fun_marking = '#<<<adding_action_fun_to_element>>>' + screen_id
            action_fun = action_fun_marking
        return card_view, action_fun

    @staticmethod
    def tab_navigator_python(ui_elm, parent_element, screen):
        elm_id = ui_elm.get('id')
        screen_id = parent_element.get('id')
        elm_name = 'tab_navigator_' + str(elm_id) + '_string'
        count = 0
        marking = '#<<<adding_new_widgets>>>' + parent_element.get('id')
        action_marking = '#<<<adding_actions_to_element>>>' + elm_id
        tab_navigator_strings = f'''\n        tab_navigator_{elm_id} = Builder.load_string({elm_name})
        self.add_widget(tab_navigator_{elm_id})\n        {marking}
        \n        {action_marking}'''
        action_fun = ''
        tab_list = ui_elm['properties'].get('list')
        for tab in tab_list:
            count += 1
            tab_navigator = ''
            action_req = tab.get('actions', {}).get('link')
            action_destination = tab.get('actions', {}).get('destination')
            action_transition = tab.get('actions', {}).get('transition')

            tab_id = 'tab' + str(count) + "_id"
            tab_bar_id = 'tab_bar' + str(count) + "_id"
            action_screen_name = 'screen_' + action_destination
            if action_destination:
                action = f'\n        tab_navigator_{elm_id}.ids.{tab_bar_id}.bind(on_press=self.switch_screen_{tab_id})'
                tab_navigator_strings += action
                action_fun += strings.tab_bar_action_function.replace('<<<tab_id>>>', tab_id) \
                    .replace('<<<action_screen_name>>>', action_screen_name) \
                    .replace('<<<screen_id>>>', screen_id)

        return tab_navigator_strings, action_fun

    @staticmethod
    def web_view_python(ui_elm, parent_element, screen):
        elm_id = ui_elm.get('id')
        elm_name = 'web_view_' + str(elm_id) + '_string'
        parent_name = parent_element.get('componentTypeName')
        # adding card view widget to screen
        marking = '#<<<adding_new_widgets>>>' + parent_element.get('id')
        action_marking = '#<<<adding_actions_to_element>>>' + elm_id
        web_view_strings = f'''\n        web_view_{elm_id} = Builder.load_string({elm_name})
        {parent_name}{parent_element.get('id')}.ids.screen_id.add_widget(web_view_{elm_id})\n        {marking}
        \n        {action_marking}'''

        # setting action to web_view
        web_view = ''
        action_fun = ''
        action_req = ui_elm['properties'].get('actions', {}).get('link')
        if action_req != 0:
            elm_name = 'web_view_'
            action, action_destination, action_req, action_fun = PYTHON.element_actions(ui_elm, elm_name,
                                                                                        parent_element, screen)
            web_view = web_view_strings.replace(action_marking, action)
        else:
            pass
        return web_view, action_fun

    @staticmethod
    def list_viewer_python(ui_elm, parent_element, screen):
        elm_id = ui_elm.get('id')
        elm_name = 'list_viewer_' + str(elm_id) + '_string'
        screen_id = screen.get('id')
        # adding list_viewer widget to screen
        marking = '#<<<adding_new_widgets>>>' + parent_element.get('id')
        action_marking = '#<<<adding_actions_to_element>>>' + elm_id
        list_viewer_strings = f'''\n        list_viewer_{elm_id} = Builder.load_string({elm_name})
        Screen{parent_element.get('id')}.ids.id_{screen_id}.add_widget(list_viewer_{elm_id})\n        {marking}
        \n        {action_marking}'''
        # setting action to list_viewer
        list_items = ui_elm['properties'].get('list')
        action_fun = ''
        # action_req = '0'
        count = 0
        for list_item in list_items:
            action_destination = list_item.get('destination')
            count += 1
            action_req = list_item.get('link')
            action = ''
            # action to screen
            if int(action_req) == 1 and action_req != 0:
                action = f'\n        list_viewer_{elm_id}.ids.list{count}_id.bind(on_press=self.switch_screen{screen_id}_{elm_id}{count})'
                action_destination = 'screen_' + action_destination
                transition_value_map = {
                    "Slide Left": "left",
                    "Slide Right": "right",
                    "Slide Up": "up",
                    "Slide Down": "down"
                }
                screen_transition = transition_value_map.get(list_item.get('transition'))
                action_fun = strings.action_to_screen
                action_fun = action_fun.replace('<<<action_screen_name>>>', action_destination) \
                    .replace('<<<transition>>>', screen_transition) \
                    .replace('<<<elm_id>>>', elm_id) \
                    .replace('<<<screen_id>>>', screen_id) \
                    .replace('<<<list_count>>>', str(count)) \
                    # action to modal
            if int(action_req) == 2:
                action = f'{elm_name}.ids.list_id{count}.bind(on_press=self.open_modal{elm_id})'
                action_fun = strings.action_to_modal
                action_fun = action_fun.replace('<<<elm_id>>>', elm_id) \
                    .replace('<<<screen_id>>>', screen_id)

            # action to url
            if action_req == 3 and action_req != 0:
                action = f'{elm_name}.ids.list_id{count}.bind(on_press=self.open_web{count}_{elm_id})'
                action_fun = strings.list_action_to_web
                action_fun = action_fun.replace('<<<url>>>', action_destination) \
                    .replace('<<<elm_id>>>', elm_id) \
                    .replace('<<<screen_id>>>', screen_id) \
                    .replace('<<<list_count>>>', str(count))
            list_viewer = list_viewer_strings.replace(action_marking, action)
            return list_viewer, action_fun

    @staticmethod
    def image_picker_python(ui_elm, parent_element, screen):
        elm_id = ui_elm.get('id')
        parent_name = parent_element.get('componentTypeName')
        parent_id = parent_element.get('id')
        elm_name = 'image_picker_' + str(elm_id) + '_string'
        element_name = ui_elm.get('componentTypeName')
        screen_id = screen.get('id')
        # adding widget to screen
        marking = '#<<<adding_new_widgets>>>' + parent_element.get('id')
        new_child_marking = '#<<<adding_new_widgets>>>' + elm_id
        action_marking = '#<<<adding_actions_to_element>>>' + elm_id
        # action_fun_marking = '#<<<adding_action_fun_to_element>>>' + screen_id
        action_id = 'image_picker_' + elm_id
        image_picker_strings = f'''\n        image_picker_{elm_id} = Builder.load_string({elm_name})
        {parent_name}{parent_id}.ids.id_{parent_id}.add_widget(image_picker_{elm_id})\n        {marking}
        \n        {action_marking}'''

        # setting functionality
        image_picker_function = strings.image_picker_python_string
        image_picker_function = image_picker_function.replace('<<<image_picker>>>', action_id) \
            .replace('<<<element_id>>>', elm_id)

        image_picker_function += f'        image_picker_{elm_id}.ids.image_picker_id.bind(on_press=file_select{elm_id})'
        image_picker = image_picker_strings + image_picker_function
        return image_picker

    @staticmethod
    def date_picker_python(ui_elm, parent_element, screen):
        elm_id = ui_elm.get('id')
        parent_name = parent_element.get('componentTypeName')
        parent_id = parent_element.get('id')
        elm_name = 'date_picker_' + str(elm_id) + '_string'
        element_name = ui_elm.get('componentTypeName')
        screen_id = screen.get('id')
        # adding widget to screen
        marking = '#<<<adding_new_widgets>>>' + parent_element.get('id')
        new_child_marking = '#<<<adding_new_widgets>>>' + elm_id
        action_marking = '#<<<adding_actions_to_element>>>' + elm_id
        # action_fun_marking = '#<<<adding_action_fun_to_element>>>' + screen_id
        action_id = 'date_picker_' + elm_id
        date_picker_strings = f'''\n        date_picker_{elm_id} = Builder.load_string({elm_name})
        {parent_name}{parent_id}.ids.id_{parent_id}.add_widget(date_picker_{elm_id})\n        {marking}
        \n        {action_marking}'''

        # setting functionality
        date_picker_function = strings.date_picker_python_string
        date_picker_function = date_picker_function.replace('<<<date_picker>>>', action_id) \
            .replace('<<<element_id>>>', elm_id)
        date_picker_function += f'        date_picker_{elm_id}.ids.date_picker_id.bind(on_press=show_date{elm_id})'
        date_picker = date_picker_strings + date_picker_function
        return date_picker

    @staticmethod
    def time_picker_python(ui_elm, parent_element, screen):
        elm_id = ui_elm.get('id')
        parent_name = parent_element.get('componentTypeName')
        parent_id = parent_element.get('id')
        elm_name = 'time_picker_' + str(elm_id) + '_string'
        element_name = ui_elm.get('componentTypeName')
        screen_id = screen.get('id')
        # adding widget to screen
        marking = '#<<<adding_new_widgets>>>' + parent_element.get('id')
        new_child_marking = '#<<<adding_new_widgets>>>' + elm_id
        action_marking = '#<<<adding_actions_to_element>>>' + elm_id
        # action_fun_marking = '#<<<adding_action_fun_to_element>>>' + screen_id
        action_id = 'time_picker_' + elm_id
        time_picker_strings = f'''\n        time_picker_{elm_id} = Builder.load_string({elm_name})
        {parent_name}{parent_id}.ids.id_{parent_id}.add_widget(time_picker_{elm_id})\n        {marking}
        \n        {action_marking}'''

        # setting functionality
        time_picker_function = strings.time_picker_python_string
        time_picker_function = time_picker_function.replace('<<<time_picker>>>', action_id) \
            .replace('<<<element_id>>>', elm_id)
        time_picker_function += f'        time_picker_{elm_id}.ids.time_picker_id.bind(on_press=show_time{elm_id})'
        # action_req = ui_elm['properties'].get('actions', {}).get('link')
        # if action_req != 0:
        #     action, action_destination, action_req, action_fun = PYTHON.element_actions(ui_elm, element_name,
        #                                                                                 parent_element, screen,
        #                                                                                 action_id)
        #     time_picker = time_picker_strings.replace(action_marking, action)
        # else:
        #     action_fun_marking = '#<<<adding_action_fun_to_element>>>' + screen_id
        #     action_fun = action_fun_marking
        time_picker = time_picker_strings + time_picker_function
        return time_picker

    @staticmethod
    def table_layout_python(ui_elm, parent_element, screen):
        elm_id = ui_elm.get('id')
        elm_name = 'table_layout_' + str(elm_id) + '_string'
        element_name = ui_elm.get('componentTypeName')
        parent_id = 'id_' + parent_element.get('id')
        screen_id = parent_element.get('id')
        parent_name = parent_element.get('componentTypeName')
        # adding widget to screen
        marking = '#<<<adding_new_widgets>>>' + parent_element.get('id')
        new_child_marking = '#<<<adding_new_widgets>>>' + elm_id
        action_marking = '#<<<adding_actions_to_element>>>' + elm_id
        # action_fun_marking = '#<<<adding_action_fun_to_element>>>' + screen_id
        action_id = ''
        table_layout_strings = f'''\n        {element_name}{elm_id} = Builder.load_string({elm_name})
        {parent_name}{parent_element.get('id')}.ids.{parent_id}.add_widget({element_name}{elm_id})\n        {marking}
        \n        {new_child_marking}\n        {action_marking}'''

        # setting action
        table_layout = ''
        action_req = ui_elm['properties'].get('actions', {}).get('link')
        if action_req != 0:
            action, action_destination, action_req, action_fun = PYTHON.element_actions(ui_elm, element_name,
                                                                                        parent_element, screen,
                                                                                        action_id)
            table_layout = table_layout_strings.replace(action_marking, action)
        else:
            action_fun_marking = '#<<<adding_action_fun_to_element>>>' + screen_id
            action_fun = action_fun_marking
        return table_layout, action_fun

    @staticmethod
    def app_bar_python(ui_elm, parent_element, screen):
        elm_id = ui_elm.get('id')
        screen_id = screen.get('id')
        elm_name = 'app_bar_' + str(elm_id) + '_string'
        parent_name = parent_element.get('componentTypeName')
        parent_id = parent_element.get('id')
        # adding widget to screen
        marking = '#<<<adding_new_widgets>>>' + parent_id
        action_marking = '#<<<adding_actions_to_element>>>' + parent_id
        app_bar_strings = f'''\n        app_bar_{elm_id} = Builder.load_string({elm_name})
        self.add_widget(app_bar_{elm_id})\n        {marking}
        \n        {action_marking}'''

        # setting action
        app_bar = ''
        action_function = ''
        action_req = ui_elm['properties'].get('actions', {}).get('link')
        action_id = '.ids.action_id_' + elm_id
        if action_req == 1:
            action_destination = ui_elm['properties'].get('actions', {}).get('destination')
            transition_value_map = {
                "Slide Left": "left",
                "Slide Right": "right",
                "Slide Up": "up",
                "Slide Down": "down"
            }
            screen_transition = transition_value_map.get(ui_elm['properties'].get('actions', {}).get('transition'))
            action_screen_name = 'screen_'+ str(action_destination)
            count=''
            action_function = strings.app_bar_action_to_screen \
                .replace('<<<action_screen_name>>>', action_screen_name) \
                .replace('<<<transition>>>', screen_transition) \
                .replace('<<<elm_id>>>', elm_id) \
                .replace('<<<screen_id>>>', parent_element.get('id')) \
                .replace('<<<list_count>>>', str(count))
            action_function += f'        app_bar_{elm_id}.ids.app_bar_id.bind(on_press=switch_screen{screen_id}_{elm_id})'
        else:
            pass
        return app_bar_strings, action_function


    @staticmethod
    def button_python(ui_elm, parent_element, screen):
        elm_id = ui_elm.get('id')
        elm_name = 'button_' + str(elm_id) + '_string'
        parent_name = parent_element.get('componentTypeName')
        parent_id = parent_element.get('id')
        # adding widget to screen
        marking = '#<<<adding_new_widgets>>>' + parent_element.get('id')
        action_marking = '#<<<adding_actions_to_element>>>' + elm_id
        button_strings = f'''\n        button_{elm_id} = Builder.load_string({elm_name})
        {parent_name}{parent_id}.ids.id_{parent_id}.add_widget(button_{elm_id})\n        {marking}
        \n        {action_marking}'''

        # setting action
        button = ''
        action_fun = ''
        action_req = ui_elm['properties'].get('actions', {}).get('link')
        action_id = '.ids.action_id_' + elm_id
        if action_req != 0:
            elm_name = 'button_'

            action, action_destination, action_req, action_fun = PYTHON.element_actions(ui_elm, elm_name,
                                                                                        parent_element, screen,
                                                                                        action_id)
            button = button_strings.replace(action_marking, action)
        else:
            pass
        return button, action_fun

    @staticmethod
    def image_view_python(ui_elm, parent_element, screen):
        elm_id = ui_elm.get('id')
        elm_name = 'image_view_' + str(elm_id) + '_string'
        parent_name = parent_element.get('componentTypeName')
        parent_id = parent_element.get('id')
        # adding widget to screen
        marking = '#<<<adding_new_widgets>>>' + parent_element.get('id')
        action_marking = '#<<<adding_actions_to_element>>>' + elm_id
        image_view_strings = f'''\n        image_view_{elm_id} = Builder.load_string({elm_name})
        {parent_name}{parent_id}.ids.id_{parent_id}.add_widget(image_view_{elm_id})\n        {marking}
        \n        {action_marking}'''

        # setting action
        image_view = ''
        action_fun = ''
        action_req = ui_elm['properties'].get('actions', {}).get('link')
        action_id = '.ids.action_id_' + elm_id
        if action_req != 0:
            elm_name = 'image_view_'
            action, action_destination, action_req, action_fun = PYTHON.element_actions(ui_elm, elm_name,
                                                                                        parent_element, screen,
                                                                                        action_id)
            image_view = image_view_strings.replace(action_marking, action)
        else:
            pass
        return image_view, action_fun

    @staticmethod
    def text_python(ui_elm, parent_element, screen):
        elm_id = ui_elm.get('id')
        elm_name = 'text_' + str(elm_id) + '_string'
        parent_name = parent_element.get('componentTypeName')
        parent_id = parent_element.get('id')
        # adding widget to screen
        marking = '#<<<adding_new_widgets>>>' + parent_element.get('id')
        action_marking = '#<<<adding_actions_to_element>>>' + elm_id
        text_strings = f'''\n        text_{elm_id} = Builder.load_string({elm_name})
        {parent_name}{parent_id}.ids.id_{parent_id}.add_widget(text_{elm_id})\n        {marking}
        \n        {action_marking}'''

        # setting action
        text = ''
        action_fun = ''
        action_req = ui_elm['properties'].get('actions', {}).get('link')
        action_id = '.ids.action_id_' + elm_id
        if action_req != 0:
            elm_name = 'text_'
            action, action_destination, action_req, action_fun = PYTHON.element_actions(ui_elm, elm_name,
                                                                                        parent_element, screen,
                                                                                        action_id)
            text = text_strings.replace(action_marking, action)
        else:
            pass
        return text, action_fun

    @staticmethod
    def text_field_python(ui_elm, parent_element, screen):
        elm_id = ui_elm.get('id')
        elm_name = 'text_field_' + str(elm_id) + '_string'
        parent_name = parent_element.get('componentTypeName')
        parent_id = parent_element.get('id')
        # adding widget to screen
        marking = '#<<<adding_new_widgets>>>' + parent_element.get('id')
        action_marking = '#<<<adding_actions_to_element>>>' + elm_id
        text_field_strings = f'''\n        text_field_{elm_id} = Builder.load_string({elm_name})
        {parent_name}{parent_id}.ids.id_{parent_id}.add_widget(text_field_{elm_id})\n        {marking}
        \n        {action_marking}'''

        # setting action
        text_field = ''
        action_fun = ''
        action_req = ui_elm['properties'].get('actions', {}).get('link')
        action_id = '.ids.action_id_' + elm_id
        if action_req != 0:
            elm_name = 'text_field_'
            action, action_destination, action_req, action_fun = PYTHON.element_actions(ui_elm, elm_name,
                                                                                        parent_element, screen,
                                                                                        action_id)
            text_field = text_field_strings.replace(action_marking, action)
        else:
            pass
        return text_field, action_fun

    @staticmethod
    def audio_player_python(ui_elm, parent_element, screen):
        elm_id = ui_elm.get('id')

        parent_name = parent_element.get('componentTypeName')
        parent_id = parent_element.get('id')
        elm_name = 'audio_player_' + str(elm_id) + '_string'
        element_name = ui_elm.get('componentTypeName')
        screen_id = screen.get('id')
        # adding widget to screen
        marking = '#<<<adding_new_widgets>>>' + parent_element.get('id')
        new_child_marking = '#<<<adding_new_widgets>>>' + elm_id
        action_marking = '#<<<adding_actions_to_element>>>' + elm_id
        # action_fun_marking = '#<<<adding_action_fun_to_element>>>' + screen_id
        action_id = 'audio_player_' + elm_id
        audio_player_strings = f'''\n        audio_player_{elm_id} = Builder.load_string({elm_name})
        {parent_name}{parent_id}.ids.id_{parent_id}.add_widget(audio_player_{elm_id})\n        {marking}
        \n        {action_marking}'''

        audio_file_name = ui_elm['properties'].get("file", {})["name"]
        print(audio_file_name)
        audio_file_url = ui_elm['properties'].get("file", {})["url"]
        if audio_file_name.startswith('http'):
            a = urlparse(audio_file_url)
            audio_file_name = os.path.basename(a.path)
        if audio_file_name:
            audio_file_name, _ = base.file_download(base.kivy_audio_folder, audio_file_url, audio_file_name)
        print(audio_file_name)
        # setting functionality
        audio_player_function = strings.audio_player_python_string \
            .replace('<<<player>>>', str('audio_player_' + elm_id)) \
            .replace('<<<audio_file_name>>>', audio_file_name)
        # audio_player_function += f'        audio_player_{elm_id}.ids.audio_player_id.bind(on_press=show_date{elm_id})'
        audio_player = audio_player_strings + audio_player_function
        return audio_player

    @staticmethod
    def video_player_python(ui_elm, parent_element, screen):
        elm_id = ui_elm.get('id')

        parent_name = parent_element.get('componentTypeName')
        parent_id = parent_element.get('id')
        elm_name = 'video_player_' + str(elm_id) + '_string'
        element_name = ui_elm.get('componentTypeName')
        screen_id = screen.get('id')
        # adding widget to screen
        marking = '#<<<adding_new_widgets>>>' + parent_element.get('id')
        new_child_marking = '#<<<adding_new_widgets>>>' + elm_id
        action_marking = '#<<<adding_actions_to_element>>>' + elm_id
        # action_fun_marking = '#<<<adding_action_fun_to_element>>>' + screen_id
        action_id = 'video_player_' + elm_id
        video_player_strings = f'''\n        video_player_{elm_id} = Builder.load_string({elm_name})
        {parent_name}{parent_id}.ids.id_{parent_id}.add_widget(video_player_{elm_id})\n        {marking}
        \n        {action_marking}'''

        video_file_name = ui_elm['properties'].get("file", {})["name"]
        print(video_file_name)
        video_file_url = ui_elm['properties'].get("file", {})["url"]
        if video_file_name.startswith('http'):
            a = urlparse(video_file_url)
            video_file_name = os.path.basename(a.path)
        if video_file_name:
            video_file_name, _ = base.file_download(base.kivy_video_folder, video_file_url, video_file_name)
        print(video_file_name)
        # setting functionality
        video_player_function = strings.video_player_python_string \
            .replace('<<<player>>>', str('video_player_' + elm_id)) \
            .replace('<<<video_file_name>>>', video_file_name)
        # video_player_function += f'        video_player_{elm_id}.ids.video_player_id.bind(on_press=show_date{elm_id})'
        video_player = video_player_strings + video_player_function
        return video_player

    @staticmethod
    def radio_button_python(ui_elm, parent_element, screen):
        elm_id = ui_elm.get('id')
        elm_name = 'radio_button_' + str(elm_id) + '_string'
        parent_name = parent_element.get('componentTypeName')
        parent_id = parent_element.get('id')
        # adding widget to screen
        marking = '#<<<adding_new_widgets>>>' + parent_element.get('id')
        action_marking = '#<<<adding_actions_to_element>>>' + elm_id
        radio_button_strings = f'''\n        radio_button_{elm_id} = Builder.load_string({elm_name})
        {parent_name}{parent_id}.ids.id_{parent_id}.add_widget(radio_button_{elm_id})\n        {marking}
        \n        {action_marking}'''

        return radio_button_strings

    @staticmethod
    def switch_python(ui_elm, parent_element, screen):
        elm_id = ui_elm.get('id')
        elm_name = 'switch_' + str(elm_id) + '_string'
        parent_name = parent_element.get('componentTypeName')
        parent_id = parent_element.get('id')
        # adding widget to screen
        marking = '#<<<adding_new_widgets>>>' + parent_element.get('id')
        action_marking = '#<<<adding_actions_to_element>>>' + elm_id
        switch_strings = f'''\n        switch_{elm_id} = Builder.load_string({elm_name})
        {parent_name}{parent_id}.ids.id_{parent_id}.add_widget(switch_{elm_id})\n        {marking}
        \n        {action_marking}'''
        return switch_strings

    @staticmethod
    def check_box_python(ui_elm, parent_element, screen):
        elm_id = ui_elm.get('id')
        elm_name = 'check_box_' + str(elm_id) + '_string'
        parent_name = parent_element.get('componentTypeName')
        parent_id = parent_element.get('id')
        # adding widget to screen
        marking = '#<<<adding_new_widgets>>>' + parent_element.get('id')
        action_marking = '#<<<adding_actions_to_element>>>' + elm_id
        check_box_strings = f'''\n        check_box_{elm_id} = Builder.load_string({elm_name})
        {parent_name}{parent_id}.ids.id_{parent_id}.add_widget(check_box_{elm_id})\n        {marking}
        \n        {action_marking}'''
        return check_box_strings

    @staticmethod
    def camera_view_python(ui_elm, screen, screen_file):
        props = ui_elm['properties']
        elm_id = ui_elm.get('id')
        elm_name = 'camera_view_' + str(elm_id) + '_string'

        # adding widget to screen
        marking = '#<<<adding_new_widgets>>>' + screen.get('id')
        action_marking = '#<<<adding_actions_to_element>>>' + elm_id
        camera_view_strings = f'''\n        camera_view_{elm_id} = Builder.load_string({elm_name})
                screen{screen.get('id')}.ids.screen_id.add_widget(camera_view_{elm_id})\n        {marking}
                \n        {action_marking}'''

        # setting action
        camera_view = ''
        action_fun = ''
        action_req = ui_elm['properties'].get('actions', {}).get('link')
        if action_req != 0:
            elm_name = 'camera_view_'
            action, action_destination, action_req, action_fun = PYTHON.element_actions(ui_elm, elm_name, screen)
            camera_view = camera_view_strings.replace(action_marking, action)
        else:
            pass
        return camera_view, action_fun

    @staticmethod
    def barcode_view_python(ui_elm, screen, screen_file):
        props = ui_elm['properties']
        elm_id = ui_elm.get('id')
        elm_name = 'barcode_scanner_' + str(elm_id) + '_string'

        # adding widget to screen
        marking = '#<<<adding_new_widgets>>>' + screen.get('id')
        action_marking = '#<<<adding_actions_to_element>>>' + elm_id
        barcode_scanner_strings = f'''\n        barcode_scanner_{elm_id} = Builder.load_string({elm_name})
                screen{screen.get('id')}.ids.screen_id.add_widget(barcode_scanner_{elm_id})\n        {marking}
                \n        {action_marking}'''

        # setting action
        barcode_scanner = ''
        action_fun = ''
        action_req = ui_elm['properties'].get('actions', {}).get('link')
        if action_req != 0:
            elm_name = 'barcode_scanner_'
            action, action_destination, action_req, action_fun = PYTHON.element_actions(ui_elm, elm_name, screen)
            barcode_scanner = barcode_scanner_strings.replace(action_marking, action)
        else:
            pass
        return barcode_scanner, action_fun

    @staticmethod
    def slider_python(ui_elm, parent_element, screen):
        elm_id = ui_elm.get('id')
        elm_name = 'slider_' + str(elm_id) + '_string'
        parent_name = parent_element.get('componentTypeName')
        parent_id = parent_element.get('id')
        # adding widget to screen
        marking = '#<<<adding_new_widgets>>>' + parent_element.get('id')
        action_marking = '#<<<adding_actions_to_element>>>' + elm_id
        slider_strings = f'''\n        slider_{elm_id} = Builder.load_string({elm_name})
        {parent_name}{parent_id}.ids.id_{parent_id}.add_widget(slider_{elm_id})\n        {marking}
        \n        {action_marking}'''

        return slider_strings

    @staticmethod
    def rating_bar_python(ui_elm, parent_element, screen):
        elm_id = ui_elm.get('id')
        value_map = process_element_properties(ui_elm)
        elm_name = 'rating_bar_' + str(elm_id) + '_string'

        parent_name = parent_element.get('componentTypeName')
        parent_id = parent_element.get('id')
        active_color = value_map.get('active_color')
        inactive_color = value_map.get('inactive_color')
        rating_bar_function = strings.rating_bar_main_string \
            .replace('<<<active_color>>>', active_color) \
            .replace('<<<inactive_color>>>', inactive_color) \
            .replace('<<<rating_bar>>>', str('rating_bar_' + elm_id))
        # adding widget to screen
        marking = '#<<<adding_new_widgets>>>' + parent_element.get('id')
        action_marking = '#<<<adding_actions_to_element>>>' + elm_id
        rating_bar_strings = f'''\n        rating_bar_{elm_id} = Builder.load_string({elm_name})
        {parent_name}{parent_id}.ids.id_{parent_id}.add_widget(rating_bar_{elm_id})\n        {marking}
        \n        {action_marking}'''

        rating_bar_strings += rating_bar_function
        return rating_bar_strings

    @staticmethod
    def map_view_python(ui_elm, screen, screen_file):
        props = ui_elm['properties']
        elm_id = ui_elm.get('id')
        elm_name = 'map_view_' + str(elm_id) + '_string'

        # adding widget to screen
        marking = '#<<<adding_new_widgets>>>' + screen.get('id')
        action_marking = '#<<<adding_actions_to_element>>>' + elm_id
        map_view_strings = f'''\n        map_view_{elm_id} = Builder.load_string({elm_name})
            screen{screen.get('id')}.ids.screen_id.add_widget(map_view_{elm_id})\n        {marking}
            \n        {action_marking}'''

        # setting action
        map_view = ''
        action_fun = ''
        action_req = ui_elm['properties'].get('actions', {}).get('link')
        if action_req != 0:
            elm_name = 'map_view_'
            action, action_destination, action_req, action_fun = PYTHON.element_actions(ui_elm, elm_name, screen)
            map_view = map_view_strings.replace(action_marking, action)
        else:
            pass
        return map_view, action_fun

    @staticmethod
    def video_picker_python(ui_elm, screen, parent_element):
        elm_id = ui_elm.get('id')
        parent_name = parent_element.get('componentTypeName')
        parent_id = parent_element.get('id')
        elm_name = 'video_picker_' + str(elm_id) + '_string'
        element_name = ui_elm.get('componentTypeName')
        screen_id = screen.get('id')
        # adding widget to screen
        marking = '#<<<adding_new_widgets>>>' + parent_element.get('id')
        new_child_marking = '#<<<adding_new_widgets>>>' + elm_id
        action_marking = '#<<<adding_actions_to_element>>>' + elm_id
        # action_fun_marking = '#<<<adding_action_fun_to_element>>>' + screen_id
        action_id = 'video_picker_' + elm_id
        video_picker_strings = f'''\n        video_picker_{elm_id} = Builder.load_string({elm_name})
        {parent_name}{parent_id}.ids.id_{parent_id}.add_widget(video_picker_{elm_id})\n        {marking}
        \n        {action_marking}'''

        # setting functionality
        video_picker_function = strings.video_picker_python_string
        video_picker_function = video_picker_function.replace('<<<video_picker>>>', action_id) \
            .replace('<<<element_id>>>', elm_id)

        video_picker_function += f'        video_picker_{elm_id}.ids.video_picker_id.bind(on_press=file_select{elm_id})'
        video_picker = video_picker_strings + video_picker_function
        return video_picker

    @staticmethod
    def audio_picker_python(ui_elm, parent_element, screen):
        elm_id = ui_elm.get('id')
        parent_name = parent_element.get('componentTypeName')
        parent_id = parent_element.get('id')
        elm_name = 'audio_picker_' + str(elm_id) + '_string'
        element_name = ui_elm.get('componentTypeName')
        screen_id = screen.get('id')
        # adding widget to screen
        marking = '#<<<adding_new_widgets>>>' + parent_element.get('id')
        new_child_marking = '#<<<adding_new_widgets>>>' + elm_id
        action_marking = '#<<<adding_actions_to_element>>>' + elm_id
        # action_fun_marking = '#<<<adding_action_fun_to_element>>>' + screen_id
        action_id = 'audio_picker_' + elm_id
        audio_picker_strings = f'''\n        audio_picker_{elm_id} = Builder.load_string({elm_name})
        {parent_name}{parent_id}.ids.id_{parent_id}.add_widget(audio_picker_{elm_id})\n        {marking}
        \n        {action_marking}'''

        # setting functionality
        audio_picker_function = strings.audio_picker_python_string
        audio_picker_function = audio_picker_function.replace('<<<audio_picker>>>', action_id) \
            .replace('<<<element_id>>>', elm_id)

        audio_picker_function += f'        audio_picker_{elm_id}.ids.audio_picker_id.bind(on_press=file_select{elm_id})'
        audio_picker = audio_picker_strings + audio_picker_function
        return audio_picker

    @staticmethod
    def side_menu_python(ui_elm, parent_element, screen):
        elm_id = ui_elm.get('id')
        screen_id = parent_element.get('id')
        elm_name = 'side_menu_' + str(elm_id) + '_string'
        tab_list = ui_elm['properties'].get('list')
        count = 0
        side_menu_id = 'side_menu_tab' + str(count) + "_id"
        marking = '#<<<adding_new_widgets>>>' + parent_element.get('id')
        action_marking = '#<<<adding_action_fun_to_element>>>' + elm_id
        side_menu_strings = f'''\n        side_menu_{elm_id} = Builder.load_string({elm_name})
        self.add_widget(side_menu_{elm_id})\n        {marking}
        \n        {action_marking}'''
        action_fun = ''
        tab_list = ui_elm['properties'].get('list')
        for tab in tab_list:
            count += 1
            tab_bar_id = 'side_menu_tab' + str(count) + "_id"
        active_tab_color = ui_elm['properties'].get("tabActiveColor")
        inactive_tab_color = ui_elm['properties'].get("tabBgColor")
        active_text_color = ui_elm['properties'].get("tabIndicatorColor")
        inactive_text_color = ui_elm['properties'].get("tabInactiveColor")
        side_menu_function = strings.side_menu_python_string \
            .replace('<<<active_tab_color>>>', active_tab_color) \
            .replace('<<<inactive_tab_color>>>', inactive_tab_color) \
            .replace('<<<active_text_color>>>', active_text_color) \
            .replace('<<<inactive_text_color>>>', inactive_text_color) \
            .replace('<<<side_menu>>>', str('side_menu_' + elm_id)) \
            .replace('<<<tab_bar_id>>>', str(tab_bar_id))
        side_menu_strings += side_menu_function
        count=0
        for tab in tab_list:
            count += 1
            side_menu = ''
            action_req = tab.get('actions', {}).get('link')
            action_destination = tab.get('actions', {}).get('destination')
            action_transition = tab.get('actions', {}).get('transition')
            side_menu_id = 'side_menu_tab' + str(count) + "_id"
            # tab_bar_id = 'tab_bar' + str(count) + "_id"
            tab_bar_id = 'side_menu_tab' + str(count) + "_id"
            action_screen_name = 'screen_' + action_destination
            if action_destination:
                action = f'\n        side_menu_{elm_id}.ids.{tab_bar_id}.bind(on_press=switch_screen_{side_menu_id})'
                side_menu_strings += action
                action_fun += strings.side_menu_tab_function.replace('<<<side_menu_id>>>', side_menu_id) \
                    .replace('<<<action_screen_name>>>', action_screen_name) \
                    .replace('<<<elm_id>>>', elm_id)
        return side_menu_strings, action_fun

    @staticmethod
    def modal_view_python(ui_elm, parent_element, screen):
        elm_id = ui_elm.get('id')
        parent_name = parent_element.get('componentTypeName')
        parent_id = parent_element.get('id')
        elm_name = 'modal_view_' + str(elm_id) + '_string'
        element_name = ui_elm.get('componentTypeName')
        screen_id = screen.get('id')
        # adding widget to screen
        marking = '#<<<adding_new_widgets>>>' + parent_element.get('id')
        new_child_marking = '#<<<adding_new_widgets>>>' + elm_id
        action_marking = '#<<<adding_actions_to_element>>>' + elm_id
        # action_fun_marking = '#<<<adding_action_fun_to_element>>>' + screen_id
        action_id = 'modal_view_' + elm_id
        modal_view_strings = f'''\n        modal_view_{elm_id} = Builder.load_string({elm_name})
        {parent_name}{parent_id}.ids.id_{parent_id}.add_widget(modal_view_{elm_id})\n        {marking}
                \n        {action_marking}'''
        modal_view = modal_view_strings
        return modal_view


    @staticmethod
    def element_actions(data, elm_name, parent_element, screen, action_id):
        pass
        parent_id = parent_element.get('id')
        action_req = data['properties'].get('actions', {}).get('link')
        action_destination = data['properties'].get('actions', {}).get('destination')
        # action_dictionary = {1: 'open_screen', 2: 'open_modal', 3: 'open_url'}
        elm_id = data.get('id')
        screen_id = screen.get('id')

        # CHECK WHETHER ACTION TO INVALLID SCREEN OR INVALLID MODAL
        # action_status = False
        action = ''
        action_fun = ''
        # action to screen
        if int(action_req) == 0:
            action_fun_marking = '#<<<adding_action_fun_to_element>>>' + screen_id
            action_fun = action_fun_marking

        if int(action_req) == 1 and action_req != 0:
            action = ''
            if elm_name == "text_field_":
                action = f'{elm_name}{elm_id}{action_id}.bind(on_double_tap=self.switch_screen{screen_id}_{elm_id})'
            else:
                action = f'{elm_name}{elm_id}{action_id}.bind(on_press=self.switch_screen{screen_id}_{elm_id})'
            action_destination = 'screen_' + action_destination
            transition_value_map = {
                "Slide Left": "left",
                "Slide Right": "right",
                "Slide Up": "up",
                "Slide Down": "down"
            }
            screen_transition = transition_value_map.get(data['properties'].get('actions', {}).get('transition'))
            action_fun = strings.action_to_screen
            action_fun = action_fun.replace('<<<action_screen_name>>>', action_destination) \
                .replace('<<<transition>>>', screen_transition) \
                .replace('<<<elm_id>>>', elm_id) \
                .replace('<<<parent_id>>>', parent_id) \
                .replace('<<<screen_id>>>', screen_id)

        # action to modal
        if int(action_req) == 2:
            action = f'{elm_name}{elm_id}{action_id}.ids.action_id.bind(on_press=self.open_modal{elm_id})'
            action_fun = strings.action_to_modal
            action_fun = action_fun.replace('<<<elm_id>>>', elm_id) \
                .replace('<<<screen_id>>>', screen_id) \
                .replace('<<<parent_id>>>', parent_id)
        # action to url
        if action_req == 3 and action_req != 0:
            action = f'{elm_name}{elm_id}{action_id}.bind(on_press=self.open_web{elm_id})'
            action_fun = strings.action_to_web
            action_fun = action_fun.replace('<<<url>>>', action_destination) \
                .replace('<<<elm_id>>>', elm_id) \
                .replace('<<<screen_id>>>', screen_id) \
                .replace('<<<parent_id>>>', parent_id)
        return action, action_destination, action_req, action_fun


def set_font_family(font_family):
    if font_family == 'Great Vibes':
        font_name = 'great-vibes.regular.ttf'
    elif font_family == 'Bebas Neue':
        font_name = 'bebas-neue.regular.ttf'
    elif font_family == 'Lato':
        font_name = 'lato.regular.ttf'
    elif font_family == 'Limelight':
        font_name = 'limelight.regular.ttf'
    elif font_family == 'Merriweather Sans':
        font_name = 'merriweather-sans.regular.ttf'
    elif font_family == 'Open Sans':
        font_name = 'open-sans.regular.ttf'
    elif font_family == 'Oswald':
        font_name = 'oswald.regular.ttf'
    elif font_family == 'Playfair Display':
        font_name = 'playfair-display.regular.ttf'
    elif font_family == 'Poppins':
        font_name = 'poppins.regular.ttf'
    elif font_family == 'Raleway':
        font_name = 'raleway.regular.ttf'
    elif font_family == 'Roboto':
        font_name = 'roboto.regular.ttf'
    elif font_family == 'Source Sans Pro':
        font_name = 'source-sans-pro.regular.ttf'
    elif font_family == 'Yellowtail':
        font_name = 'yellowtail.regular.ttf'
    else:
        font_name = 'open-sans.regular.ttf'
    return font_name


def copy_font(symlinks=False, ignore=None):
    src = 'font/'
    dst = Path(base.base_directory + 'fonts/')

    if not dst.exists():
        os.mkdir(dst)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)


def process_element_properties(elm):
    # BASIC PROPERTY VALUES
    value_map = {'width': elm['properties'].get('width', {}).get('value') or "150",
                 'height': elm['properties'].get('height', {}).get('value') or "100",
                 'padding_top': elm['properties'].get("padding", {})["top"] or "0",
                 'padding_bottom': elm['properties'].get("padding", {})["bottom"] or "0",
                 'padding_left': elm['properties'].get("padding", {})["left"] or "0",
                 'padding_right': elm['properties'].get("padding", {})["right"] or "0",
                 'margin_top': elm['properties'].get("margin", {})["top"] or "0",
                 'margin_bottom': elm['properties'].get("margin", {})["bottom"] or "0",
                 'margin_left': elm['properties'].get("margin", {})["left"] or "0",
                 'margin_right': elm['properties'].get("margin", {})["right"] or "0",
                 'bg_color': elm['properties'].get("bgColor") or "#ffffff",
                 'text': elm['properties'].get("text") or "sample-text!"}

    if elm['properties'].get("horizontalAlign"):
        value_map['h_align'] = elm['properties'].get("horizontalAlign") or "center"
        value_map['v_align'] = elm['properties'].get("verticalAlign") or "center"

    if elm['properties'].get("font"):
        value_map['font_size'] = elm['properties'].get("font", {})["size"] or "10"
        font_family = elm['properties'].get("font", {})["family"] or "Verdana-bold"
        value_map['font_family'] = set_font_family(font_family)
        value_map['font_color'] = elm['properties'].get("font", {})["color"] or "#000000"

    if elm['properties'].get("border"):
        value_map['border_color'] = elm['properties'].get("border", {})["color"] or '#ffffff'
        value_map['border_radius'] = elm['properties'].get("border", {})["radius"] or "0"
        value_map['border_size'] = elm['properties'].get("border", {})["size"] or "0"

    if elm['properties'].get("borderRadius"):
        value_map['border_radius'] = elm['properties'].get("borderRadius") or "0"
    else:
        value_map['border_radius'] = '0'

    if elm['properties'].get("borderColor"):
        value_map['border_color'] = elm['properties'].get("borderColor") or '#ffffff'
    else:
        value_map['border_color'] = '#ffffff'

    if elm['properties'].get("shadow"):
        if elm['properties'].get("shadow", {})["isActive"] == True:
            value_map['shadow_x'] = elm['properties'].get("shadow", {})["x"]
            value_map['shadow_y'] = elm['properties'].get("shadow", {})["y"]
            value_map['blur'] = elm['properties'].get("shadow", {})["blur"]
            value_map['shadow_color'] = elm['properties'].get("shadow", {})["color"]

        else:
            value_map['shadow_x'] = 0
            value_map['shadow_y'] = 0
            value_map['blur'] = 0
            value_map['shadow_color'] = "#000000"

    if elm['properties'].get("checkboxActiveColor"):
        value_map['active_color'] = elm['properties'].get("checkboxActiveColor") or "ffffff"
        value_map['inactive_color'] = elm['properties'].get("checkboxInactiveColor") or "ffffff"

    if elm['properties'].get("ratingbarActiveColor"):
        value_map['active_color'] = elm['properties'].get("ratingbarActiveColor") or "ffffff"
        value_map['inactive_color'] = elm['properties'].get("ratingbarInactiveColor") or "ffffff"


    value_map['h_align'] = elm['properties'].get("horizontalAlign") or "center"
    value_map['v_align'] = elm['properties'].get("verticalAlign") or "center"
    value_map['text_align'] = elm['properties'].get("textAlign") or "center"
    value_map['title'] = elm['properties'].get("title") or "Sample Text!"

    value_map['width_margin_adjustment'] = int(value_map.get('width')) + int(value_map.get('margin_left')) + int(
        value_map.get('margin_right'))
    value_map['height_margin_adjustment'] = int(value_map.get('height')) + int(value_map.get('margin_top')) + int(
        value_map.get('margin_bottom'))

    value_map['min_value'] = elm['properties'].get("minValue") or "0"
    value_map['max_value'] = elm['properties'].get("maxValue") or "100"
    value_map['value'] = elm['properties'].get("value") or value_map['min_value']
    value_map['hint_text'] = elm['properties'].get("hintText") or "Enter"
    value_map['textfield_type'] = elm['properties'].get("type") or "text"

    # background image
    value_map['button_image'] = ''
    if elm['properties'].get("bgImage"):
        bg_image_url = elm['properties'].get("bgImage", {})["url"]
        bg_image = elm['properties'].get("bgImage", {})["name"]
        if bg_image.startswith('https'):
            a = urlparse(bg_image_url)
            bg_image = os.path.basename(a.path)

        if bg_image_url:
            file_name, _ = base.file_download(base.kivy_image_folder, bg_image_url, bg_image)
            value_map['button_image'] = f"background:'images/{bg_image}' "
            value_map['bg_color'] = "ffffff"

    # card-view
    if elm['componentTypeName'] == 'CardView':
        value_map['border_color'] = elm['properties'].get("border", {})["color"] or '#ffffff'
        if value_map['border_color'] == '#fff':
            value_map['border_color'] = '#ffffff'
        value_map['border_radius'] = elm['properties'].get("border", {})["radius"] or "0"
        value_map['border_size'] = elm['properties'].get("border", {})["size"] or "0"
        value_map['bg_color'] = elm['properties'].get("bgColor") or '#ffffff'
        if value_map['bg_color'] == '#fff':
            value_map['bg_color'] = '#ffffff'
    return value_map

