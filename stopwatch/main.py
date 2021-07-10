from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.bottomsheet import MDCustomBottomSheet

from kivy.lang import Builder
from kivy.core.window import Window
from kivy.factory import Factory
Window.size = (500, 750)
Window.left, Window.top = 1350, -900

class MainApp(MDApp):

    def build(self):
        self.title = 'KivyMD StopWatch'
        self.theme_cls.primary_palette = 'Teal'
        self.sm = ScreenManager()
        screens = [
            Factory.MainScreen(name='main')
        ]
        for screen in screens:
            self.sm.add_widget(screen)

        return self.sm

if __name__ == '__main__':
    MainApp().run()