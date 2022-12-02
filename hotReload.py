from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp

Window.size = (350, 600)

kv = """
BoxLayout:
    HotReloadViewer:
        path: app.path_to_kv_file
        errors:True
        errors_text_color: 1,1,0,1
        errors_background_color: app.theme_cls.bg_dark
"""


class TourCeylon(MDApp):
    path_to_kv_file = "mainscreen.kv"

    def build(self):
        return Builder.load_string(kv)


TourCeylon().run()