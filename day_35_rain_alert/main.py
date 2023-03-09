import requests

api_key = "c138e2cb6b00a2dfed09d3d4f56eda2a"
weather_url = "https://api.openweathermap.org/data/3.0/onecall"
MY_LAT = 36.778259
MY_LONG = -119.417931

parameters = {
    'lat': MY_LAT,
    'lon': MY_LONG,
    'appid': api_key,
}

response = requests.get(weather_url, parameters)
print(response.raise_for_status())
data = response.json()
print(data)
