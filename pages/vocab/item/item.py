from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem, IRightBody, OneLineRightIconListItem
from kivymd.uix.label import MDLabel
from kivy.properties import StringProperty
from kivymd.uix.list import OneLineListItem
from kivymd.uix.screen import MDScreen


class ListItemWithTwoText(OneLineRightIconListItem):
    rtext = StringProperty()

    def on_release(self):
        sm = self.parent.parent.parent.parent.parent
        sm.transition.direction = 'left'
        sm.current = 'detail'
        sm.get_screen('detail').init_data(self.text)


class RightText(IRightBody, MDLabel):
    """"""


class Item(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def init_data(self, data):
        self.ids.rv.data = data

    def go_previous(self):
        sm = self.parent
        sm.transition.direction = 'right'
        sm.current = sm.previous()

