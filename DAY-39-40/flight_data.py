class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self,city_from, city_to, price, utc_departure, utc_arrival):
        self.city_from = city_from
        self.city_to =city_to
        self.price = price
        self.utc_arrival = utc_arrival
        self.utc_departure = utc_departure