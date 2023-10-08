from kivymd.uix.bottomnavigation import MDBottomNavigationItem

from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen

from pages.vocab.resc.resc import Resc
from pages.vocab.item.item import Item
from pages.vocab.detail.detail import Detail


class Vocab(MDBottomNavigationItem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.sm = MDScreenManager()

        screens = {'resc': Resc,
                   'item': Item,
                   'detail': Detail}

        for name, page in screens.items():
            self.sm.add_widget(page(name=name))

        self.add_widget(self.sm)
