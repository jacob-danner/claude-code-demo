# Overview

I want python script to help me decide when to go for a bike ride

## General

- Use OpenWeatherMap API (1000 free calls/day):
  - **Current Weather API**: For real-time conditions
  - **Geocoding API**: Convert location names to coordinates
  - **5-day Forecast API**: For planning ahead
  - **Air Pollution API**: For air quality data (4-day, 1-hour intervals)

## Phase 1 - Use Geocoding API to get (lat, long) for location

DONE

## Phase 2 - Is it good weather to bike right now?

If 2/4 criteria are met, weather is good enough to bike

### Good Weather Criteria for Biking

- **Temperature**: 70°F - 90°F ideal range
- **Precipitation**: No rain
- **Wind Speed**: 13 mph or less
- **Humidity**: Less than 70%
