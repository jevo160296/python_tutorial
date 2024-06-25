users = {}
attempts = {}
amounts = {}

class ATMException(Exception):
    def __init__(self, value) -> None:
        super().__init__(value)
        self.value = value

class UserDontExistException(ATMException):
    def __init__(self, username: str) -> None:
        super().__init__(f"Username {username} don't exist.")

class UserExistException(ATMException):
    def __init__(self, username: str) -> None:
        super().__init__(f"Username {username} already exists.")

class WrongPasswordException(ATMException):
    def __init__(self, remaining_attemps: int) -> None:
        super().__init__(f"Password incorrect, try again. Remaining attemps: {remaining_attemps}")

class LockedUserException(ATMException):
    def __init__(self) -> None:
        super().__init__(f"User is locked, max login attempts reached. Contact administrator.")

class LoginError(ATMException):
    def __init__(self) -> None:
        super().__init__("Cannot log in.")

class WithdrawException(ATMException):
    def __init__(self, amount, current_amount) -> None:
        super().__init__(f"Cannot withdraw {amount}. Account only have {current_amount}.")

def create_user(username, password):
    if(username not in users):
        users[username] = password
    else:
        raise UserExistException(username)
    
def login(username, password):
    if(username not in users):
        raise UserDontExistException(username)
    if(password != users[username] and attempts.setdefault(username, 0) < 3):
        attempts[username] = attempts.setdefault(username, 0) + 1
        raise WrongPasswordException(3 - attempts[username])
    if(password != users[username] and attempts.setdefault(username, 0) >= 3):
        raise LockedUserException()
    if(password == users[username]):
        attempts[username] = 0
        return True
    else:
        return False

def modify_amount(username, password, amount):
    is_loggedin = login(username, password)
    if not is_loggedin:
        raise LoginError()
    current_amount = amounts.setdefault(username, 0)
    if(amount + current_amount < 0):
        raise WithdrawException(amount, current_amount)
    amounts[username] = current_amount + amount
    return True

def check_amoount(username, password):
    is_loggedin = login(username, password)
    if not is_loggedin:
        raise LoginError()
    current_amount = amounts.setdefault(username, 0)
    return current_amount

def print_amount(username, amount):
    print(f"User {username} has {amount} in its account.")

def change_password(username, password, new_password):
    is_loggedin = login(username, password)
    if not is_loggedin:
        raise LoginError()
    users[username] = new_password
    return True