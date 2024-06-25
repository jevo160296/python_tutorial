# Instructions
The final goal is to write a program that acts as an ATM, the main functions should include:

1. Request a username and a password.
2. If the password you enter is wrong three times, your account will be blocked.
3. You can add or withdraw money.
4. You can change your password.
5. You can check how much do you have in your account.

This will be solved dividing the whole problem in many tiny problems as follow:

1. Build a function that accepts two arguments: *username*, *password* and saves in a dictionary the username and password.
2. Build a function that accepts two arguments: *username*, *password* and returns a Boolean value (True or False) indicating if the password is correct for the specified user.
    2.1 Modify the function to count how many wrong attempts has been made for every user and returns an error if the number of attempts is greater than 3.
    2.3 Modify the function to return a Password error if the password is wrong, and a username doesn't exist if the username hasn't been created yet.
3. Build a function that accepts three arguments: *username*, *password*, *amount* and returns a Boolean value (True or False) if the money can be withdrawn.
4. Build a function that accepts three arguments: *username*, *password* and returns how many does the user have in its account.
5. Build a function that accepts three arguments: *username*, *password*, *newpassword* and returns a Boolean value indicating if the password was changed successfully.
6. Merge all the functions to build the ATM.
