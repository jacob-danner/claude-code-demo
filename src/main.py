import requests
import os
from typing import Tuple
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


def main():
    city = "des-moines"
    state = "IA"
    lat, lon = get_lat_lon(city, state)
    print(lat, lon)


if __name__ == "__main__":
    main()
