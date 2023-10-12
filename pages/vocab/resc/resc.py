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
        self.app = MDApp.get_running_app()
        resc = self.app.db.get_resc()

        if resc:
            for name, count in resc:
                item = CustomTwoLineIconListItem(text=name, secondary_text=f'Count: {count}')
                item.ids.plus.bind(on_release=lambda x: self.icon_plus(name))
                item.bind(on_release=lambda x: self.to_item(self.app.db.get_item(name)))
                self.ids.resc.add_widget(item)

    def to_item(self, data):
        sm = self.parent
        sm.transition.direction = 'left'
        sm.current = 'item'
        sm.get_screen('item').init_data(data)

    def icon_plus(self, name):
        self.app.db.add_memo(name)
        self.app.refresh = True

