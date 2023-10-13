from kivy.core.text import LabelBase
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.color_definitions import colors

KV = '''
MDFloatLayout:
    CustomLabel:
        theme_text_color: "Custom"
        text_color: 1, 0, 0, 1
        text: "●"
        font_size: "48sp"
'''


class CustomLabel(MDLabel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.font_name = 'Heiti'


class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Red"  # 设置主题颜色为红色
        LabelBase.register(name='Heiti', fn_regular='font/STHeiti Medium.ttc')
        return Builder.load_string(KV)

MainApp().run()
