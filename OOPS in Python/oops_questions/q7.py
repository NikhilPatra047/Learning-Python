# Create a Bus child class that inherits from the Vehicle class.
# The default fare charge of any vehicle is seating capacity * 100.
# If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge.
# So total fare for bus instance will become the final amount = total fare + 10% of the total fare.
#

class Vehicle:
    def __init__(self, seating_capacity = 50):
        self.seating_capacity = seating_capacity

    def fare_charge(self):
        return float(self.seating_capacity * 100)

class Bus(Vehicle):
    def __init__(self, seating_capacity = 50):
       Vehicle.__init__(self, seating_capacity)

# Polymorphism
    def fare_charge(self):
        total_fare = self.seating_capacity * 100
        return float(total_fare + ((10 / 100) * total_fare))

def main():
    chevvy = Bus()
    result = chevvy.fare_charge()

    print(result)

main()

# Abstraction in python
# Polymorphism through function overloading and function overriding. There is no concept of virtual functions in Python.
# Inheritance - Done
# Encapsulation - Done
# Difference between static methods, class methods in Python
    # Static methods are belong to the class rather than any instance of the class
    # These can be called on the class itself or on an instance of a class
    # They are used to group together functions that have some logical connections and they don't change the state of an instance.
    # Don't take any argument that is a reference to the instance or the class itself.
    # Defined using the @staticmethod decorator

    # Class Methods are bound to the class and not to an object.
    # These can be called on the class itself, or an instance of a class.
    # These methods can affect the state of a class but not an instance.
    # Takes a reference to the class as an argument.
    # Defined using the @classmethod decorator

    # Non-static methods are bound to an instance of a class.
    # These can be called on the class itself or an instance of a class.
    # These methods can affect the state of an instance
    # Takes a reference to the object as its first argument.
    # Doesn't require any decorator
# What is a decorator in Python?
