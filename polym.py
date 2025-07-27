from abc import my_car, abstractmethod

class Vehicle(my_car):
    @abstractmethod
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

def demonstrate_polymorphism():
    vehicles = [Car(), Plane()]

    for vehicle in vehicles:
        vehicle.move()
demonstrate_polymorphism()

