from kivy.core.clipboard import Clipboard
from kivy.lang.builder import Builder
from kivy.metrics import dp

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.menu import MDDropdownMenu
from kivymd.toast import toast

KV = '''
MDBoxLayout:
    orientation: "vertical"
    spacing: "12dp"
    padding: "24dp"

    MDScrollView:

        MDBoxLayout:
            id: box
            orientation: "vertical"
            padding: "24dp"
            spacing: "12dp"
            adaptive_height: True

    MDTextField:
        max_height: "200dp"
        mode: "fill"
        multiline: True

    MDWidget:
'''

data = [
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
    "Sed blandit libero volutpat sed cras ornare arcu. Nisl vel pretium "
    "lectus quam id leo in. Tincidunt arcu non sodales neque sodales ut etiam.",
    "Elit scelerisque mauris pellentesque pulvinar pellentesque habitant. "
    "Nisl rhoncus mattis rhoncus urna neque. Orci nulla pellentesque "
    "dignissim enim. Ac auctor augue mauris augue neque gravida in fermentum. "
    "Lacus suspendisse faucibus interdum posuere."

]


class CopyLabel(MDLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.allow_selection = True
        self.adaptive_height = True
        self.theme_text_color = "Custom"
        self.text_color = self.theme_cls.text_color


class Example(MDApp):
    context_menu = None

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_string(KV)

    def on_start(self):
        for text in data:
            copy_label = CopyLabel(text=text)
            copy_label.bind(
                on_selection=self.open_context_menu,
                on_cancel_selection=self.restore_text_color,
            )
            self.root.ids.box.add_widget(copy_label)

    def click_item_context_menu(
        self, type_click: str, instance_label: CopyLabel
    ) -> None:
        Clipboard.copy(instance_label.text)

        if type_click == "copy":
            toast("Copied")
        elif type_click == "cut":
            self.root.ids.box.remove_widget(instance_label)
            toast("Cut")
        if self.context_menu:
            self.context_menu.dismiss()

    def restore_text_color(self, instance_label: CopyLabel) -> None:
        instance_label.text_color = self.theme_cls.text_color

    def open_context_menu(self, instance_label: CopyLabel) -> None:
        instance_label.text_color = "black"
        menu_items = [
            {
                "text": "Copy text",
                "viewclass": "OneLineListItem",
                "height": dp(48),
                "on_release": lambda: self.click_item_context_menu(
                    "copy", instance_label
                ),
            },
            {
                "text": "Cut text",
                "viewclass": "OneLineListItem",
                "height": dp(48),
                "on_release": lambda: self.click_item_context_menu(
                    "cut", instance_label
                ),
            },
        ]
        self.context_menu = MDDropdownMenu(
            caller=instance_label, items=menu_items, width_mult=3
        )
        self.context_menu.open()


Example().run()