#A system for managing vehicles available for rent,
#where each type of vehicle (car, bike, etc.) behaves differently.
#Customers can rent and return vehicles
from abc import ABC ,abstractmethod
class Vehicle(ABC):
    def __init__(self,brand,model,price_per_day):
        self.brand=brand
        self.model=model
        self.price_per_day=price_per_day
        self.available=True
    @abstractmethod
    def rent(self):
        pass
    def return_vehicle(self):
        pass
class Car(Vehicle):
    def rent(self):
        self.available=False
        return f"{self.brand} {self.model} has been rented."
    def return_vehicle(self):
        self.available=True
        return f"{self.brand} {self.model} has been returned."
class Customer:
    def __init__(self,name):
        self.name=name
        self.rented_vehicles=[]
    def rent_vehicle(self,vehicle):
        if vehicle.available:
            vehicle.rent()
            self.rented_vehicles.append(vehicle)
            return f"{self.name} has rented {vehicle.brand} {vehicle.model}"
        else:
            return f"{self.name} has not rented {vehicle.brand} {vehicle.model}"
    def return_vehicle(self,vehicle):
        vehicle.available=True
        self.rented_vehicles.remove(vehicle)
        return f"{self.name} has returned {vehicle.brand} {vehicle.model}"

class RentalAgency:
    def __init__(self,name):
        self.name=name
        self.vehicles=[]
    def add_vehicle(self,vehicle):
        self.vehicles.append(vehicle)
    def show_available_vehicles(self):
        print("\nAvailable Vehicle:\n")
        for v in self.vehicles:
            if v.available:
                print(f"{v.brand} {v.model} for ${v.price_per_day}/day")

#Example Usage
c1=Car("Mercedes Benz","e250",120)
c2=Car("Bmw","i6",110)
agency1=RentalAgency("Floran")
agency1.add_vehicle(c1)
agency1.add_vehicle(c2)
agency1.show_available_vehicles()