from twilio.rest import Client
account_sid = 'AC025e00e80850cff3eceb291b2836a60f'
auth_token = 'a8b4485d1b21af6b2c7efa3ced16be5c'
client = Client(account_sid, auth_token)
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def send_message(self, my_flight):
        body = f"{my_flight.city_from} ----> {my_flight.city_to} on {my_flight.utc_departure} ----> {my_flight.utc_arrival} for the cost of {my_flight.price}"
        message = client.messages.create(
            from_='+17165266244',
            body=body,
            to='+918248298176'
        )