
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen


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


class Detail(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = MDApp.get_running_app()

    def init_data(self, w):
        self.ids.answer.clear_widgets()
        word = self.app.db.get_def(w)
        self.ids.word.text = word.word
        if word:
            for definition in word.definitions:
                posLabel = PosLabel(text=definition.pos)
                self.ids.answer.add_widget(posLabel)

                defLabel = DefLabel(text=definition.definition)
                self.ids.answer.add_widget(defLabel)

                for sentence in definition.sentences:
                    senLabel = SenLabel(text=sentence.sentence)
                    self.ids.answer.add_widget(senLabel)

                self.ids.answer.add_widget(MDLabel(text=""))

    def to_previous(self):
        sm = self.parent
        sm.transition.direction = 'right'
        sm.current = sm.previous()
