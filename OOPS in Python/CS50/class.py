class Student:
    name = ""
    house = ""

    @staticmethod
    def get_student():
        name = input("Enter your name: \n")
        house = input("Enter your house: \n")

        student = Student(name, house)
        student.house = "Ravenclaw"
        print(student)
        print(student.__repr__())

    def __init__(self, name, house):
        self.name = name
        self.house = house

# Overloading the string method in Python to return the object as a string
    def __str__(self):
        return f"{self.name} from {self.house}"

    def __repr__(self):
        return f"{isinstance(self, Student)} and {type(self.name) == str} and {type(self.house) == str}"
    # repr - representation of an object.
    # Meant for developers
    #
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        else:
            self._name = name

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if not house in ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]:
            raise ValueError("Invalid House")
        else:
            self._house = house

def main():
    Student.get_student()

if __name__ == "__main__":
    main()

# Class is a blueprint or representation of all the attributes and methods that are going defined on the instance of the class when it is created.
# Instance variable - _house
# Attribute - house
