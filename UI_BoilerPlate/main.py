from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_file("main.kv")

class NavigationManager(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class MainApp(App):
    def build(self):
        return NavigationManager()


if __name__ == "__main__":
    MainApp().run()
    
