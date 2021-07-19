from kivystudio import KivyStudio
from kivymd.uix.screen import MDScreen
from pathlib import Path
from kivymd.app import MDApp
from kivy.clock import Clock
from kivy.lang import Builder
import os
import pytube
from kivymd.toast import toast


class MainScreen(MDScreen):

    image_loaded = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def set_assets(self, thumbnail, title):
        self.ids.thumbnail.source = thumbnail
        self.ids.title.text = title

    def download_video(self, url):
        yt = pytube.YouTube(url)
        self.set_assets(yt.thumbnail_url, yt.title)
        self.image_loaded = True
        Clock.schedule_once(lambda x: self.get_video(yt.streams.first()), 4)

    def get_video(self, stream):
        if self.image_loaded == True:
            stream.download()
        toast("Video is downloading...")


class MyApp(MDApp):

    def build(self):
        Builder.load_file('main.kv')
        return MainScreen()

if __name__ == '__main__':
    MyApp().run()
    # studio = KivyStudio(str(Path(os.path.dirname(__file__)) / 'main.kv'))
    # studio.run()
