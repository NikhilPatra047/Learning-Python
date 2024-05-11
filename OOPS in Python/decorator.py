def new_decorator(func):
    def wrapper():
        print("Something is happening before the execution")
        func()
        print("Something is happening after the execution")
    return wrapper

@new_decorator
def say_hello():
    print("Hello World")

say_hello()

# Decorators in python are design patterns that allows developers to modify or extend the behaviour
# of a method without changing its source code. Decorators are functions themselves and they allow
# the execution of code before and after the wrapped function runs. The wrapped function can be removed altogether.
