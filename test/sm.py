from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button


class RootWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        # 创建一个ScreenManager
        screen_manager = ScreenManager()

        # 创建两个Screen
        screen1 = Screen(name='Screen 1')
        screen2 = Screen(name='Screen 2')

        # 在Screen中添加组件
        button1 = Button(text='Go to Screen 2')
        button1.bind(on_release=lambda x: self.go_to_screen(screen_manager, 'Screen 2'))
        screen1.add_widget(button1)

        button2 = Button(text='Go to Screen 1')
        button2.bind(on_release=lambda x: self.go_to_screen(screen_manager, 'Screen 1'))
        screen2.add_widget(button2)

        # 将Screen添加到ScreenManager中
        screen_manager.add_widget(screen1)
        screen_manager.add_widget(screen2)

        # 将ScreenManager添加到根节点中
        self.add_widget(screen_manager)

    def go_to_screen(self, screen_manager, screen_name):
        screen_manager.current = screen_name

class MyApp(App):
    def build(self):
        return RootWidget()


if __name__ == '__main__':
    MyApp().run()