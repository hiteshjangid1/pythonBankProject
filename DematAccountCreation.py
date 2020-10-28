import random
import json



def demat_creation():
    acc_No = int(random.randrange(1111111111, 9999999999))
    name = input("Enter Your Name--> ")
    user_name = input("Enter the User Name--> ")
    balance = 0
    while(balance < 3000):
        print("Initial Balance must be greater than or equal to 3000")
        balance = int(input("Enter Initial Balance Amount--> "))
    option = False
    while(option == False):
        print("Both Passwords Should be Same")
        password1 = input("Enter your Password--> ")
        password2 = input("ReEnter the Password--> ")
        if(password1 == password2):
            option = True
    f = open("DematAccounts.txt", mode="r")
    accounts = json.load(f)
    f.close()
    f = open("DematAccounts.txt", mode="w")
    accounts[user_name] = [acc_No, name.title(), balance, password1]
    json.dump(accounts, f)
    print("Demat Account Created for "+name+" and account no. is "+str(acc_No))
    f.close()


# demat_creation()
