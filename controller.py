from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from utils import train_requests

from models.station import get_stations_from_response
from models.departure import get_departures_from_response

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def index():
    return {"status": "Working"}


@app.get("/stations")
def get_stations():
    response = train_requests.get_stations()
    stations = get_stations_from_response(response)
    return stations


@app.get("/departures/{station_code}")
def get_departures(station_code: str):
    response = train_requests.get_departures(station_code)
    departures = get_departures_from_response(response)
    return departures
