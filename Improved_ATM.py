
import random

database = {}

# Initialising Function
def main():
    welcome_prompt()
    is_valid = False
    while is_valid == False:
        choice = int(input("Do you have an account? Enter 1 for yes, 2 for no: "))

        if choice == 1:
            is_valid = True
            login()
        elif choice == 2:
            is_valid = True
            register()
        else:
            print("Invalid option entered, please try again.")


# Welcome Message
def welcome_prompt():
    print("Welcome to Trusted Bank!")
    print()


# Login Function
def login():
    print("---Login---")
    is_successful = False
    while is_successful == False:

        user_account_number =int(input("Enter your account number: "))
        password = input("Enter your password: ")

        for account_number, user_details in database.items():
            if account_number == user_account_number:
                if user_details[3] == password:
                    is_successful = True

    print("Invalid account number or password.")
    print("Please try again.")
    bank_operations(user_details)


# Register function
def register():
    first_name = input("Enter your first name: ")
    last_name = input ("Enter your last name: ")
    email = input("Enter your email address: ")
    password = input("Please create a password: ")
    balance = int(input("Deposit a starting balance: "))

    account_number = gen_account_no()
    database[account_number] = [first_name, last_name, email, password, balance]
    
    print("Registration Successful")
    print("Here is your account number: ", account_number)
    login()


# General banking operations
def bank_operations(user):
    print("Welcome %s  %s" % (user[0], user[1]))
    print("Options")
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Make a complaint")
    print("4. Logout")
    print("5. Exit")

    is_valid = False
    while is_valid == False:
        option = int(input("Select an option: "))

        if option == 1:
            is_valid == True
            withdraw(user)
        elif option == 2:
            is_valid == True
            deposit(user)
        elif option == 3:
            is_valid == True
            complaint(user)
        elif option == 4:
            is_valid == True
            logout()
        elif option == 5:
            is_valid == True
            exit()
        else:
            print("Error!")
            print("Invalid option selected, please try again.")


# Withdrawal Function
def withdraw(user):
    balance = get_balance(user)
    debit = int(input("How much do you want to withdraw: "))
    if balance > debit:
        balance -= debit
        print("Your current balance is", balance)
    else:
        print("Insufficient funds.")


# Deposit Function
def deposit(user):
    balance = get_balance(user)
    credit = int(input("How much do you want to deposit: "))
    balance += credit
    print("Your current balance is", balance)


# Complaint function
def complaint(issue):
    issue = input("What issue would you like to report?: ")
    print("Your complaint has been registered.")


# Account number generator
def gen_account_no():
    return random.randrange(1111111111,9999999999)


# Current balance Function
def get_balance(user_details):
    return user_details[4]


# Logout function
def logout():
    login()


main()
