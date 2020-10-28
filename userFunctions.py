import json
import time
import datetime



def findUserNameByaccNo(accNo):
    f = open("DematAccounts.txt", mode="r")
    acc = f.read()
    if(len(acc) != 0):
        f.seek(0)
        accounts = json.load(f)
        f.close()
        flag = 1
        for x, y in accounts.items():
            if(y[0] == accNo):
                flag = 0
                return [y[1], y[2], x]
        return []
    else:
        return []


def tranRepoByCustomer(customer):
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


def auto_deposit_money(accNo, amount):
    f = open("DematAccounts.txt", mode="r")
    acc = f.read()
    if(len(acc) != 0):
        f.seek(0)
        accounts = json.load(f)
        f.close()
        flag = 1
        for x, y in accounts.items():
            if(y[0] == int(accNo)):
                y[2] = y[2]+amount
                flag = 0
                f = open("DematAccounts.txt", mode="w")
                json.dump(accounts, f)
                f.close()
                print(amount, "rs. deposited to Account", y[0])
                return True
                break
        if(flag == 1):
            print("No Account Found!")
            return False
    else:
        print("No Accounts Found!")
        return False


def updateUserAquiredShare(ls):
    f = open("userAquiredShares.txt", mode="r")
    data = f.read()
    if(len(data) != 0):
        f.seek(0)
        userShares = json.load(f)
        f.close()
        if(str(ls[1]) in userShares):
            list = userShares[str(ls[1])]
            up_flag = 1
            for x in list:
                if(x[0] == ls[2] and x[1] == ls[3]):
                    if(ls[8] == "b"):
                        x[2] = x[2]+ls[0]
                        up_flag = 0
                        break
                    else:
                        if(ls[0] > x[2]):
                            return False
                        else:
                            x[2] = x[2]-ls[0]
                            up_flag = 0
                            break
            if(up_flag == 1):
                list.append([ls[2], ls[3], ls[0]])
        else:
            p = userShares[str(ls[1])]
            p.append([ls[2], ls[3], ls[0]])

        f = open("userAquiredShares.txt", mode="w")
        json.dump(userShares, f)
        f.close()
        return True
    else:
        userShares = {}
        userShares[ls[1]] = [[ls[2], ls[3], ls[0]]]
        f = open("userAquiredShares.txt", mode="w")
        json.dump(userShares, f)
        f.close()
        return True


def selltransaction(accNo):
    f = open("userAquiredShares.txt", mode="r")
    data = f.read()
    if(len(data) != 0):
        f.seek(0)
        usershares = json.load(f)
        f.close()
        ls = usershares[str(accNo)]
        print("------Acquired Shares-----")
        print("COMPANYNAME-SHARENAME-SHAREQUANTITY")
        coun = 1
        if(len(ls) != 0):
            for x in ls:
                print(x)
        else:
            print("No Acquired Shares!")
            return False
        company = input("Enter the Company--> ")
        share = input("Enter the ShareName--> ")
        while True:
            try:
                quantity = int(input("Quantity to sell--> "))
                break
            except:
                print("Please Enter a Integer Number!")
        flag = 1
        for x in ls:
            if(x[0] == company.title() and share.lower() == x[1] and x[2] >= quantity):
                flag = 0
                x[2] = x[2]-quantity
                flag = 0
                f = open("company.txt", mode="r")
                com = f.read()
                if(len(com) != 0):
                    f.seek(0)
                    companies = json.load(f)
                    f.close()
                    if company.title() in companies:
                        ls = companies[company.title()]
                        flag_comp = 1
                        for x in ls:
                            if (x[0] == share.lower()):
                                flag_comp = 0
                                effective_amount = x[2]
                                effective_amount = effective_amount*quantity
                                f = open("tax_rates.txt", mode="r")
                                if(len(f.read()) != 0):
                                    f.seek(0)
                                    tax = json.load(f)
                                    f.close()
                                else:
                                    tax = {"tran_charge": 0.5, "stt": 0.1}
                                trch = (
                                    effective_amount*tax["tran_charge"])//100
                                if(trch < 100):
                                    trch = 100
                                st = (effective_amount*tax["stt"])//100
                                effective_amount = effective_amount+trch+st

                        if(flag_comp == 1):
                            print("Company Does not have These shares!")
                            return False
                    else:
                        print("Company Does Not Available")
                        return False

                f = open("transaction.txt", mode="r")
                data = f.read()
                if(len(data) != 0):
                    f.seek(0)
                    trans = json.load(f)
                    f.close()
                else:
                    trans = []
                userData = findUserNameByaccNo(int(accNo))
                print(userData[0])
                new_transaction = [
                    quantity,
                    accNo, company.title(),
                    share.lower(),
                    str(datetime.date.today()),
                    effective_amount,
                    str(datetime.datetime.now().strftime(
                        "%H:%M:%S")),
                    userData[0], 's']
                if(updateUserAquiredShare(new_transaction)):
                    trans.append(new_transaction)
                    auto_deposit_money(accNo, effective_amount*quantity)
                    f = open("transaction.txt", mode="w")
                    json.dump(trans, f)
                    f.close()
                    f = open("userAquiredShares.txt", mode="w")
                    json.dump(usershares, f)
                    f.close()
                    print("Transaction Successful")
                    return True
        if(flag == 1):
            print("No such Record")
            return False
    else:
        print("Company Data Not Available")
        return False


