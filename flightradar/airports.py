class airport:
    def __init__(self, NAME, IATA, ICAO, LAT, LON, COUNTRY, ALT):
        self.name =NAME
        self.IATA =IATA
        self.ICAO =ICAO
        self.LAT =LAT
        self.LON =LON
        self.COUNTRY =COUNTRY
        self.ALT =ALT
    def __str__(self) -> str:
        return f"airport Name: {self.name}\n" \
               f"airport IATA: {self.IATA}\n" \
               f"airport ICAO: {self.ICAO}\n" \
               f"airport LAT: {self.LAT}\n" \
               f"airport LON: {self.LON}\n" \
               f"airport COUNTRY: {self.COUNTRY}\n" \
               f"airport ALT: {self.ALT}\n" 