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
            userlist.append({"name": name, "account_number": account_number, "pin": first_pass})
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
            break
    else:
        print("Invalid account number or PIN.")

def forgot_password():
    login_account_number = input("Enter Account number: ")

    for user in userlist:
        if user["account_number"] == login_account_number:
            OTP = int(input("If you want to forgot password press 5: "))
            if OTP == 5:
                
                generated_otp = ''.join([str(r.randint(1, 9)) for _ in range(4)])
                print(f"Your OTP is {generated_otp}. It is valid for 30 seconds.")

                entered_otp =input("Enter the received OTP: ")

                if entered_otp == generated_otp:
                    new_pin = int(input("Enter new pin: "))
                    if any(user_item["pin"] == new_pin for user_item in userlist):
                        print("Pin already Exist :")
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
    login_account_number = input("Enter account number: ")
    login_pin = int(input("Enter your account PIN: "))

    for user in userlist:
        if user["account_number"] == login_account_number and user["pin"] == login_pin:
            print(f"User Information: {user}")
            break
    else:
        print("Invalid account number or PIN.")

while True:
    print("""Welcome to Python :
    1. Create an account :
    2. Log in :
    3. Forgot password By OTP :
    4. Show profile by providing old password :
    5. Exit""")

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
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Select a valid option.")
