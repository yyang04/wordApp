from kivy.uix.widget import Widget
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

        self.bg.remove_widget(self.memoButton)
        self.bg.remove_widget(self.scroll)

    def show_definitions(self, touch):
        if self.collide_point(*touch.pos):
            self.bg.remove_widget(self.hint)
            self.bg.add_widget(self.scroll)
            self.bg.add_widget(self.memoButton)
            self.ids.answer.clear_widgets()

            posLabel = PosLabel(text='v. t.')
            self.ids.answer.add_widget(posLabel)

            defLabel = DefLabel(text='夸奖， 赞扬； 吹嘘：')
            self.ids.answer.add_widget(defLabel)

            senLabel = SenLabel(text='On nous avait beaucoup vanté ce médecin. 人们向我们大大夸奖了这位医生。')
            self.ids.answer.add_widget(senLabel)

            senLabel = SenLabel(text='vanter sa marchandise 夸自己的货色')
            self.ids.answer.add_widget(senLabel)

            self.ids.answer.add_widget(Divider())

            posLabel = PosLabel(text='se vanter v. pr.')
            self.ids.answer.add_widget(posLabel)

            defLabel = DefLabel(text='1. 自吹自擂， 吹牛')
            self.ids.answer.add_widget(defLabel)

            defLabel = DefLabel(text='2. se vanter de 夸耀， 吹嘘， 以…自豪：')
            self.ids.answer.add_widget(defLabel)

            senLabel = SenLabel(text="Il n'y a pas de quoi se vanter. 这没什么可吹的。")
            self.ids.answer.add_widget(senLabel)

            senLabel = SenLabel(text="Et je m'en vante ! 我还感到自豪呢！")
            self.ids.answer.add_widget(senLabel)

            senLabel = SenLabel(text="Il se vante de réussir. 他夸口说定能够功。")
            self.ids.answer.add_widget(senLabel)

    def next_word(self):
        self.bg.add_widget(self.hint)
        self.bg.remove_widget(self.scroll)
        self.bg.remove_widget(self.memoButton)











