from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.bottomnavigation import MDBottomNavigation
from kivy.core.text import LabelBase
from pages.home.home import Home
from pages.memo.memo import Memo
from pages.vocab.vocab import Vocab


class MainScreen(MDBottomNavigation):
    use_text = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.add_widget(Memo())
        self.add_widget(Vocab())
        self.add_widget(Home())


class Word(MDApp):
    def build(self):

        self.theme_cls.material_style = "M3"  # M1/M5
        self.theme_cls.theme_style = "Dark"   # Light
        self.theme_cls.primary_palette = "Red"
        Window.size = (450, 900)

        # 注册字体
        LabelBase.register(name='Heiti', fn_regular='font/STHeiti Medium.ttc')
        # kv
        self.load_kv("main.kv")
        self.load_kv("pages/home/home.kv")
        self.load_kv("pages/memo/memo.kv")
        self.load_kv("pages/vocab/vocab.kv")

        return MainScreen()


if __name__ == '__main__':
    app = Word()
    app.run()