def buytransaction(accNo):
    company = input("Enter the company Name--> ")
    f = open("company.txt", mode="r")
    data = f.read()
    if(len(data) != 0):
        f.seek(0)
        companies = json.load(f)
        f.close()
        comp_flag = 1
        for x, y in companies.items():
            if(x == company.title()):
                comp_flag = 0
                print("Share Name     Share Quantity      Share Price")
                for val in y:
                    print(val[0], val[1], val[2], sep="              ")

                while True:
                    share_name = input("ShareName to purchase--> ")
                    if(share_name == "none"):
                        break
                    share_flag = 1
                    for val in y:
                        if(val[0] == share_name):
                            share_flag = 0
                            while True:
                                try:
                                    quantity = int(
                                        input("Enter the valid quantity to Buy--> "))
                                    break
                                except:
                                    print("Please Enter an integer Value")

                            if(quantity > val[1]):
                                print("Share Quantity not Available")
                                continue
                            elif(quantity == 0):
                                print(
                                    "No opertaion occured for current share.")
                                break
                            else:
                                f = open("tax_rates.txt", mode="r")
                                if(len(f.read()) != 0):
                                    f.seek(0)
                                    tax = json.load(f)
                                    f.close()
                                else:
                                    tax = {"tran_charge": 0.5, "stt": 0.1}
                                trch = (
                                    quantity*val[2]*tax["tran_charge"])//100
                                if(trch < 100):
                                    trch = 100
                                st = (quantity*val[2]*tax["stt"])//100
                                effective_amount = quantity*val[2]+trch+st
                                status = auto_withdraw_money(
                                    accNo, int(effective_amount))
                                if(status):
                                    f = open("transaction.txt", mode="r")
                                    dat = f.read()
                                    if(len(dat) != 0):
                                        f.seek(0)
                                        transactions = json.load(f)
                                        f.close()
                                    else:
                                        transactions = []
                                    userData = findUserNameByaccNo(
                                        int(accNo))
                                    new_transaction = [
                                        quantity,
                                        accNo, company.title(),
                                        share_name.lower(),
                                        str(datetime.date.today()),
                                        effective_amount,
                                        str(datetime.datetime.now().strftime(
                                            "%H:%M:%S")), userData[0], 'b']
                                    updateUserAquiredShare(new_transaction)
                                    updateCompanyShare(new_transaction)
                                    transactions.append(new_transaction)
                                    f = open("transaction.txt", mode="w")
                                    json.dump(transactions, f)
                                    f.close()
                                    print("Transaction Successful!")
                                    return True
                                else:
                                    print("transaction failed!")
                                    return False
                    if(share_flag == 1):
                        print("Asked Share Not Found!")
                        return False
        if(comp_flag == 1):
            print("Company Not Found!")
            return False


