from kivy.uix.accordion import NumericProperty
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.lang import Builder
import kivy.utils as utils
from kivy.properties import NumericProperty()

Builder.load_file("main.kv")

class NavigationManager(Widget):
    def screen_switcher(self, instance, value)
        counter = self.ids.screen_manager.current_screen
        print("Screen changed to:", value)
class MainApp(App):
    def build(self):
        return NavigationManager()


if __name__ == "__main__":
    MainApp().run()
    
