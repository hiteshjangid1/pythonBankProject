import json



def addNewCompany():
    company_name = input("Enter the Company Name--> ")
    f = open("company.txt", "r")
    x = f.read()
    if(len(x) != 0):
        f.seek(0)
        company_list = json.load(f)
    else:
        company_list = {}
    if(company_name.title() in company_list):
        print("Company is already Listed!")
    else:
        flag = 1
        ls = []
        while(flag == 1):
            share_name = input("Enter Name of Share-->")
            share_number = int(input("Enter Number of Shares--> "))
            share_price = int(input("Enter Share Price--> "))
            ls.append([share_name.lower(), share_number, share_price])
            flag = int(
                input("Enter 1 to add one more otherwise add 0--> "))
        company_list[company_name.title()] = ls
        f = open("company.txt", "w")
        json.dump(company_list, f)
        f.close()


def addShareToCompany():
    company_name = input("Enter the Company Name--> ")
    f = open("company.txt", "r")
    x = f.read()
    if(len(x) != 0):
        f.seek(0)
        company_list = json.load(f)
        f.close()
        if(company_name.title() in company_list):
            ls = company_list[company_name.title()]
            flag = 1
            while(flag == 1):
                share_name = input("Enter Name of Share-->")
                share_number = int(input("Enter Number of Shares--> "))
                share_price = int(input("Enter Share Price--> "))
                ls.append([share_name.lower(), share_number, share_price])
                flag = int(
                    input("Enter 1 to add one more otherwise add 0--> "))
            f = open("company.txt", mode="w")
            json.dump(company_list, f)
            f.close()
    else:
        print("Company Does Not Exist!")


def deleteACompany():
    company_name = input("Enter the Company Name--> ")
    f = open("company.txt", "r")
    x = f.read()
    if(len(x) != 0):
        f.seek(0)
        company_list = json.load(f)
        f.close()
    if(company_name.title() in company_list):
        del company_list[company_name.title()]
        f = open("company.txt", mode="w")
        json.dump(company_list, f)
        f.close()
        print("Company "+company_name.title()+" Deleted Successfully!")
    else:
        print("Company Does Not Exist!")


def editSharesOrSharePrices():
    add_more = 1
    while(add_more == 1):
        company_name = input("Enter the Company Name--> ")
        f = open("company.txt", "r")
        x = f.read()
        if(len(x) != 0):
            f.seek(0)
            company_list = json.load(f)
            f.close()
            if(company_name.title() in company_list):
                share_name = input("Enter the Share Name--> ")
                ls = company_list[company_name.title()]
                for x in ls:
                    cx = 1
                    if(x[0] == share_name.lower()):
                        share_name = input("Enter Share Name to Change--> ")
                        share_number = int(
                            input("Enter Share Value to Change--> "))
                        share_price = int(
                            input("Enter Share Price to Change--> "))
                        ls.remove(x)
                        ls.append([share_name, share_number, share_price])
                        cx = 0
                        f = open("company.txt", mode="w")
                        json.dump(company_list, f)
                        f.close()
                        break
                if(cx == 1):
                    print("Share Not Found!")
        else:
            print("Company Does Not Exist!")
        add_more = int(
            input("Enter 1 to edit more Shares else Enter 0--> "))


def tranReportByCustomer():
    customer = input("Please Enter name of the Customer--> ")
    f = open("transaction.txt", mode="r")
    data = f.read()
    if(len(data) != 0):
        f.seek(0)
        trans = json.load(f)
        f.close()
        flag = 1
        print(
            "SHAREAMOUNT-BANKACCOUNT-COMPANY-SHARENAME-DATE-AMOUNT-TIME-PERSON-(BUY/SELL)")
        for x in trans:
            if(x[7] == customer.title()):
                flag = 0
                print(x)
        if(flag == 1):
            print("No data Found")


def tranReportByCompany():
    company = input("Please Enter name of the Company--> ")
    f = open("transaction.txt", mode="r")
    data = f.read()
    if(len(data) != 0):
        f.seek(0)
        trans = json.load(f)
        f.close()
        flag = 1
        print(
            "SHAREAMOUNT-BANKACCOUNT-COMPANY-SHARENAME-DATE-AMOUNT-TIME-PERSON-(BUY/SELL)")
        for x in trans:
            if(x[2] == company.title()):
                flag = 0
                print(x)
        if(flag == 1):
            print("No data Found")


def tranReportByDate():
    date = input("Please Date (yyyy-mm-dd) format--> ")
    f = open("transaction.txt", mode="r")
    data = f.read()
    if(len(data) != 0):
        f.seek(0)
        trans = json.load(f)
        f.close()
        flag = 1
        print(
            "SHAREAMOUNT-BANKACCOUNT-COMPANY-SHARENAME-DATE-AMOUNT-TIME-PERSON-(BUY/SELL)")
        for x in trans:
            if(x[4] == date):
                flag = 0
                print(x)
        if(flag == 1):
            print("No data Found")


def tranReportByDateAndCompany():
    date = input("Please Date (yyyy-mm-dd) format--> ")
    company = input("Please Enter name of the Company--> ")
    f = open("transaction.txt", mode="r")
    data = f.read()
    if(len(data) != 0):
        f.seek(0)
        trans = json.load(f)
        f.close()
        flag = 1
        print(
            "SHAREAMOUNT-BANKACCOUNT-COMPANY-SHARENAME-DATE-AMOUNT-TIME-PERSON-(BUY/SELL)")
        for x in trans:
            if(x[4] == date and x[2] == company.title()):
                flag = 0
                print(x)
        if(flag == 1):
            print("No data Found")


def tranReportByDateAndCustomer():
    date = input("Please Date (yyyy-mm-dd) format--> ")
    customer = input("Please Enter name of the Customer--> ")
    f = open("transaction.txt", mode="r")
    data = f.read()
    if(len(data) != 0):
        f.seek(0)
        trans = json.load(f)
        f.close()
        flag = 1
        print(
            "SHAREAMOUNT-BANKACCOUNT-COMPANY-SHARENAME-DATE-AMOUNT-TIME-PERSON-(BUY/SELL)")
        for x in trans:
            if(x[4] == date and x[7] == customer.title()):
                flag = 0
                print(x)
        if(flag == 1):
            print("No data Found")


def fetchTransactions():
    print("1--> By customer")
    print("2--> By company")
    print("3--> By dates of all company")
    print("4--> By dates of a specific company")
    print("5--> By dates of a specific customer ")

    while True:
        try:
            option = int(input("Enter Your Choice--> "))
            break
        except:
            print("Please enter an integer value")

    if(option == 1):
        tranReportByCustomer()

    if(option == 2):
        tranReportByCompany()

    if(option == 3):
        tranReportByDate()

    if(option == 4):
        tranReportByDateAndCompany()

    if(option == 5):
        tranReportByDateAndCustomer()
