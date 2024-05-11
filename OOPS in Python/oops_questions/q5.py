#Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.

class Vehicle:
    seating_capacity = 50
    name = None
    max_speed = None
    mileage = None

    def __init__(self, name, max_speed, mileage, seating_capacity = 50):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.seating_capacity = seating_capacity

    def print_seating_capacity(self):
        print(f"{self.name} has a seating capacity of {self.seating_capacity} members")

# Inheritance
class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage):
        Vehicle.__init__(self, name, max_speed, mileage)

def main():
    chevrolet = Bus("Chevvy", 100, 52)
    print(chevrolet.name)
    print(chevrolet.max_speed)
    print(chevrolet.mileage)
    print(chevrolet.seating_capacity)
    chevrolet.print_seating_capacity()

main()
