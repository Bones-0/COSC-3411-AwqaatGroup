from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.lang import Builder
import kivy.utils as utils
from kivy.core.window import Window
from kivy.clock import Clock
from datetime import datetime, timedelta

from prayer_calculation import PrayerTimeFetcher
from location_fetcher import LocationFetcher
from kivy.core.audio import SoundLoader

Builder.load_file("./UserInterface/main.kv")
Window.title = "Awqaat"
adhan = SoundLoader.load('./sounds/azan.mp3')

class NavigationManager(FloatLayout):
    
    def hide_widget(self, widget):
        widget.opacity = 0
        widget.disabled = True

    def show_widget(self, widget):
        widget.opacity = 1
        widget.disabled = False 
        
    def mute_adhan(self):
        if adhan:
            adhan.stop()
            self.hide_widget(self.ids.mute_button)
    
    def screen_switcher(self, instance, button):
        sm = self.ids.current_screen
        sm.current = instance
        print("Screen changed to:", instance)

    def on_kv_post(self, base_widget):
        self.app_setup()
        self.update_next_prayer()
        self.hide_widget(self.ids.mute_button)
        # Update prayer every minute (in case you switch times manually)
        Clock.schedule_interval(self.update_next_prayer, 60)

        # Update the countdown every second
        Clock.schedule_interval(self.update_countdown, 1)

    def app_setup(self):
        current_city = LocationFetcher.get_city()
        lat, lon = LocationFetcher.get_location()
        self.lat, self.lon = lat, lon

        self.prayer_times = PrayerTimeFetcher.get_prayer_times(lat, lon)

        if not self.prayer_times:
            print("Could not fetch prayer times.")
            return

        # populate UI
        self.ids.fajr_label.text = f"Fajr: {self.prayer_times['Fajr']}"
        self.ids.duhur_label.text = f"Dhuhr: {self.prayer_times['Dhuhr']}"
        self.ids.asr_label.text = f"Asr: {self.prayer_times['Asr']}"
        self.ids.maghrib_label.text = f"Maghrib: {self.prayer_times['Maghrib']}"
        self.ids.isha_label.text = f"Isha: {self.prayer_times['Isha']}"

        self.ids.location_label.text = f"Location: {current_city} ({lat}, {lon})"

    def reset_label_colors(self):
        for name in ["fajr", "duhur", "asr", "maghrib", "isha"]:
            self.ids[name + "_label"].color = utils.get_color_from_hex("#000000")

    def find_next_prayer(self):
        """Return the next prayer name and its datetime."""
        MAIN_PRAYERS = {"fajr", "dhuhr", "asr", "maghrib", "isha"}
        now = datetime.now()

        # check today's remaining prayers
        for prayer, time_str in sorted(self.prayer_times.items(), key=lambda x: x[1]):
            if prayer.lower() in MAIN_PRAYERS:
                prayer_dt = datetime.strptime(time_str, "%H:%M").replace(
                    year=now.year, month=now.month, day=now.day
                )
                if now < prayer_dt:
                    return prayer.lower(), prayer_dt

        # If no remaining prayers → next prayer = tomorrow's Fajr
        fajr_time = self.prayer_times["Fajr"]
        tomorrow_fajr = datetime.strptime(fajr_time, "%H:%M").replace(
            year=now.year, month=now.month, day=now.day
        ) + timedelta(days=1)

        return "fajr", tomorrow_fajr

    def update_next_prayer(self, *args):
        self.reset_label_colors()

        prayer, prayer_dt = self.find_next_prayer()
        self.next_prayer = prayer
        self.next_prayer_time = prayer_dt  # save for countdown

        # Highlight next prayer
        highlight_id = prayer + "_label"
        if highlight_id in self.ids:
            self.ids[highlight_id].color = utils.get_color_from_hex("#FF0000")

    def update_countdown(self, *args):
        """Update time remaining until the next prayer."""
        if not hasattr(self, "next_prayer_time"):
            return

        now = datetime.now()
        remaining = self.next_prayer_time - now

        # When prayer time reaches 0 → recompute next prayer
        if remaining.total_seconds() <= 0:
            if adhan:
                adhan.volume = 1.0
                adhan.play()
                show_widget(self.ids.mute_button)

            self.update_next_prayer()
            return

        hours = remaining.seconds // 3600
        minutes = (remaining.seconds % 3600) // 60
        seconds = remaining.seconds % 60

        self.ids.time_remaining_label.text = (
            f"Time until {self.next_prayer.capitalize()}: "
            f"{hours:02}:{minutes:02}:{seconds:02}"
        )


class MainApp(App):
    title = "Awqaat"

    def build(self):
        return NavigationManager()


if __name__ == "__main__":
    MainApp().run()
