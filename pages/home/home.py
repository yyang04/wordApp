from kivymd.app import MDApp
from kivymd.uix.bottomnavigation import MDBottomNavigationItem


class Home(MDBottomNavigationItem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = MDApp.get_running_app()

    def init_memo(self):
        self.app.db.init_memo()

    def init_task(self):
        self.app.db.init_task()
