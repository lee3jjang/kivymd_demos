from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDFlatButton

class ScreenUI(Screen):

    def __init__(self):
        super().__init__()
        button = MDFlatButton(
            text="Nice To Meet You",
            pos_hint={"center_x": .5, "center_y": .5}
        )
        self.add_widget(button)