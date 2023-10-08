from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivymd.uix.bottomnavigation import MDBottomNavigationItem
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.chip import MDChip
from kivymd.uix.label import MDLabel
from kivymd.uix.scrollview import MDScrollView


class MyChip(MDChip):
    icon_check_color = (0, 0, 0, 1)
    text_color = (0, 0, 0, 0.5)
    _no_ripple_effect = True

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class Divider(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class PosLabel(MDLabel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.font_name = 'Heiti'


class DefLabel(MDLabel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.font_name = 'Heiti'


class SenLabel(MDLabel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.font_name = 'Heiti'


class Memo(MDBottomNavigationItem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bg = self.ids.bg
        self.hint = self.ids.hint
        self.scroll = self.ids.scroll
        self.answer = self.ids.answer
        self.memoButton = self.ids.memoButton
        self.app = MDApp.get_running_app()

        self.bg.remove_widget(self.memoButton)
        self.bg.remove_widget(self.scroll)

    def show_definitions(self, touch, w):
        if self.collide_point(*touch.pos):
            self.bg.remove_widget(self.hint)
            self.bg.add_widget(self.scroll)
            self.bg.add_widget(self.memoButton)
            self.ids.answer.clear_widgets()

            word = self.app.get_word(w)
            if word:
                for definition in word.definitions:
                    posLabel = PosLabel(text=definition.pos)
                    self.ids.answer.add_widget(posLabel)

                    defLabel = DefLabel(text=definition.definition)
                    self.ids.answer.add_widget(defLabel)

                    for sentence in definition.sentences:
                        senLabel = SenLabel(text=sentence.sentence)
                        self.ids.answer.add_widget(senLabel)

    def next_word(self):
        self.bg.add_widget(self.hint)
        self.bg.remove_widget(self.scroll)
        self.bg.remove_widget(self.memoButton)











