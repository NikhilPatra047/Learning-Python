# Write a Python program to create a calculator class.
# Include methods for basic arithmetic operations.
#

class calculator:
    def __add__(self, x, y):
        print(x + y)

    def __sub__(self, x, y):
        print(x - y)

    def __mul__(self, x, y):
        print(x * y)

    def __div__(self, x, y):
        print(x / y)

def take_user_input():
    x = input("Enter a number \n")
    y = input("Enter another number \n")
    return x, y

def check_for_correct_input(x, y):
    if x.isdigit() and y.isdigit():
        return True
    else:
        return False

def main():
    calc = calculator()
    select = input("Enter 1-4: 1: addition, 2: subtraction, 3: multiplication, 4: division \n")

    if not select.isdigit():
        print("Wrong choice!")
        return
    elif select.isdigit() and int(select) > 4 or int(select) < 1:
        print("Wrong choice!")
        return

    select = int(select)
    while select in range(1, 5):
        match select:
            case 1:
                x, y = take_user_input()
                is_correct = check_for_correct_input(x, y)
                if is_correct:
                    x = int(x)
                    y = int(y)
                    calc.__add__(x, y)
                else:
                    print("Wrong input!")
            case 2:
                x, y = take_user_input()
                is_correct = check_for_correct_input(x, y)
                if is_correct:
                    x = int(x)
                    y = int(y)
                    calc.__sub__(x, y)
                else:
                    print("Wrong input!")
            case 3:
                x, y = take_user_input()
                is_correct = check_for_correct_input(x, y)
                if is_correct:
                    x = int(x)
                    y = int(y)
                    calc.__mul__(x, y)
                else:
                    print("Wrong input!")
            case 4:
                x, y = take_user_input()
                is_correct = check_for_correct_input(x, y)
                if is_correct:
                    x = int(x)
                    y = int(y)
                    calc.__div__(x, y)
                else:
                    print("Wrong input!")
            case default:
                print("Wrong choice!")

        select = input("Enter 1-4: 1: addition, 2: subtraction, 3: multiplication, 4: division \n")
        if not select.isdigit():
            print("Wrong choice!")
            return
        elif select.isdigit() and int(select) > 4 or int(select) < 1:
            print("Wrong choice!")
            return

        select = int(select)

main()
