from kivystudio import KivyStudio
from kivymd.uix.screen import MDScreen
from pathlib import Path
from kivymd.app import MDApp
from kivy.clock import Clock
from kivy.lang import Builder
import os
from kivymd.toast import toast


class MainScreen(MDScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)



class MyApp(MDApp):

    def build(self):
        Builder.load_file('main.kv')
        return MainScreen()

if __name__ == '__main__':
    # MyApp().run()
    studio = KivyStudio(str(Path(os.path.dirname(__file__)) / 'main.kv'))
    studio.run()
