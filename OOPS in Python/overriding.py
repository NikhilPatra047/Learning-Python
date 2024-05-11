class Animal:
    __name = None

    def __init__(self, name):
        self.__name = name

    def print_name(self):
        return self.__name

    def make_sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)

# Method overriding - a concept of runtime polymorphism
    def make_sound(self):
        name = self.print_name()
        print(f"{name} makes a sound")

dog = Dog("Murphy")
dog.make_sound()
