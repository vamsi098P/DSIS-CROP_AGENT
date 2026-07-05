import streamlit as st
import requests


class WeatherService:

    def __init__(self):
        self.api_key = st.secrets["WEATHER_API_KEY"]

    def get_weather(self, city):

        url = (
            f"http://api.weatherapi.com/v1/current.json"
            f"?key={self.api_key}"
            f"&q={city}"
            f"&aqi=yes"
        )

        response = requests.get(url)

        if response.status_code != 200:
            print(response.text)
            return None

        data = response.json()

        current = data["current"]
        location = data["location"]

        return {

            "city": location["name"],

            "country": location["country"],

            "temperature": current["temp_c"],

            "humidity": current["humidity"],

            "wind_speed": current["wind_kph"],

            "rainfall": current.get("precip_mm", 0),

            "condition": current["condition"]["text"],

            "icon": "https:" + current["condition"]["icon"]

        }