import requests
import datetime
from flight_data import FlightData
from data_manager import *
tequila_api_entry = "https://api.tequila.kiwi.com/locations/query"
tequila_price_api = "https://api.tequila.kiwi.com/v2/search"
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def get_destination_code(self, city_name):
        # Return "TESTING" for now to make sure Sheety is working. Get TEQUILA API data later.
        params = {
            "term" : city_name
        }
        header = {
            "apikey" : "tB6NfyEM_leRRKm1QMw04vfmbzgdeDyg"
        }
        response = requests.get(url=tequila_api_entry, params=params, headers=header)
        code = response.json()['locations'][0]['code']
        return code


    def get_prices(self, i, data, fly_from, fly_to, date_from, date_to):
        params = {
            'fly_from' : fly_from,
            'fly_to' :fly_to,
            'date_from' :date_from,
            'date_to' : date_to,
            'curr' : 'INR',
            'max_stopovers' : 0
        }
        header = {
            'apikey' : "tB6NfyEM_leRRKm1QMw04vfmbzgdeDyg"
        }
        response = requests.get(url=tequila_price_api, params=params, headers=header)
        fly_from = "LON"
        fly_to = data[i]['iataCode']
        try:
            data = response.json()
            city_from, city_to, price, utc_departure, utc_arrival = data['data'][0]['cityFrom'], data['data'][0]['cityTo'], data['data'][0]['price'], data['data'][0]['utc_departure'], data['data'][0]['utc_arrival']
        except:
            print(f"No flights found for {fly_to}")
            return None
        else:

            my_flight = FlightData(city_from, city_to, price, utc_departure, utc_arrival)
            return my_flight

