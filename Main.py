from bank_admin import change_tax_rates
from user import demat_details
from DematAccountCreation import demat_creation
from auth import bank_admin_login
from auth import demat_login
from auth import admin_login
from admin import show_admin_options



print("Demat Account Project")
option = 1
while(option != 0):
    print("1 -> You're a User")
    print("2 -> You're an Admin")
    print("3 -> You're Bank Admin")
    print("0--> Exit the Application")

    option = int(input("Enter Your Choice --> "))

    if (option == 1):
        print("1--> Create a Demat Account")
        print("2--> Already have a Demat Account")
        choice = int(input("Enter your Choice--> "))
        if(choice == 1):
            demat_creation()
        elif(choice == 2):
            accNo = input("Enter Account Number--> ")
            password = input("Enter Your Password--> ")

            loginSuccess = demat_login(accNo, password)
            if(loginSuccess):
                demat_details(accNo)
            else:
                print("Account Number or Password is incorrect!")

        else:
            print("You have Entered a Wrong Choice")

    elif(option == 2):
        print("Enter your Credentials--> ")
        username = input("Enter the username--> ")
        password = input("Enter the password--> ")

        adminloginSuccess = admin_login(username, password)
        if(True):
            show_admin_options()
        else:
            print("Username or password is incorrect!")

    elif(option == 3):
        print("Enter your Credentials--> ")
        username = input("Enter the username--> ")
        password = input("Enter the password--> ")
        bankadminloginSuccess = bank_admin_login(username, password)
        if True:
            change_tax_rates()
        else:
            print("Username or password is incorrect!")

    elif(option == 0):
        break
    else:
        print("You have chosen a wrong option")
