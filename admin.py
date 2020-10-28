import json


from adminFunction import *


def show_admin_options():
    while True:
        print("0--> quit")
        print("1--> Add a new Company")
        print("2--> Add shares to specific Company")
        print("3--> Delete a Company")
        print("4--> Edit Shares,Number of shares and share Prices")
        print("5--> View Transaction reports")

        while True:
            try:
                option = int(input("Enter the Option--> "))
                break
            except:
                print("Please enter an integer value--> ")

        if(option == 1):
            addNewCompany()

        if(option == 2):
            addShareToCompany()

        if(option == 3):
            deleteACompany()

        if(option == 4):
            editSharesOrSharePrices()

        if(option == 5):
            fetchTransactions()

        if(option == 0):
            break
