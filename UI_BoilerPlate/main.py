from kivy.app import App
from kivy.uix.label import Label

class NavigationManger():
    pass    

class MainApp(App):
    def build(self):
        return NavigationManger()


if __name__ == "__main__":
    MainApp().run()
    
