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
Window.left, Window.top = 1350, -900


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color

class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()

class MainApp(MDApp):
    
    def build(self):
        return Factory.MainScreen()

    def on_start(self):
        icons_item = {
            "folder": "My files",
            "account-multiple": "Shared with me",
            "star": "Starred",
            "history": "Recent",
            "checkbox-marked": "Shared with me",
            "upload": "Upload",
        }
        for icon, text in icons_item.items():
            self.root.ids.nav_drawer.children[0].ids.md_list.add_widget(
                ItemDrawer(icon=icon, text=text)
            )


if __name__ == '__main__':
    MainApp().run()