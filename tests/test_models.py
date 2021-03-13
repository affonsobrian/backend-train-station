import mock

from models.departure import Departure, format_date, get_departure_from_json, get_departures_from_response
from models.station import Station, get_station_from_json, get_stations_from_response

def test_format_date():
    date_str = "2021-12-01T10:15:25+01000"
    result = format_date(date_str)
    expected_result = "01/12/2021 at 10:15:25 (CET)"

    assert result == expected_result


def test_get_departure_from_json():
    json = {
        "plannedDateTime": "2021-12-01T10:15:25+01000",
        "direction": "Aachen Hbf",
        "plannedTrack": "5",
        "trainCategory": "RE"
    }

    expected_result = Departure(
        planned_departure_time="01/12/2021 at 10:15:25 (CET)", 
        direction="Aachen Hbf",
        platform="5",
        train_type="RE"
    )

    result = get_departure_from_json(json)

    assert result == expected_result


def test_get_departures_from_json():
    json = {
        "payload": {
            "departures": [
                {
                    "plannedDateTime": "2021-12-01T10:15:25+01000",
                    "direction": "Aachen Hbf",
                    "plannedTrack": "5",
                    "trainCategory": "RE"
                },
            ]
        }
    }

    response = mock.Mock()
    response.status_code = 200
    response.json = mock.Mock(return_value=json)

    expected_result = [Departure(
        planned_departure_time="01/12/2021 at 10:15:25 (CET)", 
        direction="Aachen Hbf",
        platform="5",
        train_type="RE"
    )]

    result = get_departures_from_response(response)

    assert result == expected_result

def test_get_station_from_json():
    json = {
        "code": "BVB",
        "namen": {
            "lang": "Aachen Hbf",
        }
    }

    expected_result = Station(
        name="Aachen Hbf",
        code="BVB"
    )

    result = get_station_from_json(json)

    assert result == expected_result


def test_get_stations_from_response():
    json = {
        "payload": [
            {
                "code": "BVB",
                "namen": {
                    "lang": "Aachen Hbf",
                }
            }
        ]
    }
    

    response = mock.Mock()
    response.status_code = 200
    response.json = mock.Mock(return_value=json)

    expected_result = [
        Station(
            name="Aachen Hbf",
            code="BVB"
        )
    ]
    result = get_stations_from_response(response)

    assert result == expected_result
