# Animal or Vehicle classes with polymorphism
class Car:
    def move(self):
        print("Driving 🚗")

class Plane:
    def move(self):
        print("Flying ✈️")

# Function to demonstrate polymorphism
def demonstrate_move(vehicle):
    vehicle.move()

# Creating objects
car = Car()
plane = Plane()

# Demonstrating polymorphism
demonstrate_move(car)   # Output: Driving 🚗
demonstrate_move(plane) # Output: Flying ✈️
