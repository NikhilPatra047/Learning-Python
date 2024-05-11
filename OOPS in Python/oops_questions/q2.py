#Write a Python program to create a class representing a bank.
#Include methods for managing customer accounts and transactions


# What are the features in a bank.
# Account - Savings or current
# add amount
# withdraw amount
# delete account

class Bank:
    account = {}

    def __init__(self):
        self.account = {}

    def create_account(self, acc_num, init_bal):
        if acc_num in self.account:
            print("Account number already exists")
            return
        else:
            self.account[acc_num] = init_bal
            print("Account created")
            return

    def delete_account(self, acc_num):
        if not acc_num in self.account:
            print("Account number doesn't exist")
            return
        else:
            del self.account[acc_num]
            print("Account successfully deleted")

    def add_amount(self, acc_num, amount):
        self.account[acc_num] += amount
        print("Amount added")
        return

    def withdraw(self, acc_num, amount):
        self.account[acc_num] -= amount
        print(f"{amount} withdrawn from the account {acc_num}")
        return

    def check_balance(self, acc_num):
        print(f"{self.account[acc_num]} is your bank balance. Thank you.")

def main():
    account = Bank()
    select = input("Enter a number from 1-5: 1: Create account, 2: Add account, 3: Withdraw amount, 4: Delete account, 5: Check balance \n")
    if not select.isdigit():
        print("Wrong Selection!")
        return
    elif select.isdigit() and int(select) > 5:
        print("Wrong Selection!")
        return

    select = int(select)
    while select in range(1, 6):
        match select:
            case 1:
                acc_num = input("Enter an account number \n")
                init_bal = int(input("Enter the initial balance amount \n"))
                account.create_account(acc_num, init_bal)

            case 2:
                acc_num = input("Enter an account number \n")
                if not acc_num in account.account:
                    print("Account number not found")
                else:
                    amount = int(input("Enter the amount you want to add \n"))
                    account.add_amount(acc_num, amount)

            case 3:
                acc_num = input("Enter an account number \n")
                if not acc_num in account.account:
                    print("Account number not found")
                else:
                    amount = int(input("Enter the amount you want to withdraw \n"))
                    account.withdraw(acc_num, amount)

            case 4:
                acc_num = input("Enter an account number \n")
                account.delete_account(acc_num)

            case 5:
                acc_num = input("Enter an account number \n")
                if acc_num in account.account:
                    account.check_balance(acc_num)
                else:
                    print("Account doesn't exist")

            case default:
                print("Wrong selection!")

        select = input("Enter a number from 1-5: 1: Create account, 2: Add account, 3: Withdraw amount, 4: Delete account, 5: Check balance \n")
        if not select.isdigit():
            print("Wrong selection!")
            break
        elif select.isdigit() and int(select) > 5:
            print("Wrong Selection!")
            break
        select = int(select)
    return

main()
