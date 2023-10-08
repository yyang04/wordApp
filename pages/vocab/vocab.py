from kivymd.uix.bottomnavigation import MDBottomNavigationItem
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager

from pages.detail.detail import Detail
from pages.items.items import Items


class Resource(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Vocab(MDBottomNavigationItem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        sm = MDScreenManager()
        sm.add_widget(Resource())

        # screens = {
        #     'resource': Resource,
        #     'items': Items,
        #     'detail': Detail
        # }
        #
        # for name, page in screens.items():
        #     screen = page(name=name)
        #     sm.add_widget(screen)
        #
        # sm.current = 'resource'
