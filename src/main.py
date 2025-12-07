from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.lang import Builder
import kivy.utils as utils
from kivy.animation import Animation
from kivy.core.window import Window

from prayer_calculation import PrayerTimeFetcher
from location_fetcher import LocationFetcher

Builder.load_file("./UserInterface/main.kv")
Window.title = "Awqaat"

class NavigationManager(FloatLayout):
    def app_setup(self):
        current_city = LocationFetcher.get_city()
        lat, lon = LocationFetcher.get_location()
        prayer_times = PrayerTimeFetcher.get_prayer_times(lat, lon)

        if not prayer_times:
            print("Could not fetch prayer times.")
            return

        self.ids.fajr_label.text = f"Fajr: {prayer_times['Fajr']}"
        self.ids.duhur_label.text = f"Dhuhr: {prayer_times['Dhuhr']}"
        self.ids.asr_label.text = f"Asr: {prayer_times['Asr']}"
        self.ids.magrib_label.text = f"Magrib: {prayer_times['Maghrib']}"   
        self.ids.isha_label.text = f"Isha: {prayer_times['Isha']}"

        self.ids.location_label.text = f"Location: {current_city}, ({lat}, {lon})"        
     
    def screen_switcher(self, instance, button):
        sm = self.ids.current_screen
        sm.current = instance
        print("Screen changed to:", instance)
    def on_kv_post(self, base_widget):
        self.app_setup()

class MainApp(App):
    title = "Awqaat"
    
    def build(self):
        return NavigationManager()

if __name__ == "__main__":
    MainApp().run()
