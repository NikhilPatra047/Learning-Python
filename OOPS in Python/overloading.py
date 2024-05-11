class Point:
    __x = None
    __y = None

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

# Operator overloading - Method overloading - Polymorphism
    def __add__(self, other):
       print(f"{self.__x + other.__x} {self.__y + other.__y}")

    def __sub__(self, other):
        print(f"{self.__x - other.__x} {self.__y - other.__y}")

    def __eq__(self, other):
        return self.__x == other.__x and self.__y == other.__y

    def __str__(self):
        print(f"{self.__x} {self.__y}")

p1 = Point(10, 20)
p2 = Point(10, 20)
p1.__add__(p2)
p1.__sub__(p2)
print(p1.__eq__(p2))
p1.__str__()
