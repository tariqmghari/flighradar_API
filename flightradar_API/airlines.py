class airlines():
    def __init__(self,NAME,CODE,ICAO):
        self.name = NAME
        self.code = CODE
        self.ICAO=ICAO
    
    def __str__(self) -> str:
        return f"airline Name: {self.name}\n" \
               f"airline code: {self.code}\n" \
               f"airline ICAO: {self.ICAO}\n" 
