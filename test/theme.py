from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''

MDCard:
    orientation: "vertical"
    padding: 0, 0, 0 , "36dp"
    size_hint: .5, .5
    pos_hint: {"center_x": .5, "center_y": .5}
    elevation: 2
    shadow_offset: 0, -2

    MDLabel:
        text: "Theme style - {}".format(app.theme_cls.theme_style)
        halign: "center"
        valign: "center"
        bold: True
        font_style: "H5"

    MDRaisedButton:
        text: "Set theme"
        on_release: app.switch_theme_style()
        pos_hint: {"center_x": .5}
'''


class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_string(KV)

    def switch_theme_style(self):
        self.theme_cls.primary_palette = (
            "Orange" if self.theme_cls.primary_palette == "Red" else "Red"
        )
        self.theme_cls.theme_style = (
            "Dark" if self.theme_cls.theme_style == "Light" else "Light"
        )


Example().run()