from kivy.properties import StringProperty
from kivymd.uix.label import MDLabel
from kivymd.uix.list import IRightBody, OneLineAvatarIconListItem, ILeftBody
from kivymd.uix.screen import MDScreen


class ListItemWithTwoText(OneLineAvatarIconListItem):
    rtext = StringProperty()
    lcolor = StringProperty(defaultvalue="Green")
    lhue = StringProperty(defaultvalue="500")


class RightText(IRightBody, MDLabel):
    pass


class LeftColor(ILeftBody, MDLabel):
    pass


class Item(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def init_data(self, data):
        words = [{'text': word,
                  'rtext': f"{freq}",
                  **self.calculate_progress(is_exposed, is_memorized, score)
                  } for word, freq, is_exposed, is_memorized, score in data]
        self.ids.rv.data = words

    def calculate_progress(self, is_exposed, is_memorized, score):
        if not is_exposed:
            return {"lcolor": "Red", "lhue": "500"}
        if is_memorized:
            return {"lcolor": "Green", "lhue": "700"}
        if score >= 150:
            return {"lcolor": "Green", "lhue": "200"}
        elif score < 150:
            return {"lcolor": "Yellow", "lhue": "500"}


    def to_previous(self):
        sm = self.parent
        sm.transition.direction = 'right'
        sm.current = sm.previous()

    def to_detail(self, text):
        sm = self.parent
        sm.transition.direction = 'left'
        sm.current = 'detail'
        sm.get_screen('detail').init_data(text)
