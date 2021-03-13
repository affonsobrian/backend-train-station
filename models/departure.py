from pydantic import BaseModel
from datetime import datetime

TRAIN_TYPES = {
    "SPR": "Sprinter",
    "IC": "Intercity",
}

class Departure(BaseModel):
    planned_departure_time: str
    direction: str
    platform: str
    train_type: str

def format_date(value: str):
    if value:
        value, _ = value.split("+")
        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S")
        value = datetime.strftime(value, "%d/%m/%Y at %H:%M:%S (CET)")
    return value

def get_departure_from_json(json: dict):
    departure = Departure(
        planned_departure_time=format_date(json.get("plannedDateTime", "")),
        direction=json.get("direction", ""),
        platform=json.get("plannedTrack", ""),
        train_type=json.get("trainCategory", ""),
    )

    departure.train_type = TRAIN_TYPES.get(
        departure.train_type,
        departure.train_type
    )

    return departure

def get_departures_from_response(response):
    if response.status_code == 200:
        departures = [get_departure_from_json(data) for data in response.json()["payload"]["departures"]]
    else:
        departures = []
    return departures
