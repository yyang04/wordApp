from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.core.window import Window


class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', size_hint=(1, None), height=Window.height)
        button_height = Window.height / 10

        button1 = Button(text='Button 1', size_hint=(1, None), height=button_height)
        button2 = Button(text='Button 2', size_hint=(1, None), height=button_height)

        spacer = Widget()  # 创建一个空的 Widget 作为间隔

        layout.add_widget(button1)
        layout.add_widget(spacer)
        layout.add_widget(button2)

        return layout


if __name__ == '__main__':
    MyApp().run()
