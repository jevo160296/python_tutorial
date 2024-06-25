def request_numbers():
    number1 = int(input("Enter a number: "))
    number2 = int(input("Enter another number: "))
    return number1, number2

def print_menu(options):
    print("-------------------------------------")
    index = 1
    for option in options:
        print(f"{index}. {option}")
        index+=1

def request_option(cant):
    option = int(input("Enter an option: "))
    available = list(range(1,cant+1))
    if(option not in available):
        raise Exception(f"Wrong option {option}. Should be one of: {available}")
    return option

def menu(options):
    print_menu(options)
    option = request_option(len(options))
    return option

def handle_option(option, number1, number2):
    if option == 1:
        print(f"The first number is {number1} the second number is {number2} and their sum is: {number1+number2}.")
    elif option == 2:
        print(f"The first number is {number1} the second number is {number2} and their product is: {number1*number2}.")
    elif option == 3:
        print(f"The first number is {number1} the second number is {number2} and their difference is: {number1-number2}.")

def main():
    options = [
        "To sum the numbers",
        "To multiply the numbers",
        "To calculate the difference"
    ]
    (number1, number2) = request_numbers()
    print_menu(options)
    option = request_option(len(options))
    handle_option(option, number1, number2)

if __name__ == "__main__":
    main()
