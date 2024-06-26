from third import menu
from functions import (modify_amount, create_user, print_amount, check_amoount, change_password, login)
from functions import (ATMException)
import os

def main(username, password):
    finish = False
    if (username == None) or (password == None):
        finish, username, password = main_menu()
    else:
        username, password = logged_in_menu(username, password)
    return finish, username, password

def main_menu():
    options = [
        "Sign in",
        "Sign up",
        "Exit"
    ]
    option = menu(options)
    if option == 1:
        username = input("Username: ")
        password = input("Password: ")
        login(username, password)
        return False, username, password
    elif option == 2:
        username = input("Username: ")
        password = input("Password: ")
        create_user(username, password)
        return False, username, password
    elif option == 3:
        return True, None, None

def logged_in_menu(username, password):
    options = [
        "Withdraw money",
        "Add money",
        "Check account",
        "Change password",
        "Log out"
    ]
    print(f"Hi {username}")
    option = menu(options)
    if option == 1:
        amount = -int(input("Amount: "))
        modify_amount(username, password, amount)
        current_amount = check_amoount(username, password)
        print_amount(username, current_amount)
        input("Press any key to continue.")
    elif option == 2:
        amount = int(input("Amount: "))
        modify_amount(username, password, amount)
        current_amount = check_amoount(username, password)
        print_amount(username, current_amount)
        input("Press any key to continue.")
    elif option == 3:
        current_amount = check_amoount(username, password)
        print_amount(username, current_amount)
        input("Press any key to continue.")
    elif option == 4:
        password = input("Current password: ")
        new_password = input("New password: ")
        change_password(username, password, new_password)
    elif option == 5:
        username = None
        password = None
    return username, password

if __name__ == "__main__":
    finish = False
    username = None
    password = None
    while(not finish):
        try:
            finish, username, password = main(username, password)
            os.system('cls||clear')
        except ATMException as e:
            print(f"ATM Error: {e.value}")
        except ValueError as e:
            print(f"Value error, please select a valid option.")
            print(e)

