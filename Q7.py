class Aeroplane():

    def __init__(self, departure: str, destination: str):
        self.departure = departure
        self.destination = destination
        self.fuel = 0
        self.altitude = 0

    def setFuel(self, fuel: int):
        self.fuel = fuel
        print(f"Fuel level is now at {self.fuel} litres")
        if self.fuel < 150000:
            print("150000 litres is needed to complete a full flight")

    def increaseAltitude(self):
        self.altitude += 1000
        print(f"Altitude increased and is now {self.altitude}")
    
    def decreaseAltitude(self):
        if self.altitude > 0:
            self.altitude -= 1000
            print(f"Altitude decreased and is now {self.altitude}")
        else:
            print("Plane is already on ground")

    def setDeparture(self, departure: str):
        self.departure = departure
        print(f"Departure is now {self.departure}")

    def setDestination(self, destination: str):
        self.destination = destination
        print(f"Destination is now {self.destination}")
    
    def getDeparture(self) -> str:
        return self.departure
    
    def getDestination(self) -> str:
        return self.destination
    
    def getAltitude(self) -> int:
        return self.altitude
    
    def __str__(self):
        out = f"Aeroplane object flying from {self.departure} to {self.destination}."
        out += f"\n\nAltitude: {self.altitude}m\nFuel: {self.fuel}l"
        return out 
    

def testPlane():
    plane = Aeroplane("London", "New York")
    plane.setFuel(150000)

    # Should be refactored into a plane.fly method
    plane.increaseAltitude()
    plane.decreaseAltitude()
    plane.setFuel(0)
    plane.setDeparture("New York")

    plane.setDestination("London")

    plane.increaseAltitude()
    plane.decreaseAltitude()
    plane.setFuel(0)
    plane.setDeparture("London")
    plane.decreaseAltitude()

    print(plane)




