import json
import time
import datetime


from userFunctions import *


def demat_details(accNo):
    while True:
        print("0  – Quit")
        print("1  – Display Demat account details")
        print("2  – Deposit Money")
        print("3  – Withdraw Money")
        print("4  – Buy transaction")
        print("5  – Sell transaction")
        print("6  – View transaction report")

        while True:
            try:
                option = int(input("Choose an option--> "))
                break
            except:
                print("Please Enter an integer Value")

        if(option == 1):
            display_demat_account_details(accNo)

        elif(option == 2):
            deposit_money(accNo)

        elif(option == 3):
            withdraw_money(accNo)

        elif(option == 4):
            buytransaction(accNo)

        elif(option == 5):
            selltransaction(accNo)

        elif(option == 6):
            ls = findUserNameByaccNo(int(accNo))
            tranRepoByCustomer(ls[0])

        elif(option == 0):
            break

        else:
            print("Wrong Choice Selected!")
