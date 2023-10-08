from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem, IRightBody, OneLineRightIconListItem
from kivymd.uix.label import MDLabel
from kivy.properties import StringProperty
from kivymd.uix.list import OneLineListItem
from kivymd.uix.screen import MDScreen


class ListItemWithTwoText(OneLineRightIconListItem):
    rtext = StringProperty()


class RightText(IRightBody, MDLabel):
    """"""


class Item(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def init_data(self, data):
        self.ids.rv.data = data
