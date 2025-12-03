from kivy.uix.filechooser import ScreenManager
from kivy.uix.accordion import NumericProperty
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.lang import Builder
import kivy.utils as utils
from kivy.animation import Animation

Builder.load_file("main.kv")

class NavigationManager(Widget):
    def screen_switcher(self, instance, button):
        ScreenManager = self.ids.current_screen
        ScreenManager.current = instance
        print("Screen changed to:", instance)

        animate_button = Animation(
            background_color=utils.get_color_from_hex("#CCCCCC"), 
            duration=0.2
        )
        animate_button.start(button)

class MainApp(App):
    def build(self):
        return NavigationManager()


if __name__ == "__main__":
    MainApp().run()
        
