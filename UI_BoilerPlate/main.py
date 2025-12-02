from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

# Load the kv files
Builder.load_file("main.kv")

class NavigationManager(ScreenManager):
    def screen_switcher(self, screen_name):
        # 'nav_manager' will be the id of NavigationManager in KV
        screen_manager = self.ids.nav_manager
        screen_manager.current = screen_name
        print("Screen changed to:", screen_name)


class MainApp(App):
    def build(self):
        return NavigationManager()

if __name__ == "__main__":
    MainApp().run()
