# Imports
from requests import get
import logging


# Create a constant 'URL_API' with the URL of the API
URL_API = "http://api.covid19api.com"


# FUNCTIONS
def download_summary():
    # Send the HTTP request
    response = get(f"{URL_API}/summary")
    # Check for the HTTP response status 200 (OK)
    if response.status_code == 200:
        # Return the response as JSON
        return response.json()
    # Otherwise, something went wrong
    else:
        # Log the error message
        logging.error(f'An error has occurred: HTTP status {response.status_code}')
        # Return an empty result
        return {}


def download_confirmed_per_country(country):
    """
    Send HTTP request to API /country/<country>/status/confirmed to receive the daily number of confirmed cases for the requested country. Return the response in JSON format.

    API details: https://documenter.getpostman.com/view/10808728/SzS8rjbc#b07f97ba-24f4-4ebe-ad71-97fa35f3b683

    country -- the name of the requested
    """
    # Send the HTTP request
    response = get(f'{URL_API}/country/{country}/status/confirmed')
    # Check for the HTTP response status 200 (OK)
    if response.status_code == 200:
        # Return the response as JSON
        logging.info('Successfully received Dutch data from COVID19 API')
        return { "data" : response.json() }
    # Otherwise, something went wrong
    else:
        # Log the error message
        logging.error(f'An error has occurred: HTTP status {response.status_code}')
        # Return an empty result
        return {}