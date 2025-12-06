import requests

def get_location():
    data = requests.get("https://ipinfo.io/json").json()
    lat, lon = data["loc"].split(",")
    return float(lat), float(lon)
print(get_location())
