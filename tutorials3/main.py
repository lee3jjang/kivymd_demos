from kivystudio import KivyStudio
from kivymd.uix.screen import MDScreen
from kivy.metrics import dp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.snackbar import Snackbar

class MainScreen(MDScreen):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

if __name__ == '__main__':
    studio = KivyStudio('tutorials3/main.kv')
    studio.run()
