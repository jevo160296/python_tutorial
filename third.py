def request_numbers():
    number1 = int(input("Enter a number: "))
    number2 = int(input("Enter another number: "))
    return number1, number2

def print_menu():
    print("-------------------------------------")
    print("""
          1. To sum the numbers
          2. To multiply the numbers
          3. To calculate the difference          
          """)

def request_option():
    option = int(input("Enter an option: "))
    return option

def handle_option(option, number1, number2):
    if option == 1:
        print(f"The first number is {number1} the second number is {number2} and their sum is: {number1+number2}.")
    elif option == 2:
        print(f"The first number is {number1} the second number is {number2} and their product is: {number1*number2}.")
    elif option == 3:
        print(f"The first number is {number1} the second number is {number2} and their difference is: {number1-number2}.")

def main():
    (number1, number2) = request_numbers()
    print_menu()
    option = request_option()
    handle_option(option, number1, number2)

if __name__ == "__main__":
    main()
