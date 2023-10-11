from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivymd.color_definitions import colors
from kivymd.uix.bottomnavigation import MDBottomNavigationItem
from kivymd.uix.chip import MDChip
from kivymd.uix.label import MDLabel

from utils.memory import Action


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


class FreqLabel(MDLabel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.font_name = 'Heiti'
        self.font_size = 25
        self.color = colors['Blue']["800"]
        self.size_hint_y = None
        self.height = self.texture_size[1] + 10
        self.halign = "left"


class Memo(MDBottomNavigationItem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bg = self.ids.bg
        self.hint = self.ids.hint
        self.scroll = self.ids.scroll
        self.answer = self.ids.answer
        self.memoButton = self.ids.memoButton
        self.word = self.ids.word
        self.freq = self.ids.freq
        self.app = MDApp.get_running_app()
        self.init_screen()

    def on_enter(self, *args):
        self.app.memoQ.refresh()
        self.init_screen()

    def show_definitions(self, touch):
        w = self.ids.word.text
        if self.collide_point(*touch.pos):
            self.bg.remove_widget(self.hint)
            self.bg.add_widget(self.scroll)
            self.bg.add_widget(self.memoButton)
            self.ids.answer.clear_widgets()

            word = self.app.db.get_def(w)
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

    def next_word(self, action: Action):
        if self.memo_word:
            self.app.memoQ.modify_memory(self.memo_word, action)
            self.bg.add_widget(self.hint)
            self.init_screen()

    def init_screen(self):
        self.bg.remove_widget(self.memoButton)
        self.bg.remove_widget(self.scroll)
        self.bg.remove_widget(self.word)
        self.bg.remove_widget(self.hint)
        self.bg.remove_widget(self.freq)
        self.ids.freq.clear_widgets()
        self.memo_word = self.app.memoQ.pop_memory()
        if self.memo_word:
            self.bg.add_widget(self.word)
            self.bg.add_widget(self.freq)
            rescFreq = self.app.db.get_freq(self.memo_word.word)
            for resc, freq in rescFreq:
                freqLabel = FreqLabel(text=f'在 {resc} 中出现 {freq} 次')
                self.ids.freq.add_widget(freqLabel)
            self.bg.add_widget(self.hint)
            self.ids.word.text = self.memo_word.word













