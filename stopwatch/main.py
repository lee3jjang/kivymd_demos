from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.bottomsheet import MDCustomBottomSheet

from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.factory import Factory
Window.size = (500, 750)
Window.left, Window.top = 1350, -900

class MainApp(MDApp):
    started = False
    seconds = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.update_time, 0)
    
    def update_time(self, obj):
        if self.started:
            self.seconds += obj
        minutes, seconds = divmod(self.seconds, 60)
        part_seconds = seconds*100 % 100
        self.sm.screens[0].ids.stopwatch.text = f'[size=45]{int(minutes):02}[/size][size=30]:[/size][size=60]{int(seconds):02}[/size][size=30].[/size][size=30]{int(part_seconds):02}[/size]'

    def start_stop(self):
        self.sm.screens[0].ids.start_stop.text = 'START' if self.started else 'STOP'
        self.started = not self.started
        self.sm.screens[0].ids.reset.disabled = True if self.started else False

    def reset(self):
        if self.started:
            self.started = False
        self.seconds = 0

    def build(self):
        self.title = 'KivyMD StopWatch'
        self.theme_cls.primary_palette = 'Teal'
        self.sm = ScreenManager()
        screens = [
            Factory.MainScreen(name='main')
        ]
        for screen in screens:
            self.sm.add_widget(screen)

        return self.sm

if __name__ == '__main__':
    MainApp().run()