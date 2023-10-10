from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.button import MDIconButton
from kivymd.uix.list import TwoLineAvatarIconListItem, IRightBody
from kivymd.uix.screen import MDScreen


class CustomTwoLineIconListItem(TwoLineAvatarIconListItem):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class RightPlus(IRightBody, MDIconButton):
    icon = 'plus'


class Resc(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        app = MDApp.get_running_app()
        resc = app.db.get_resc()
        self.sm = self.parent

        if resc:
            for name, count in resc:
                item = CustomTwoLineIconListItem(text=name, secondary_text=f'Count: {count}')
                item.ids.plus.bind(on_release=lambda x: app.db.add_memo(name))
                item.bind(on_release=lambda x: self.to_item(app.db.get_item(name)))
                self.ids.resc.add_widget(item)

    def to_item(self, data):
        self.sm.transition.direction = 'left'
        self.sm.current = 'item'
        self.sm.get_screen('item').init_data(data)
