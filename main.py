from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.bottomnavigation import MDBottomNavigation
from kivy.core.text import LabelBase
from pages.home.home import Home
from pages.memo.memo import Memo
from pages.vocab.vocab import Vocab
from utils.database import DataBase
from utils.memory import MemoryQueue
import json



class MainScreen(MDBottomNavigation):
    use_text = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.add_widget(Memo())
        self.add_widget(Vocab())
        self.add_widget(Home())


class WordApp(MDApp):
    def build(self):

        self.theme_cls.material_style = "M3"  # M1/M5
        self.theme_cls.theme_style = "Dark"   # Light
        self.theme_cls.primary_palette = "Red"
        Window.size = (450, 900)

        # 初始化字体
        LabelBase.register(name='Heiti', fn_regular='font/STHeiti Medium.ttc')

        # 初始化kv
        self.load_kv("pages/home/home.kv")
        self.load_kv("pages/memo/memo.kv")
        self.load_kv("pages/vocab/vocab.kv")
        self.load_kv("pages/vocab/resc/resc.kv")
        self.load_kv("pages/vocab/item/item.kv")
        self.load_kv("pages/vocab/detail/detail.kv")

        # 初始化数据库
        self.db = DataBase()

        # 初始化记忆组件
        self.memoQ = MemoryQueue()
        return MainScreen()


if __name__ == '__main__':
    app = WordApp()
    app.run()
