from kivymd.app import MDApp
from kivymd.uix.bottomnavigation import MDBottomNavigationItem
from kivymd.uix.label import MDLabel


class Progress(MDLabel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.font_name = 'Heiti'
        self.theme_text_color = "Custom"


class Home(MDBottomNavigationItem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = MDApp.get_running_app()

    def init_memo(self):
        self.app.db.init_memo()
        self.app.memoQ.refresh()
        self.on_enter()

    def init_task(self):
        self.app.db.init_task()
        self.app.memoQ.refresh()
        self.on_enter()

    def on_enter(self, *args):
        total, exposed, know, memorized = self.app.db.get_progress()
        total = 0 if not total else total
        exposed = 0 if not exposed else exposed
        know = 0 if not know else know
        memorized = 0 if not memorized else memorized

        self.ids.progress.clear_widgets()
        self.ids.progress.add_widget(Progress(text=f"全部词汇:\n{total}", text_color='white'))
        self.ids.progress.add_widget(Progress(text=f"学习词汇:\n{exposed}", text_color='red'))
        self.ids.progress.add_widget(Progress(text=f"认识词汇:\n{know}", text_color='yellow'))
        self.ids.progress.add_widget(Progress(text=f"记住词汇:\n{memorized}", text_color='green'))

