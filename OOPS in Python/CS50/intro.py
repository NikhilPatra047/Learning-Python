def main():
    (name, house) = get_student()
    print(f"{name} from {house}")

# Introducing Abstraction
def get_student():
    name = get_name()
    house = get_house()
    return (name, house)

def get_name():
    return input("Enter your name \n")

def get_house():
    return input("Enter your house \n")

if __name__ == "__main__":
    main()
