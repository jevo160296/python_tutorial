# Instructions
1. Open *main.py* and write the following code:

~~~python
def main():
    number1 = int(input("Enter a number: "))
    number2 = int(input("Enter another number: "))
    print(f"The first number is {number1} the second number is {number2}")

if __name__ == "__main__":
    main()

~~~

2. Open a terminal and write the following
~~~shell
python -m main
~~~

The window should be requesting two numbers, enter the two numbers and hit enter, you should see the following

~~~shell
Enter a number: {number1}
Enter another number: {number2}
The first number is {number1} the second number is {number2}
~~~