from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.uix.button import MDIconButton

from kivymd.app import MDApp
from kivymd.uix.list import IRightBody, OneLineAvatarIconListItem, OneLineAvatarListItem, OneLineRightIconListItem
from kivymd.uix.label import MDLabel
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.icon_definitions import md_icons


KV = '''
<ListItemWithCheckbox>:

    RightCheckbox:
        id: plus

MDScrollView:

    MDList:
        id: scroll
'''


class ListItemWithCheckbox(OneLineRightIconListItem):
    '''Custom list item.'''

    icon = StringProperty()


class RightCheckbox(IRightBody, MDIconButton):
    '''Custom right container.'''
    icon = 'plus'



class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)

    def on_start(self):
        icons = list(md_icons.keys())
        for i in range(30):
            item = ListItemWithCheckbox(text=f"Item {i}", icon=icons[i])
            item.ids.plus.bind(on_release=lambda x: print("1"))
            self.root.ids.scroll.add_widget(item)


Example().run()