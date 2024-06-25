# Instructions
1. Open *main.py* and write the following code:

~~~python
def hello_world():
    print("Hello python")

def hello_name():
    name = input("Enter your name: ")
    print(f"Hello {name}.")

def numerical_input():
    number1 = int(input("Enter a number: "))
    number2 = int(input("Enter another number: "))
    print(f"The first number is {number1} the second number is {number2}")

def main():
    print("""
    1. Hello world.
    2. Hello name.
    3. Numerical input.
    """)
    option = int(input("Select an option: "))
    if option == 1:
        hello_world()
    elif option == 2:
        hello_name()
    elif option == 3:
        numerical_input()

if __name__ == "__main__":
    main()

~~~
2. Open a terminal and write the following
~~~shell
python -m main
~~~

The window should request an option between multiple options, and depending on the input it should do the requested task.