from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.bottomsheet import MDCustomBottomSheet

from kivy.lang import Builder
from kivy.core.window import Window
from kivy.factory import Factory
Window.size = (500, 750)
Window.left, Window.top = 1350, -900


Builder.load_file('kvs/widgets/check.kv')
Builder.load_file('kvs/widgets/content_custom_sheet.kv')
Builder.load_file('kvs/widgets/element_card.kv')
Builder.load_file('kvs/widgets/tab_card.kv')


class MainApp(MDApp):

    def build(self):
        self.title = 'KivyMD Online Shop'
        self.theme_cls.primary_palette = 'Teal'
        self.sm = ScreenManager()
        screens = [
            Factory.MainScreen(name='main')
        ]
        for screen in screens:
            self.sm.add_widget(screen)

        return self.sm

    def show_custom_bottom_sheet(self, image, price, rate):
        bottom_sheet = Factory.ContentCustomSheet()
        bottom_sheet.rate = rate
        bottom_sheet.image = image
        bottom_sheet.price = price
        self.custom_sheet = MDCustomBottomSheet(screen=bottom_sheet)
        self.custom_sheet.open()


if __name__ == '__main__':
    MainApp().run()