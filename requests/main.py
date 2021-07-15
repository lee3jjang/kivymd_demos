from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.list import OneLineIconListItem, MDList
from kivymd.theming import ThemableBehavior

from kivy.properties import StringProperty
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.factory import Factory

import requests

# Window.size = (500, 750)
# Window.left, Window.top = 1350, -900

class MainApp(MDApp):

    def get_data(self):
        response_data = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
        city_air = response_data.json()
        result = city_air['RealtimeCityAir']['row'][0]['MSRSTE_NM']
        self.root.ids.display.text = result
    
    def build(self):

        return Factory.MainScreen()


if __name__ == '__main__':
    MainApp().run()