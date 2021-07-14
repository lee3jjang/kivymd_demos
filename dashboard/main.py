from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.list import OneLineIconListItem, MDList
from kivymd.theming import ThemableBehavior
from kivy.properties import StringProperty
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.factory import Factory
Window.size = (500, 750)
Window.left, Window.top = 50, 50

# Builder.load_file('main.kv')

class MainApp(MDApp):
    
    def build(self):
        
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"

        return Factory.MainScreen()


if __name__ == '__main__':
    MainApp().run()