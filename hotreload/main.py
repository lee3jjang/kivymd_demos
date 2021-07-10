from kaki.app import App
from kivymd.app import MDApp

from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.factory import Factory
Window.size = (500, 750)
Window.left, Window.top = 1350, -900

class MDLive(App, MDApp):

    CLASSES = {
        'ScreenUI': "liveapp.screen_ui",
    }

    AUTORELOADER_PATHS = [
        (".", {"recursive": True})
    ]

    def build_app(self, *args):
        print("Inside Build App Auto Reload 2")
        return Factory.ScreenUI()

    

if __name__ == '__main__':
    MDLive().run()