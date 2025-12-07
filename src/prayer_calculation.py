import requests

class PrayerTimeFetcher:

    @staticmethod
    def get_prayer_times(lat, lon, method=4):
        """
        Fetch today's prayer times from Aladhan API.
        Default method = 4 (Umm al-Qura)
        """
        try:
            url = (
                f"https://api.aladhan.com/v1/timings?"
                f"latitude={lat}&longitude={lon}&method={method}"
            )

            response = requests.get(url, timeout=5).json()

            if response["code"] != 200:
                return None

            print(response)
            return response["data"]["timings"]

        except Exception as e:
            print("Error fetching prayer times:", e)
            return None
