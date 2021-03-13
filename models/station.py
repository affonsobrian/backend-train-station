from pydantic import BaseModel

class Station(BaseModel):
    name: str
    code: str

def get_station_from_json(json):
    station = Station(name=json["namen"]["lang"], code=json["code"])
    return station

def get_stations_from_response(response):
    if response.status_code == 200:
        stations = [get_station_from_json(data) for data in response.json()["payload"]]
    else:
        stations = []
    stations.sort(key=lambda x : x.name)
    return stations