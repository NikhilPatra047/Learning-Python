def main():
    x = take_user_input()
    print("x squared is", square(x))

def take_user_input():
    x = int(input("What's x? "))
    return x

def square(n):
    return n * n

def hello(to="world"):
    return f"hello, {to}"

if __name__ == "__main__":
    main()
