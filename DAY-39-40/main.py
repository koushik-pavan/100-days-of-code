#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirement.
from data_manager import DataManager
from flight_search import FlightSearch
import requests
from flight_data import FlightData
import datetime
from notification_manager import NotificationManager
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()


for i in range(len(sheet_data)):
    if sheet_data[i]['iataCode'] == '':
        #print(sheet_data[i])
        flight_search = FlightSearch()
        sheet_data[i]['iataCode'] = flight_search.get_destination_code(sheet_data[i]["city"])

data_manager.destination_data = sheet_data

data_manager.update_destination_codes()
print(data_manager.destination_data)

date_from = datetime.date.today()
date_to = date_from + datetime.timedelta(days=180)
date_from = date_from.strftime("%d/%m/%Y")
date_to = date_to.strftime("%d/%m/%Y")
message = NotificationManager()
for i in range(len(sheet_data)):
    fly_from = "LON"
    fly_to = data_manager.destination_data[i]['iataCode']
    flight_search = FlightSearch()

    #city_from, city_to, price, utc_departure, utc_arrival = flight_search.get_prices(i= i, data = data_manager.destination_data, fly_from=fly_from, fly_to=fly_to, date_from=date_from, date_to=date_to)
    #my_flight = FlightData(city_from, city_to, price, utc_departure, utc_arrival)
    my_flight = flight_search.get_prices(i= i, data = data_manager.destination_data, fly_from=fly_from, fly_to=fly_to, date_from=date_from, date_to=date_to)
    if my_flight is None:
        continue
    else:
        print(my_flight.price)
    if my_flight.price<data_manager.destination_data[i]['lowestPrice']:
        message.send_message(my_flight)

