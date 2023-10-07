from kivy.uix.widget import Widget
from kivymd.uix.bottomnavigation import MDBottomNavigationItem
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.scrollview import MDScrollView


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


class MemoButtons(MDBoxLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Answer(MDScrollView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Memo(MDBottomNavigationItem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def show_definitions(self, touch):
        if self.collide_point(*touch.pos):
            hint = self.ids.hint
            self.ids.cadre.remove_widget(hint)
            self.ids.cadre.add_widget(Answer())

            self.ids.box
            # defLabel = DefLabel(text='夸奖， 赞扬； 吹嘘：')
            # senLabel1 = SenLabel(text='On nous avait beaucoup vanté ce médecin. 人们向我们大大夸奖了这位医生。')
            # senLabel2 = SenLabel(text='vanter sa marchandise 夸自己的货色')
            # self.ids.box.add_widget(posLabel)
            # self.ids.box.add_widget(defLabel)
            # self.ids.box.add_widget(senLabel1)
            # self.ids.box.add_widget(senLabel2)
            # posLabel = PosLabel(text='se vanter v. pr.')
            # self.ids.box.add_widget(posLabel)
            # defLabel = DefLabel(text='1. 自吹自擂， 吹牛')
            # self.ids.box.add_widget(defLabel)
            # defLabel = DefLabel(text='2. se vanter de 夸耀， 吹嘘， 以…自豪：')
            # self.ids.box.add_widget(defLabel)
            # senLabel = SenLabel(text="Il n'y a pas de quoi se vanter. 这没什么可吹的。")
            # self.ids.box.add_widget(senLabel)
            # senLabel = SenLabel(text="Et je m'en vante ! 我还感到自豪呢！")
            # self.ids.box.add_widget(senLabel)
            # senLabel = SenLabel(text="Il se vante de réussir. 他夸口说定能够功。")
            # self.ids.box.add_widget(senLabel)











