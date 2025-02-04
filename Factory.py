from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass

class Car(Vehicle):
    def drive(self):
        print("driving car!")

class Bike(Vehicle):
    def drive(self):
        print("driving bike!")

class VehicleFactory:
    @staticmethod
    def getVehicle(vehicle_type):
        if vehicle_type == "car":
            return Car()
        elif vehicle_type == "bike":
            return Bike()
        else:
            return None
        
if __name__ == "__main__":
    vehicle1 = VehicleFactory.getVehicle("car")
    vehicle1.drive()
    vehicle2 = VehicleFactory.getVehicle("bike")
    vehicle2.drive()