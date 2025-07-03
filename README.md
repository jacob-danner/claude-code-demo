# Bike Ride Weather Recommendation System

A Python-based application that uses the OpenWeatherMap API to help users decide when to go for a bike ride based on weather conditions.

## Overview

This project provides a foundation for weather-based bike ride recommendations. The main script currently implements geocoding functionality to convert city and state names into geographic coordinates (latitude and longitude) using the OpenWeatherMap API.

## Main Script Functionality

The main script (`src/main.py`) performs the following operations:

1. **Environment Setup**: Loads configuration from environment variables using python-dotenv
2. **Geocoding Service**: Converts city/state combinations to precise latitude/longitude coordinates
3. **API Integration**: Interfaces with OpenWeatherMap's geocoding API to retrieve location data
4. **Error Handling**: Validates API responses and handles cases where locations cannot be found

### Current Implementation

The script demonstrates geocoding by:
- Taking a city name and state abbreviation as input
- Making a request to the OpenWeatherMap geocoding API
- Extracting and returning the latitude and longitude coordinates
- Currently hardcoded to fetch coordinates for Des Moines, IA

## Setup Requirements

### Prerequisites
- Python 3.7+
- OpenWeatherMap API key

### Environment Configuration

Create a `.env` file in the project root with your OpenWeatherMap API key:

```
API_KEY=your_openweathermap_api_key
```

You can obtain a free API key by registering at [OpenWeatherMap](https://openweathermap.org/api).

### Dependencies

Install required packages using uv:

```bash
uv sync
```

## Usage

Run the main application:

```bash
uv run python src/main.py
```

This will output the latitude and longitude coordinates for the configured location.

## Development

### Running Tests
```bash
uv run pytest             # Run all tests
uv run pytest tests/test_main.py::test_get_lat_lon  # Run specific test
```

### Code Quality
```bash
uv run ruff check          # Lint code
uv run ruff check --fix    # Auto-fix linting issues
uv run ruff format         # Format code
```

## Future Enhancements

The current implementation provides the foundation for a complete bike ride weather recommendation system. Future development could include:

- Weather data retrieval for the geocoded locations
- Bike-riding condition analysis (temperature, precipitation, wind)
- Recommendation engine based on weather conditions
- User interface for location input and recommendation display

---

*Generated with assistance from Claude AI* >