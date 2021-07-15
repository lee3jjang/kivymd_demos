from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.list import OneLineIconListItem, MDList
from kivymd.theming import ThemableBehavior

from kivy.properties import StringProperty
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.factory import Factory
from kivy.network.urlrequest import UrlRequest

import numpy as np
import matplotlib.pyplot as plt

# Window.size = (500, 750)
# Window.left, Window.top = 1350, -900

class MainApp(MDApp):

    def get_data(self):
        req = UrlRequest('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
        req.wait()
        city_air = req.result
        #result = city_air['RealtimeCityAir']['row'][0]['MSRDT']
        x = np.linspace(0, 1, 100)
        y = np.sin(x)
        plt.plot(x, y)
        plt.savefig('test.png')
        self.root.ids.img.source = 'test.png'

        # result = str(np.array([4, 2]).sum())
        # self.root.ids.display.text = result
    
    def build(self):

        return Factory.MainScreen()


if __name__ == '__main__':
    MainApp().run()
