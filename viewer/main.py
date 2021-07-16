from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window

KV = '''
#:import KivyLexer kivy.extras.highlight.KivyLexer
#:import HotReloadViewer kivymd.utils.hot_reload_viewer.HotReloadViewer

Screen:
    BoxLayout:
        BoxLayout:
            orientation: "vertical"
            size_hint_x: .7
            CodeInput:
                id: code
                lexer: KivyLexer()
                style_name: "native"
                size_hint_y: 0.9
            # Button:
            #     text: "Reload"
            #     on_release: app.update_kv_file(code.text)
            #     size_hint_y: 0.1

        HotReloadViewer:
            size_hint_x: .3
            path: app.path_to_kv_file
            errors: True
            errors_text_color: 1, 1, 0, 1
            errors_background_color: app.theme_cls.bg_dark
'''

class Example(MDApp):

    def __init__(self, **kwargs):
        super(Example, self).__init__(**kwargs)
        self.path_to_kv_file = "viewer/main.kv"
        Window.bind(on_key_down=self._on_keyboard_down)

    def _on_keyboard_down(self, *args):
        if args[3]=='s' and args[4][1]=='ctrl':
            self.update_kv_file(self.screen.ids.code.text)
    
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.screen = Builder.load_string(KV)
        with open(self.path_to_kv_file, "r") as kv_file:
            self.screen.ids.code.text = kv_file.read()
        return self.screen

    def update_kv_file(self, text):
        with open(self.path_to_kv_file, "w") as kv_file:
            kv_file.write(text)

Example().run()