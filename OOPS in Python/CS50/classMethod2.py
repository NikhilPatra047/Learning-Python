class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} is in {self.house}"

    @classmethod
    def get(cls):
        name = input("Enter your name: ")
        house = input("Enter your house: ")
        return cls(name, house)
        # The above line creates an instance of the class using the cls() method that takes in the name and house as input.

def main():
    student = Student.get()
    print(student)

if __name__ == "__main__":
    main()
