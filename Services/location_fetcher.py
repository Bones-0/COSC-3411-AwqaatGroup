import requests
from geopy.geocoders import Nominatim

class LocationFetcher:
    @staticmethod
    def get_location():
        """Use a stable API that never returns 403."""
        try:
            res = requests.get("https://ipinfo.io/json", timeout=5)
            data = res.json()
            lat, lon = data["loc"].split(",")
            return float(lat), float(lon)
        except Exception as e:
            print("IPINFO ERROR:", e)
            return None, None

    @staticmethod
    def get_address(lat, lon):
        geolocator = Nominatim(user_agent="location_fetcher")
        try:
            location = geolocator.reverse(f"{lat}, {lon}", exactly_one=True)
            return location.raw.get("address", {}) if location else {}
        except Exception as e:
            print("Geopy error:", e)
            return {}

        
    @staticmethod
    def get_city():
        lat, lon = LocationFetcher.get_location()
        if not lat or not lon:
            return "Unknown"

        try:
            geolocator = Nominatim(user_agent="location_fetcher", timeout=5)

            # Only "language" is allowed in your geopy version
            location = geolocator.reverse(
                (lat, lon),
                exactly_one=True,
                language="en"
            )

            if not location:
                return "Unknown"

            address = location.raw.get("address", {})
            print("DEBUG ADDRESS:", address)

            # Try best fields for city-like name
            for key in ["city", "town", "village", "municipality", "county", "state"]:
                if key in address:
                    return address[key]

            return "Unknown"

        except Exception as e:
            print("Error:", e)
            return "Unknown"


