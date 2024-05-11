# Example of class methods

class my_class:
    class_var = 0
    def __init__(self, value):
        self.value = value

    @classmethod
    def increment_class_var(cls, amount):
        cls.class_var += amount

    @classmethod
    def default_value(cls):
        return cls(100)

obj = my_class(10)
obj1 = my_class(20)

obj2 = my_class.default_value()

my_class.increment_class_var(30)
print(obj.value, obj1.value, my_class.class_var, obj2.value)
