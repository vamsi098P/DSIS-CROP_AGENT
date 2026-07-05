from services.weather_service import WeatherService

weather = WeatherService()

result = weather.get_weather("Vijayawada")

print(result)