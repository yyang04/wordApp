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


class Config:
    def __init__(self, file_name='config'):
        self.file_name = file_name
        with open(file_name, 'r') as f:
            self.config = json.load(f)

    def get_config(self, key, default):
        return self.config.get(key, default)

    def set_config(self, key, value):
        self.config[key] = value
        with open(self.file_name, 'w') as f:
            json.dump(self.config, f)


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
        self.load_kv("pages/word.kv")
        self.load_kv("pages/home/home.kv")
        self.load_kv("pages/memo/memo.kv")
        self.load_kv("pages/vocab/vocab.kv")
        self.load_kv("pages/vocab/resc/resc.kv")
        self.load_kv("pages/vocab/item/item.kv")
        self.load_kv("pages/vocab/detail/detail.kv")

        # 初始化数据库, 配置文件, 记忆组件
        self.db = DataBase()
        self.conf = Config()
        self.memoQ = MemoryQueue(db=self.db, conf=self.conf)
        return MainScreen()


if __name__ == '__main__':
    app = WordApp()
    app.run()
