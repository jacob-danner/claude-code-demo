import requests
import os
from typing import Tuple, Dict
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("API_KEY")


def get_lat_lon(city: str, state: str) -> Tuple[float, float]:
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city},{state},us&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()

    if not data:
        raise ValueError(f"No results found for {city}, {state}")

    return data[0]["lat"], data[0]["lon"]


def get_current_weather(lat: float, lon: float) -> Dict[str, float]:
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=imperial"
    response = requests.get(url)
    data = response.json()
    
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    
    # Check if it's raining based on weather conditions
    precipitation = 0.0
    if data["weather"] and data["weather"][0]["main"] == "Rain":
        precipitation = data.get("rain", {}).get("1h", 0.1)  # Default to 0.1 if rain but no amount specified
    
    return {
        "temperature": temperature,
        "humidity": humidity,
        "wind_speed": wind_speed,
        "precipitation": precipitation
    }


def is_criteria_met(weather_data: Dict[str, float]) -> bool:
    temperature = weather_data["temperature"]
    humidity = weather_data["humidity"]
    wind_speed = weather_data["wind_speed"]
    precipitation = weather_data["precipitation"]
    
    # Criteria: 70°F - 90°F, no rain, ≤13 mph wind, <70% humidity
    return (
        70 <= temperature <= 90 and
        precipitation == 0.0 and
        wind_speed <= 13 and
        humidity < 70
    )


def main():
    city = "des-moines"
    state = "IA"
    lat, lon = get_lat_lon(city, state)
    print(lat, lon)


if __name__ == "__main__":
    main()
