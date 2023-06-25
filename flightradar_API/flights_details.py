class flight_details:
    def __init__(self,FLIGHTS_ID, ICAO_24_bits,LATITUDE, LONGITUDE, TRACK, ALT, GROUND_SPEED, AIRCRAFT_ICAO, REGISTRATION, FLIGHT_NUMBER,  AIRLINE_ICAO,AIRCRAFT_MODEL, AIRLINE_NAME, AIRPORT_ORIGIN, AIRPORT_ORIGIN_ICAO, AIRPORT_ORIGIN_COUNTRY_NAME, AIRPORT_ORIGIN_COUNTRY_CODE, AIRPORT_ORIGIN_POSITION_REGION, AIRPORT_DESTINATION, AIRPORT_DESTINATION_ICAO, AIRPORT_DESTINATION_COUNTRY_NAME, AIRPORT_DESTINATION_COUNTRY_CODE, AIRPORT_DESTINATION_POSITION_REGION, TIME_SCHEDULE_DEPARTURE, TIME_SCHEDULE_ARRIVAL, TIME_REAL_DEPARTURE, TIME_REAL_ARRIVAL, TIME_ESTIMATED_DEPARTURE, TIME_ESTIMATED_ARRIVAL, TIME_HISTORICAL_FLIGHTTIME, TIME_HISTORICAL_DELAY ):
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
        self.AIRCRAFT_MODEL = AIRCRAFT_MODEL
        self.AIRLINE_NAME = AIRLINE_NAME
        self.AIRPORT_ORIGIN = AIRPORT_ORIGIN
        self.AIRPORT_ORIGIN_ICAO = AIRPORT_ORIGIN_ICAO
        self.AIRPORT_ORIGIN_COUNTRY_NAME = AIRPORT_ORIGIN_COUNTRY_NAME
        self.AIRPORT_ORIGIN_COUNTRY_CODE = AIRPORT_ORIGIN_COUNTRY_CODE
        self.AIRPORT_ORIGIN_POSITION_REGION = AIRPORT_ORIGIN_POSITION_REGION
        self.AIRPORT_DESTINATION = AIRPORT_DESTINATION
        self.AIRPORT_DESTINATION_ICAO = AIRPORT_DESTINATION_ICAO
        self.AIRPORT_DESTINATION_COUNTRY_NAME = AIRPORT_DESTINATION_COUNTRY_NAME
        self.AIRPORT_DESTINATION_COUNTRY_CODE = AIRPORT_DESTINATION_COUNTRY_CODE
        self.AIRPORT_DESTINATION_POSITION_REGION = AIRPORT_DESTINATION_POSITION_REGION
        self.TIME_SCHEDULE_DEPARTURE = TIME_SCHEDULE_DEPARTURE
        self.TIME_SCHEDULE_ARRIVAL = TIME_SCHEDULE_ARRIVAL
        self.TIME_REAL_DEPARTURE = TIME_REAL_DEPARTURE
        self.TIME_REAL_ARRIVAL = TIME_REAL_ARRIVAL
        self.TIME_ESTIMATED_DEPARTURE = TIME_ESTIMATED_DEPARTURE
        self.TIME_ESTIMATED_ARRIVAL = TIME_ESTIMATED_ARRIVAL
        self.TIME_HISTORICAL_FLIGHTTIME = TIME_HISTORICAL_FLIGHTTIME
        self.TIME_HISTORICAL_DELAY = TIME_HISTORICAL_DELAY
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
               f"Airline ICAO: {self.AIRLINE_ICAO}\n" \
               f"Aircraft Model: {self.AIRCRAFT_MODEL}\n" \
               f"Airline Name: {self.AIRLINE_NAME}\n" \
               f"Origin Airport: {self.AIRPORT_ORIGIN}\n" \
               f"Origin Airport ICAO: {self.AIRPORT_ORIGIN_ICAO}\n" \
               f"Origin Country: {self.AIRPORT_ORIGIN_COUNTRY_NAME}\n" \
               f"Origin Country Code: {self.AIRPORT_ORIGIN_COUNTRY_CODE}\n" \
               f"Origin Region: {self.AIRPORT_ORIGIN_POSITION_REGION}\n" \
               f"Destination Airport: {self.AIRPORT_DESTINATION}\n" \
               f"Destination Airport ICAO: {self.AIRPORT_DESTINATION_ICAO}\n" \
               f"Destination Country: {self.AIRPORT_DESTINATION_COUNTRY_NAME}\n" \
               f"Destination Country Code: {self.AIRPORT_DESTINATION_COUNTRY_CODE}\n" \
               f"Destination Region: {self.AIRPORT_DESTINATION_POSITION_REGION}\n" \
               f"Schedule Departure Time: {self.TIME_SCHEDULE_DEPARTURE}\n" \
               f"Schedule Arrival Time: {self.TIME_SCHEDULE_ARRIVAL}\n" \
               f"Real Departure Time: {self.TIME_REAL_DEPARTURE}\n" \
               f"Real Arrival Time: {self.TIME_REAL_ARRIVAL}\n" \
               f"Estimated Departure Time: {self.TIME_ESTIMATED_DEPARTURE}\n" \
               f"Estimated Arrival Time: {self.TIME_ESTIMATED_ARRIVAL}\n" \
               f"Historical Flight Time: {self.TIME_HISTORICAL_FLIGHTTIME}\n" \
               f"Historical Delay: {self.TIME_HISTORICAL_DELAY}"