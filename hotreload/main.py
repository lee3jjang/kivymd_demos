from kivy.lang import Builder
from kivymd.app import MDApp
from datetime import datetime
from kivy.factory import Factory

KV = '''
#:import KivyLexer kivy.extras.highlight.KivyLexer
#:import HotReloadViewer kivymd.utils.hot_reload_viewer.HotReloadViewer

BoxLayout:

    CodeInput:
        lexer: KivyLexer()
        style_name: "native"
        on_text: app.update_kv_file(self.text)
        size_hint_x: .6

    HotReloadViewer:
        size_hint_x: .4
        path: app.path_to_kv_file
        errors: True
        errors_text_color: 1, 1, 0, 1
        errors_background_color: app.theme_cls.bg_dark
'''

class Example(MDApp):
    now = datetime.now().strftime('%Y%m%d%H%M%S')
    path_to_kv_file = f"hotreload/main_{now}.kv"

    def build(self):
        self.theme_cls.theme_style = "Dark"
        # return Builder.load_string(KV)
        # Builder.load_file('main.kv')
        return Factory.MainScreen()

    def update_kv_file(self, text):
        with open(self.path_to_kv_file, "w") as kv_file:
            kv_file.write(text)


Example().run()