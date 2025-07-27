import responses
import os
from dotenv import load_dotenv
from src.main import get_lat_lon, get_current_weather, is_criteria_met

load_dotenv()

API_KEY = os.environ.get("API_KEY")


@responses.activate
def test_get_lat_lon():
    url = f"http://api.openweathermap.org/geo/1.0/direct?q=des-moines,ia,us&appid={API_KEY}"
    responses.add(
        responses.GET,
        url,
        json=[
            {
                "name": "Des Moines",
                "lat": 41.5868654,
                "lon": -93.6249494,
                "country": "US",
                "state": "Iowa",
            }
        ],
        status=200,
    )

    lat, lon = get_lat_lon("des-moines", "ia")

    assert lat == 41.5868654
    assert lon == -93.6249494


@responses.activate
def test_get_current_weather():
    lat, lon = 41.5868654, -93.6249494
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=imperial"
    responses.add(
        responses.GET,
        url,
        json={
            "coord": {"lon": -93.6249494, "lat": 41.5868654},
            "weather": [{"id": 800, "main": "Clear", "description": "clear sky", "icon": "01d"}],
            "main": {
                "temp": 75.0,
                "feels_like": 72.0,
                "temp_min": 70.0,
                "temp_max": 80.0,
                "pressure": 1013,
                "humidity": 65
            },
            "wind": {
                "speed": 10.0,
                "deg": 180
            },
            "visibility": 10000,
            "clouds": {"all": 0},
            "dt": 1625097600,
            "sys": {
                "type": 1,
                "id": 1234,
                "country": "US",
                "sunrise": 1625049600,
                "sunset": 1625105400
            },
            "timezone": -18000,
            "id": 4853828,
            "name": "Des Moines",
            "cod": 200
        },
        status=200,
    )

    weather_data = get_current_weather(lat, lon)

    assert weather_data["temperature"] == 75.0
    assert weather_data["humidity"] == 65.0
    assert weather_data["wind_speed"] == 10.0
    assert weather_data["precipitation"] == 0.0


@responses.activate
def test_get_current_weather_with_rain():
    lat, lon = 41.5868654, -93.6249494
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=imperial"
    responses.add(
        responses.GET,
        url,
        json={
            "coord": {"lon": -93.6249494, "lat": 41.5868654},
            "weather": [{"id": 500, "main": "Rain", "description": "light rain", "icon": "10d"}],
            "main": {
                "temp": 75.0,
                "feels_like": 72.0,
                "temp_min": 70.0,
                "temp_max": 80.0,
                "pressure": 1013,
                "humidity": 65
            },
            "wind": {
                "speed": 10.0,
                "deg": 180
            },
            "rain": {
                "1h": 0.5
            },
            "visibility": 10000,
            "clouds": {"all": 75},
            "dt": 1625097600,
            "sys": {
                "type": 1,
                "id": 1234,
                "country": "US",
                "sunrise": 1625049600,
                "sunset": 1625105400
            },
            "timezone": -18000,
            "id": 4853828,
            "name": "Des Moines",
            "cod": 200
        },
        status=200,
    )

    weather_data = get_current_weather(lat, lon)

    assert weather_data["temperature"] == 75.0
    assert weather_data["humidity"] == 65.0
    assert weather_data["wind_speed"] == 10.0
    assert weather_data["precipitation"] == 0.5


def test_is_criteria_met_good_weather():
    weather_data = {
        "temperature": 75.0,
        "humidity": 65.0,
        "wind_speed": 10.0,
        "precipitation": 0.0
    }
    
    assert is_criteria_met(weather_data) == True


def test_is_criteria_met_bad_weather():
    weather_data = {
        "temperature": 95.0,
        "humidity": 80.0,
        "wind_speed": 20.0,
        "precipitation": 0.5
    }
    
    assert is_criteria_met(weather_data) == False
