# Write a Python program to create a class representing a shopping cart.
# Include methods for adding and removing items, and calculating the total price.

# items - list of items

class shopping_cart:
    cart = {}

    def __init__(self):
        self.cart = {}

    def add_items(self, item, price):
        if not item in self.cart:
            self.cart[item] = 1 * price
        else:
            self.cart[item] += price

    def remove_items(self, item, price):
        if not item in self.cart:
            print("Item doesn't exist")
        else:
            self.cart[item] -= price
            if self.cart[item] == 0:
                del self.cart[item]

    def calc_total(self):
        sum = 0
        for price in self.cart.values():
            sum += price
        print(f"Total price = {sum}")

    def show_cart(self):
        print(f"{self.cart}")

def main():
    item_list = {
        "1": 20,
        "2": 30,
        "3": 40,
        "4": 50,
        "5": 100
    }

    cart = shopping_cart()
    select = input("Enter a number from 1-4: 1: add an item, 2: remove an item, 3: calculate total, 4: show cart \n")
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
                product = input("Enter a product id \n")
                if product in item_list:
                    cart.add_items(product, item_list[product])
                else:
                    print("Wrong product id")
            case 2:
                product = input("Enter a product id \n")
                if product in item_list:
                    cart.remove_items(product, item_list[product])
                else:
                    print("Wrong product id")
            case 3:
                cart.calc_total()
            case 4:
                cart.show_cart()
            case default:
                print("Wrong choice!")

        select = input("Enter a number from 1-4: 1: add an item, 2: remove an item, 3: calculate total, 4: show cart \n")
        if not select.isdigit():
            print("Wrong choice!")
            return
        elif select.isdigit() and int(select) > 4 or int(select) < 1:
            print("Wrong choice!")
            return

        select = int(select)

main()
