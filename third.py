def main():
    number1 = int(input("Enter a number: "))
    number2 = int(input("Enter another number: "))
    print("-------------------------------------")
    print("""
          1. To sum the numbers
          2. To multiply the numbers
          3. To calculate the difference          
          """)
    option = int(input("Enter an option: "))
    if option == 1:
        print(f"The first number is {number1} the second number is {number2} and their sum is: {number1+number2}.")
    elif option == 2:
        print(f"The first number is {number1} the second number is {number2} and their product is: {number1*number2}.")
    elif option == 3:
        print(f"The first number is {number1} the second number is {number2} and their difference is: {number1-number2}.")

if __name__ == "__main__":
    main()
