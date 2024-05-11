# A demonstration of inheritance in OOPs using Python
class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

    @classmethod
    def get_name(cls, inheritor_name):
        name = input(f"Enter {inheritor_name} name: ")
        return name

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name) # super() represents the parent class. In this case, the Wizard class.
        self.house = house

    def __str__(self):
        return f"{self.name} is in {self.house}"

    @classmethod
    def get(cls):
        name = super().get_name("student's")
        house = input("Enter student's house: ")
        return cls(name, house)

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name) # super() represents the parent class. In this case, the Wizard class.
        self.subject = subject

    def __str__(self):
        return f"{self.name} teaches {self.subject}"

    @classmethod
    def get(cls):
        name = super().get_name("professor's")
        subject = input("Enter professor's subject: ")
        return cls(name, subject)

def main():
    student = Student.get()
    professor = Professor.get()

    print(professor)
    print(student)

main()
