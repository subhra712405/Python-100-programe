import random as r
import time

user_file = "user_data.txt"

try:
    with open(user_file, "r") as file:
        userlist = eval(file.read())
except FileNotFoundError:
    userlist = []

def save_user_data():
    with open(user_file, "w") as file:
        file.write(str(userlist))

def account_creation():
    name = str(input("Enter your Name: "))
    account_number = ''.join([str(r.randint(0, 9)) for _ in range(10)])
    print(f"Your account number is {account_number}")

    first_pass = int(input("Enter 4 digit new pin (only 2 attempts): "))
    second_pass = int(input("Confirm the password (only 2 attempts): "))

    if first_pass == second_pass:
        if any(user["pin"] == first_pass for user in userlist):
            print("Error: This pin is already in use. Please choose a different one.")
        else:
            userlist.append({
                "name": name,
                "account_number": account_number,
                "pin": first_pass,
                "balance": 0  # initial balance
            })
            print(f"Your pin is {first_pass}")
            print("Your account created successfully")
            save_user_data()
    else:
        print("Reenter your pin.")

def login():
    login_account_number = input("Enter your account number: ")
    login_pin = int(input("Enter your account PIN: "))

    for user in userlist:
        if user["account_number"] == login_account_number and user["pin"] == login_pin:
            print("You are successfully logged in.")
            return user
    print("Invalid account number or PIN.")
    return None

def forgot_password():
    login_account_number = input("Enter Account number: ")

    for user in userlist:
        if user["account_number"] == login_account_number:
            OTP = int(input("If you want to forgot password press 5: "))
            if OTP == 5:
                generated_otp = ''.join([str(r.randint(1, 9)) for _ in range(4)])
                print(f"Your OTP is {generated_otp}. It is valid for 30 seconds.")

                entered_otp = input("Enter the received OTP: ")

                if entered_otp == generated_otp:
                    new_pin = int(input("Enter new pin: "))
                    if any(user_item["pin"] == new_pin for user_item in userlist):
                        print("Pin already exists.")
                    else:
                        user["pin"] = new_pin
                        print("Your pin has been updated.")
                        save_user_data()
                else:
                    print("Invalid OTP.")
            else:
                print("Invalid choice.")
            break
    else:
        print("Invalid account number.")

def show_profile():
    user = login()
    if user:
        print(f"User Information:\nName: {user['name']}\nAccount: {user['account_number']}\nBalance: {user['balance']}")

# -----------------------
# New Features
# -----------------------
def credit_money():
    user = login()
    if user:
        amount = float(input("Enter amount to deposit: "))
        user["balance"] += amount
        print(f"₹{amount} credited successfully. Current balance: ₹{user['balance']}")
        save_user_data()

def withdraw_money():
    user = login()
    if user:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= user["balance"]:
            user["balance"] -= amount
            print(f"₹{amount} withdrawn successfully. Current balance: ₹{user['balance']}")
            save_user_data()
        else:
            print("Insufficient balance.")

def check_balance():
    user = login()
    if user:
        print(f"Your current balance is: ₹{user['balance']}")

# -----------------------
# Menu
# -----------------------
while True:
    print("""
Welcome to Python Banking System:
    1. Create an account
    2. Log in
    3. Forgot password (via OTP)
    4. Show profile
    5. Credit money (Deposit)
    6. Withdraw money
    7. Check balance
    8. Exit
    """)

    choice = int(input("Enter your choice: "))
    if choice == 1:
        account_creation()
    elif choice == 2:
        login()
    elif choice == 3:
        forgot_password()
    elif choice == 4:
        show_profile()
    elif choice == 5:
        credit_money()
    elif choice == 6:
        withdraw_money()
    elif choice == 7:
        check_balance()
    elif choice == 8:
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Select a valid option.")
