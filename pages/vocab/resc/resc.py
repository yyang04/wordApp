from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import TwoLineIconListItem
from kivymd.uix.screen import MDScreen


class CTwoLineIconListItem(TwoLineIconListItem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Resc(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        app = MDApp.get_running_app()
        resc = app.db.get_resc()
        if resc:
            for name, count in resc:
                item = CTwoLineIconListItem(text=name, secondary_text=f'Count: {count}')

                item.bind(on_release=lambda x: self.to_item(self.parent, app.db.get_item(name)))
                self.ids.resc.add_widget(item)

    def to_item(self, sm, data):
        sm.transition.direction = 'left'
        sm.current = 'item'
        sm.get_screen('item').init_data(data)
