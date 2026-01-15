import requests
import logging
from django.conf import settings

#get an instance of a logger ==> this will be used to log messages in this module
logger = logging.getLogger(__name__)

def fetch_weather_data(city, aqi='no'):
    """
    Fetch weatheter data for given city using an external weather API.

    Args:
        city (str): Name of the city to fetch weather data for.
    Returns:
        dict: Weather data if successful, None otherwise.
    """

    api_key = settings.WEATHER_API_KEY
    base_url = "http://api.weatherapi.com/current.json"
    params = {
        'key': api_key,
        'q': city,
        'aqi': aqi,
    }

    try:

    # Ten (10) seconds timeout for the request
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()  # Raise an error for bad status codes

        return response.json(), response.status_code

    except requests.exceptions.Timeout:
        logger.error(f"Request to weather API timed out for city: {city}")
        return {"error": "Request timed out"}, 504

    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred for city: {http_err} for city: {city}")
        return {"error": str(http_err)}, response.status_code if 'response' in locals() else 500

    except Exception as e:
        logger.error(f"An error occurred for city: {err} for city: {city}")
        return {"error": "An unexpected error occurred"}, 500
