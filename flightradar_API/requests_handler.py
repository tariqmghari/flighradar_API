import requests
import json
class requests_handler:
    def get_flight_details(self,flight_id,headers):
        url = f"https://data-live.flightradar24.com/clickhandler/?flight={flight_id}"
        response = requests.get(url,headers=headers)
        return json.loads(response.content)
    def get_flights(self, payload, header, url):
        url += "?" + "&".join(["{}={}".format(k, v) for k, v in payload.items()])
        response = requests.get(url,headers=header)
        return json.loads(response.content)
    def get_airlines(self, url, headers):
        response = requests.get(url, headers = headers)
        return json.loads(response.content)
    def get_airports(self,url,headers):
        response = requests.get(url,headers=headers)
        return json.loads(response.content)