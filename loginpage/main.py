from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager

from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.factory import Factory
Window.size = (500, 750)
Window.left, Window.top = 1350, -900


Builder.load_file('main.kv')


class LoginPage(MDApp):

    def build(self):
        self.title = 'KivyMD Login Page'
        self.theme_cls.primary_palette = 'Teal'
        self.sm = ScreenManager()
        screens = [
            Factory.MainScreen(name='main')
        ]
        for screen in screens:
            self.sm.add_widget(screen)

        return self.sm

if __name__ == '__main__':
    LoginPage().run()