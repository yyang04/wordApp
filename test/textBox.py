from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.app import App


class MainApp(MDApp):
    def build(self):
        return Builder.load_string(
            """
MDBoxLayout:
    orientation: 'vertical'
    
    MDLabel:
        text: "Label with valign = middle"
        size_hint_y: None
        height: self.texture_size[1] + 100
        valign: 'center'
            

    MDLabel:
        text: "Label with valign = bottom"
        height: self.texture_size[1]
        valign: "bottom"
""")


if __name__ == '__main__':
    MainApp().run()
