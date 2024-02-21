import requests
from twilio.rest import Client

account_sid = "AC025e00e80850cff3eceb291b2836a60f"
auth_token = "a8b4485d1b21af6b2c7efa3ced16be5c"
parameters = {
    "lat":28.363800,
    "lon":75.600998,
    "cnt":4,
    "appid": "4d268184d208e163116753f51256163e"
}

received = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
weather_data = received.json()
will_rain = False
for i in range(len(weather_data["list"])):
    hourly_3 = weather_data["list"][i]["weather"][0]["id"]
    if hourly_3 < 800:
        will_rain = True

client = Client(account_sid, auth_token)

if will_rain:
    message = client.messages \
        .create(
        body='Get an Umbrella',
        from_='+17165266244',
        to='+919884411528'
    )
else:
    message = client.messages \
        .create(
        body='Are you going to the office?',
        from_='+17165266244',
        to='+919884411528'
    )


