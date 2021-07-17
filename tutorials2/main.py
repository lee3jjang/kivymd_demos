from kivystudio import KivyStudio
from kivymd.uix.screen import MDScreen
from kivy.metrics import dp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.snackbar import Snackbar

class MainScreen(MDScreen):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        items = [
            {
                "viewclass": "OneLineListItem",
                "text": f"Item {i}",
                "height": dp(56),
                "on_release": lambda x=f"Item {i}": self.menu_callback(x)
            } for i in range(5)
        ]
        self.menu = MDDropdownMenu(items=items, width_mult=4)

    def callback(self, button):
        self.menu.caller = button
        self.menu.open()

    def menu_callback(self, text):
        self.menu.dismiss()
        Snackbar(text=text).open()

if __name__ == '__main__':
    studio = KivyStudio('tutorials2/main.kv')
    studio.run()
