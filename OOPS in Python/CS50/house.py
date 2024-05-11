class Student:
    _name = ""
    _house = ""
    classVar = "Hello World"

    def __init__(self, name, house):
        self.name = name
        self.house = house

# property is name but the instance variable is _name
# There is no notion of access specifiers in Python
# _ represents a protected variable
# __ represents a private variable

    @property
    def name(self):
        return self._name

    @property
    def house(self):
        return self._house

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        else:
            self._name = name

    @house.setter
    def house(self, house):
        if not house in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        else:
            self._house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    def __repr__(self):
        return f"{isinstance(self, Student)} {type(self.name) == str} {type(self.house) == str}"

    @staticmethod
    def get_student():
        name = input("Enter your name \n")
        house = input("Enter your house \n")

        student = Student(name, house)
        print(student.__str__())
        print(student.__repr__())

    @classmethod
    def hello_world(cls):
       return cls.classVar

def main():
    # Student.get_student()
    # print(Student.hello_world())
    new_dict = dict([('a', 1), ('b', 2), ('c', 3)])
    print(new_dict)

if __name__ == "__main__":
    main()


    # int, float, boolean, string, dictionary, list, set, frozenset, tuple, range, None
