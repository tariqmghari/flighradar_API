class Flight():

    def __init__(self,FLIGHTS_ID, ICAO_24_bits,LATITUDE, LONGITUDE, TRACK, ALT, GROUND_SPEED, AIRCRAFT_ICAO, REGISTRATION, FLIGHT_NUMBER,AIRLINE_ICAO):
        self.FLIGHTS_ID = FLIGHTS_ID
        self.ICAO_24_bits = ICAO_24_bits
        self.LATITUDE = LATITUDE
        self.LONGITUDE = LONGITUDE
        self.TRACK = TRACK
        self.ALT = ALT
        self.GROUND_SPEED = GROUND_SPEED
        self.AIRCRAFT_ICAO = AIRCRAFT_ICAO
        self.REGISTRATION = REGISTRATION
        self.FLIGHT_NUMBER = FLIGHT_NUMBER
        self.AIRLINE_ICAO = AIRLINE_ICAO
    def __str__(self):
        return f"Flight ID: {self.FLIGHTS_ID}\n" \
               f"ICAO 24 bits: {self.ICAO_24_bits}\n" \
               f"Latitude: {self.LATITUDE}\n" \
               f"Longitude: {self.LONGITUDE}\n" \
               f"Track: {self.TRACK}\n" \
               f"Altitude: {self.ALT}\n" \
               f"Ground Speed: {self.GROUND_SPEED}\n" \
               f"Aircraft ICAO: {self.AIRCRAFT_ICAO}\n" \
               f"Registration: {self.REGISTRATION}\n" \
               f"Flight Number: {self.FLIGHT_NUMBER}\n" \
               f"Airline ICAO: {self.AIRLINE_ICAO}\n"