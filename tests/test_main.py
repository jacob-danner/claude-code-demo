import responses
import os
from dotenv import load_dotenv
from src.main import get_lat_lon

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
