from kivy.properties import StringProperty
from kivymd.uix.label import MDLabel
from kivymd.uix.list import IRightBody, OneLineRightIconListItem
from kivymd.uix.screen import MDScreen


class ListItemWithTwoText(OneLineRightIconListItem):
    rtext = StringProperty()


class RightText(IRightBody, MDLabel):
    pass


class Item(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def init_data(self, data):
        self.ids.rv.data = data

    def to_previous(self):
        sm = self.parent
        sm.transition.direction = 'right'
        sm.current = sm.previous()

    def to_detail(self, text):
        sm = self.parent
        sm.transition.direction = 'left'
        sm.current = 'detail'
        sm.get_screen('detail').init_data(text)
