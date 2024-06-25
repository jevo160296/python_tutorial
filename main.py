from third import menu
from functions import (modify_amount, create_user, print_amount, check_amoount, change_password)
from functions import (ATMException)
import os

def main():
    options = [
        "Withdraw money",
        "Add money",
        "Check account",
        "Change password",
        "Create account"
    ]
    option = menu(options)
    if option == 1:
        username = input("Username: ")
        password = input("Password: ")
        amount = -int(input("Amount: "))
        modify_amount(username, password, amount)
    elif option == 2:
        username = input("Username: ")
        password = input("Password: ")
        amount = int(input("Amount: "))
        modify_amount(username, password, amount)
    elif option == 3:
        username = input("Username: ")
        password = input("Password: ")
        current_amount = check_amoount(username, password)
        print_amount(username, current_amount)
        input("Press any key to continue.")
    elif option == 4:
        username = input("Username: ")
        password = input("Password: ")
        new_password = input("New password: ")
        change_password(username, password, new_password)
    elif option == 5:
        username = input("Username: ")
        password = input("Password: ")
        create_user(username, password)


if __name__ == "__main__":
    while(True):
        try:
            main()
            os.system('cls||clear')
        except ATMException as e:
            print(f"ATM Error: {e.value}")

