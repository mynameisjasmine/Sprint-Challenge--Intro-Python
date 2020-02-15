# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# this is the base class
class Vehicle:
   def __init__(self, FlightVehicle, Starship):
       self.FlightVehicle = FlightVehicle
       self.Starship = Starship
       pass

    

class Airplane(Vehicle):
    def __init__(self, FlightVehicle, Starship):
        super().__init__(FlightVehicle, Starship)

    pass

class GroundVehicle(Airplane):
    def __init__(self, FlightVehicle, Starship):
        super().__init__(FlightVehicle, Starship)
        
    pass

class Car(GroundVehicle):
    def __init__(self, FlightVehicle, Starship):
        super().__init__(FlightVehicle, Starship)
        
    pass

class Motorcycle(Car):
    def _init__(self, FlightVehicle, Starship):
        super().__init__(FlightVehicle, Starship)
        
    pass
