class Car: 
  runs = True 
  name = None 
  
  def __init__(self, name):
    self.name = name  
    print(f"{self.name} {self.runs}")
  
  # Non-static methods
  def start(self): 
    if self.runs: 
      print(f"{self.name} car has started")
    else: 
      print(f"{self.name} car has broken")

  @staticmethod 
  def add(n1, n2): 
    print(n1 + n2)
    
  @classmethod
  def printName(cls, name): 
    print(cls.name, name)

my_car = Car("Camaro")
my_car.start()
Car.add(1,2)
# Static methods don't necessarily require objects to call them 
Car.printName("Chevrolet")

print(isinstance(my_car, Car))

# Booleans are subclass of integers
# That's why when you check isinstance(1, bool) it returns false. 

