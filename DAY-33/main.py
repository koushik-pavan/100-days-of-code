import requests
from datetime import datetime

my_lat = 28.363800
my_long = 75.600998
parameters = {
    "lat": my_lat,
    "lng": my_long,
    "formatted": 0
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
data = response.json()
sunrise = data["results"]["sunrise"]
print(sunrise.split("T")[1].split(":")[0])
time_now = datetime.now()
print(time_now.hour)
