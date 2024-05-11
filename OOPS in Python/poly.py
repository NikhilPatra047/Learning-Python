# An example of Polymorphism (runtime) and inheritance

class Vehicle:
  name = None
  def __init__(self, name):
    self.name = name

  def start(self):
    print(f"{self.name} has started")

class Car(Vehicle):
  def __init__(self, name):
    Vehicle.__init__(self, name)

  def start(self):
    print(f"{self.name} has not started")

car = Vehicle("Camaro")
car.start()