def updateCompanyShare(ls):
    f = open("company.txt", mode="r")
    data = f.read()
    if(len(data) != 0):
        f.seek(0)
        companies = json.load(f)
        f.close()
        if(ls[8] == "b"):
            for x in companies[ls[2]]:
                if(x[0] == ls[3]):
                    x[1] = x[1]-ls[0]
                    f = open("company.txt", mode="w")
                    json.dump(companies, f)
                    f.close()
                    break
    else:
        print("Company Data not found!")


def display_demat_account_details(accNo):
    f = open("DematAccounts.txt", mode="r")
    acc = f.read()
    if(len(acc) != 0):
        f.seek(0)
        accounts = json.load(f)
        f.close()
        flag = 1
        for x, y in accounts.items():
            if(y[0] == int(accNo)):
                print("===========Account Details============")
                print("User                --> ", y[1])
                print("Username            -->", x)
                print("DMAT Account Number --> ", y[0])
                print("DMAT Account Balance--> ", y[2])
                flag = 0
                break
        if(flag == 1):
            print("User Data not Available!")
    else:
        print("User Data not Available!")


def deposit_money(accNo):
    while True:
        try:
            amount = int(input("Enter the amount to deposit--> "))
            break
        except:
            print("Please Enter an integer Value")
    f = open("DematAccounts.txt", mode="r")
    acc = f.read()
    if(len(acc) != 0):
        f.seek(0)
        accounts = json.load(f)
        f.close()
        flag = 1
        for x, y in accounts.items():
            if(y[0] == int(accNo)):
                y[2] = y[2]+amount
                flag = 0
                f = open("DematAccounts.txt", mode="w")
                json.dump(accounts, f)
                f.close()
                print(amount, "rs. deposited to Account", y[0])
                return True
                break
        if(flag == 1):
            print("No Account Found!")
            return False
    else:
        print("No Accounts Found!")
        return False


def withdraw_money(accNo):
    while True:
        try:
            amount = int(input("Enter the amount to Withdraw--> "))
            break
        except:
            print("Please Enter an integer Value")
    f = open("DematAccounts.txt", mode="r")
    acc = f.read()
    if(len(acc) != 0):
        f.seek(0)
        accounts = json.load(f)
        f.close()
        flag = 1
        for x, y in accounts.items():
            if(y[0] == int(accNo)):
                flag = 0
                if(y[2] >= amount):
                    y[2] = y[2]-amount
                    f = open("DematAccounts.txt", mode="w")
                    json.dump(accounts, f)
                    f.close()
                    print(amount, "rs. withdrawn to Account", y[0])
                    return True
                    break
                else:
                    print(
                        "Not Sufficient amount in your Account with Account Number", y[0])
                    return False
                    break
        if(flag == 1):
            print("No Account Found!")
            return False
    else:
        print("No Accounts Found!")
        return False


def auto_withdraw_money(accNo, amount):
    f = open("DematAccounts.txt", mode="r")
    acc = f.read()
    if(len(acc) != 0):
        f.seek(0)
        accounts = json.load(f)
        f.close()
        flag = 1
        for x, y in accounts.items():
            if(y[0] == int(accNo)):
                flag = 0
                if(y[2] >= amount):
                    y[2] = y[2]-amount
                    f = open("DematAccounts.txt", mode="w")
                    json.dump(accounts, f)
                    f.close()
                    print(amount, "rs. withdrawn to Account", y[0])
                    return True
                    break
                else:
                    print(
                        "Not Sufficient amount in your Account with Account Number", y[0])
                    return False
                    break
        if(flag == 1):
            print("No Account Found!")
            return False
    else:
        print("No Accounts Found!")
        return False
