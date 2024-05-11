# Define a property that must have the same value for every class instance (object)
#

class Student:
    name = None
    age = None
    stream = "Science"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(f"{self.name}, age {self.age}, belongs to the stream of {self.stream}")

def main():
    student = Student("Nikhil", 24)
    student.print_info()

main()
