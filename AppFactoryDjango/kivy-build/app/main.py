

import webbrowser
from kivymd.uix.pickers import MDDatePicker
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.behaviors import ButtonBehavior
from kivy.core.window import Window
from kivy.lang import Builder
from base_strings.screen_1783_strings import *

from plyer import filechooser
import os
import time
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.menu import MDDropdownMenu
from kivy.uix.video import Video
os.environ["KIVY_VIDEO"] = "ffpyplayer"
from kivymd.uix.pickers import MDTimePicker
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.label import Label
from kivy.uix.modalview import ModalView
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivymd.app import MDApp
import base_strings
from kivymd.uix.bottomsheet import MDCustomBottomSheet
from kivy.factory import Factory
# Setting window size
window_size = Window.size
window_width = window_size[0]
window_height = window_size[1]


splash_screen = """ 
WindowManager:
    SplashScreen:
        name: "splash"
    Screen_1783:
        name: "screen_1783"
        
<SplashScreen>:
    FitImage:
        source:""
        """
#<<<new_tab_bar_marking>>>

class Screen_1783(Screen):
    def __init__(self, **kwargs):
        super(Screen_1783, self).__init__(**kwargs)
        #<<<new_tab_bar_marking>>>1783
        Screen1783 = Builder.load_string(screen_1783_string)
        self.add_widget(Screen1783)
        
        check_box_ = Builder.load_string(check_box__string)
        Screen1783.ids.id_1783.add_widget(check_box_)
        
        check_box_ = Builder.load_string(check_box__string)
        Screen1783.ids.id_1783.add_widget(check_box_)
        
        rating_bar_19 = Builder.load_string(rating_bar_19_string)
        Screen1783.ids.id_1783.add_widget(rating_bar_19)
        
        radio_button_10 = Builder.load_string(radio_button_10_string)
        Screen1783.ids.id_1783.add_widget(radio_button_10)
        
        radio_button_10 = Builder.load_string(radio_button_10_string)
        Screen1783.ids.id_1783.add_widget(radio_button_10)
        
        text_field_ = Builder.load_string(text_field__string)
        Screen1783.ids.id_1783.add_widget(text_field_)
        
        text_8831 = Builder.load_string(text_8831_string)
        Screen1783.ids.id_1783.add_widget(text_8831)
        #<<<adding_new_widgets>>>1783
        
        
        
        
        
        #<<<adding_actions_to_element>>>10
        
        #<<<adding_actions_to_element>>>10
        
        #<<<adding_actions_to_element>>>19
        # RATING BAR

        icon_color_inactive = '#9D96A5FF'
        icon_color_active = '#f5e342'
        rating_bar_19.ids.icon_two.text_color = icon_color_inactive
        rating_bar_19.ids.icon_three.text_color = icon_color_inactive
        rating_bar_19.ids.icon_four.text_color = icon_color_inactive
        rating_bar_19.ids.icon_five.text_color = icon_color_inactive
        rating_bar_19.ids.icon_one.text_color = icon_color_inactive
        
        def select_star1(instance):
            rating_bar_19.ids.icon_two.text_color = icon_color_inactive
            rating_bar_19.ids.icon_three.text_color = icon_color_inactive
            rating_bar_19.ids.icon_four.text_color = icon_color_inactive
            rating_bar_19.ids.icon_five.text_color = icon_color_inactive

            if rating_bar_19.ids.icon_one.icon == 'star-outline':
                rating_bar_19.ids.icon_one.icon = 'star-half-full'
                rating_bar_19.ids.icon_one.text_color = icon_color_active
            elif rating_bar_19.ids.icon_one.icon == 'star-half-full':
                rating_bar_19.ids.icon_one.text_color = icon_color_active
                rating_bar_19.ids.icon_one.icon = 'star'
                rating_bar_19.ids.icon_one.text_color = icon_color_active
            elif rating_bar_19.ids.icon_one.icon == 'star':
                rating_bar_19.ids.icon_one.text_color = icon_color_active
                rating_bar_19.ids.icon_one.icon = 'star-outline'
                rating_bar_19.ids.icon_one.text_color = icon_color_inactive
            rating_bar_19.ids.icon_two.icon = 'star-outline'
            rating_bar_19.ids.icon_three.icon = 'star-outline'
            rating_bar_19.ids.icon_four.icon = 'star-outline'
            rating_bar_19.ids.icon_five.icon = 'star-outline'

        def select_star2(instance):
            rating_bar_19.ids.icon_one.text_color = icon_color_active
            rating_bar_19.ids.icon_three.text_color = icon_color_inactive
            rating_bar_19.ids.icon_four.text_color = icon_color_inactive
            rating_bar_19.ids.icon_five.text_color = icon_color_inactive
            if rating_bar_19.ids.icon_two.icon == 'star-outline':
                rating_bar_19.ids.icon_two.text_color = icon_color_inactive
                rating_bar_19.ids.icon_two.icon = 'star-half-full'
                rating_bar_19.ids.icon_one.text_color = icon_color_active
                rating_bar_19.ids.icon_two.text_color = icon_color_active
            elif rating_bar_19.ids.icon_two.icon == 'star-half-full':
                rating_bar_19.ids.icon_one.text_color = icon_color_active
                rating_bar_19.ids.icon_two.text_color = icon_color_active
                rating_bar_19.ids.icon_two.icon = 'star'
                rating_bar_19.ids.icon_two.text_color = icon_color_active

            elif rating_bar_19.ids.icon_two.icon == 'star':
                rating_bar_19.ids.icon_one.text_color = icon_color_active
                rating_bar_19.ids.icon_two.text_color = icon_color_active
                rating_bar_19.ids.icon_two.icon = 'star-outline'
                rating_bar_19.ids.icon_two.text_color = icon_color_inactive
            rating_bar_19.ids.icon_one.icon = 'star'
            rating_bar_19.ids.icon_three.icon = 'star-outline'
            rating_bar_19.ids.icon_four.icon = 'star-outline'
            rating_bar_19.ids.icon_five.icon = 'star-outline'

        def select_star3(instance):
            rating_bar_19.ids.icon_four.text_color = icon_color_inactive
            rating_bar_19.ids.icon_five.text_color = icon_color_inactive
            rating_bar_19.ids.icon_one.text_color = icon_color_active
            rating_bar_19.ids.icon_two.text_color = icon_color_active
            if rating_bar_19.ids.icon_three.icon == 'star-outline':
                rating_bar_19.ids.icon_three.text_color = icon_color_inactive
                rating_bar_19.ids.icon_three.icon = 'star-half-full'
                rating_bar_19.ids.icon_three.text_color = icon_color_active
            elif rating_bar_19.ids.icon_three.icon == 'star-half-full':
                rating_bar_19.ids.icon_three.icon = 'star'
                rating_bar_19.ids.icon_three.text_color = icon_color_active
            elif rating_bar_19.ids.icon_three.icon == 'star':
                rating_bar_19.ids.icon_three.icon = 'star-outline'
                rating_bar_19.ids.icon_three.text_color = icon_color_inactive
            rating_bar_19.ids.icon_one.icon = 'star'
            rating_bar_19.ids.icon_two.icon = 'star'
            rating_bar_19.ids.icon_four.icon = 'star-outline'
            rating_bar_19.ids.icon_five.icon = 'star-outline'

        def select_star4(instance):
            rating_bar_19.ids.icon_five.text_color = icon_color_inactive
            rating_bar_19.ids.icon_three.text_color = icon_color_active
            rating_bar_19.ids.icon_one.text_color = icon_color_active
            rating_bar_19.ids.icon_two.text_color = icon_color_active
            if rating_bar_19.ids.icon_four.icon == 'star-outline':
                rating_bar_19.ids.icon_four.icon = 'star-half-full'
                rating_bar_19.ids.icon_four.text_color = icon_color_active
            elif rating_bar_19.ids.icon_four.icon == 'star-half-full':
                rating_bar_19.ids.icon_four.icon = 'star'
                rating_bar_19.ids.icon_four.text_color = icon_color_active
            elif rating_bar_19.ids.icon_four.icon == 'star':
                rating_bar_19.ids.icon_four.icon = 'star-outline'
                rating_bar_19.ids.icon_four.text_color = icon_color_inactive
            rating_bar_19.ids.icon_one.icon = 'star'
            rating_bar_19.ids.icon_two.icon = 'star'
            rating_bar_19.ids.icon_three.icon = 'star'
            rating_bar_19.ids.icon_five.icon = 'star-outline'

        def select_star5(instance):
            rating_bar_19.ids.icon_four.text_color = icon_color_active
            rating_bar_19.ids.icon_three.text_color = icon_color_active
            rating_bar_19.ids.icon_one.text_color = icon_color_active
            rating_bar_19.ids.icon_two.text_color = icon_color_active
            if rating_bar_19.ids.icon_five.icon == 'star-outline':
                rating_bar_19.ids.icon_five.icon = 'star-half-full'
                rating_bar_19.ids.icon_five.text_color = icon_color_active
            elif rating_bar_19.ids.icon_five.icon == 'star-half-full':
                rating_bar_19.ids.icon_five.icon = 'star'
                rating_bar_19.ids.icon_five.text_color = icon_color_active
            elif rating_bar_19.ids.icon_five.icon == 'star':
                rating_bar_19.ids.icon_five.icon = 'star-outline'
                rating_bar_19.ids.icon_five.text_color = icon_color_inactive
            rating_bar_19.ids.icon_one.icon = 'star'
            rating_bar_19.ids.icon_two.icon = 'star'
            rating_bar_19.ids.icon_three.icon = 'star'
            rating_bar_19.ids.icon_four.icon = 'star'

        rating_bar_19.ids.icon_one.bind(on_press=select_star1)
        rating_bar_19.ids.icon_two.bind(on_press=select_star2)
        rating_bar_19.ids.icon_three.bind(on_press=select_star3)
        rating_bar_19.ids.icon_four.bind(on_press=select_star4)
        rating_bar_19.ids.icon_five.bind(on_press=select_star5)

        
        #<<<adding_actions_to_element>>>
        
        #<<<adding_actions_to_element>>>
        #<<<adding_actions_to_element>>>1783
    
        # -----------------------------END OF SCREEN----------------------------- #


class SplashScreen(Screen):
    pass
    
class Videos(Video):
    pass
    
class ContentNavigationDrawer(MDBoxLayout):
    pass

class Shadow(RoundedRectangularElevationBehavior, MDBoxLayout):
    pass

class ClickableBoxLayout(ButtonBehavior, MDBoxLayout):
    pass


class WindowManager(ScreenManager):
    pass

class ScreenApp(MDApp):
    window_size = Window.size
    window_width = window_size[0]
    window_height = window_size[1]
    def build(self):
        self.icon = ''
        self.window_manager=Builder.load_string(splash_screen)
        Clock.schedule_once(self.go_to_home,3)
        return self.window_manager

    def go_to_home(self, *args):
        screen_manager = ScreenManager()
        self.window_manager.current = 'screen_1783'
        screen_manager.add_widget(Screen_1783(name="screen_1783",size_hint=(None, None),size=(window_width, window_height)))
        
        return screen_manager

    

# run the app
ScreenApp().run()
