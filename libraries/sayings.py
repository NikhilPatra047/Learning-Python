def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"Hello, {name}")

def goodbye(name):
    print(f"Goodbye, {name}")

# Main function now will be executed if and only if the name of the module is main
#
if __name__ == "__main__":
    main()
