import requests

from utils.config import OCP_API_KEY

BASE_ENDPOINT = "https://gateway.apiportal.ns.nl/reisinformatie-api/api/v2"

def get_headers():
    headers = {
        "content-type": "application/json",
        "Ocp-Apim-Subscription-Key": OCP_API_KEY
    }
    return headers


def get_stations(headers=None):
    if not headers:
        headers = get_headers()
    result = requests.get(f"{BASE_ENDPOINT}/stations", headers=headers) 
    return result


def get_departures(stations_code, headers=None):
    if not headers:
        headers = get_headers()
    result = requests.get(f"{BASE_ENDPOINT}/departures?station={stations_code}", headers=headers) 
    return result
