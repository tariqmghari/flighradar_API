from .requests_handler import requests_handler
from .flights import Flight
from .airlines import airlines
from .airports import airport
from .flights_details import flight_details
class FRadarAPI:
    real_time_flight_tracker_data_url = "https://data-cloud.flightradar24.com/zones/fcgi/feed.js"
    airlines_url="https://www.flightradar24.com/_json/airlines.php"
    airports_url="https://www.flightradar24.com/_json/airports.php"
    payload = {
        "faa": "1",
        "satellite": "1",
        "mlat": "1",
        "flarm": "1",
        "adsb": "1",
        "gnd": "1",
        "air": "1",
        "vehicles": "1",
        "estimated": "1",
        "maxage": "14400",
        "gliders": "1",
        "stats": "1",
        "limit": "5000"
        }
    headers = {
        "accept-encoding": "gzip, br",
        "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
        "cache-control": "max-age=0",
        "origin": "https://www.flightradar24.com",
        "referer": "https://www.flightradar24.com/",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }
    def __init__(self):
        self.request_handler = requests_handler()
    def get_nested_value(self,data, *keys, default=""):
        """
        Recursively retrieves nested keys from a dictionary.
        Returns the value if all keys are present, otherwise returns the default value.
        """
        for key in keys:
            if data is None or key not in data:
                return default
            data = data[key]
        return data
    def get_flights(self):
        flights=[]
        flight_data = self.request_handler.get_flights(self.payload,self.headers,self.real_time_flight_tracker_data_url)
        for flight_id, flight_info in flight_data.items():
            if flight_id[0].isnumeric():
                try:
                    flights.append(Flight(flight_id,flight_info[0],flight_info[1]
                                        ,flight_info[2],flight_info[3],flight_info[4]
                                        ,flight_info[5],flight_info[8],flight_info[9]
                                        ,flight_info[13],flight_info[18]
                                        ))
                except Exception as e:
                    print(e)
        return flights
    def get_flights_with_details(self):
        flights=[]
        flight_data = self.request_handler.get_flights(self.payload,self.headers,self.real_time_flight_tracker_data_url)
        for flight_id, flight_info in flight_data.items():
            if flight_id[0].isnumeric():
                try:
                    flight_details_dict = self.request_handler.get_flight_details(flight_id,self.headers)
                    flights.append(flight_details(flight_id,flight_info[0],flight_info[1]
                                        ,flight_info[2],flight_info[3],flight_info[4]
                                        ,flight_info[5],flight_info[8],flight_info[9]
                                        ,flight_info[13],flight_info[18]
                                        ,self.get_nested_value(flight_details_dict, "aircraft", "model", "text"),
                                        self.get_nested_value(flight_details_dict, "airline", "name"),
                                        self.get_nested_value(flight_details_dict, "airport", "origin", "name"),
                                            self.get_nested_value(flight_details_dict, "airport", "origin", "code", "icao"),
                                            self.get_nested_value(flight_details_dict, "airport", "origin", "position", "country", "name"),
                                            self.get_nested_value(flight_details_dict, "airport", "origin", "position", "country", "code"),
                                            self.get_nested_value(flight_details_dict, "airport", "origin", "position", "region","city"),
                                            self.get_nested_value(flight_details_dict, "airport", "destination", "name"),
                                            self.get_nested_value(flight_details_dict, "airport", "destination", "code", "icao"),
                                            self.get_nested_value(flight_details_dict, "airport", "destination", "position", "country", "name"),
                                            self.get_nested_value(flight_details_dict, "airport", "destination", "position", "country", "code"),
                                            self.get_nested_value(flight_details_dict, "airport", "destination", "position", "region","city"),
                                            self.get_nested_value(flight_details_dict, "time", "schedule", "departure"),
                                            self.get_nested_value(flight_details_dict, "time", "schedule", "arrival"),
                                            self.get_nested_value(flight_details_dict, "time", "real", "departure"),
                                            self.get_nested_value(flight_details_dict, "time", "real", "arrival"),
                                            self.get_nested_value(flight_details_dict, "time", "estimated", "departure"),
                                            self.get_nested_value(flight_details_dict, "time", "estimated", "arrival"),
                                            self.get_nested_value(flight_details_dict, "time", "historical", "flighttime"),
                                            self.get_nested_value(flight_details_dict, "time", "historical", "delay")
                                        ))
                except Exception as e:
                    pass
        return flights
    def get_airlines(self):
        airlines_list=[]
        airlines_request=self.request_handler.get_airlines(self.airlines_url,self.headers)
        for airline in airlines_request["rows"]:
            airlines_list.append(airlines(airline["Name"],airline["Code"],airline["ICAO"]))
        return airlines_list
    def get_airports(self):
        airports_list=[]
        airports_request = self.request_handler.get_airports(self.airports_url,self.headers)
        for airport_x in airports_request["rows"]:
            airports_list.append(airport(airport_x["name"],airport_x["iata"],airport_x["icao"],airport_x["lat"],airport_x["lon"],airport_x["country"],airport_x["alt"]))
        return airports_list
