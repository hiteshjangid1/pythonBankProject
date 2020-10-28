import json



def change_tax_rates():
    print("Input Values in Percentage")
    while True:
        try:
            tran = float(input("Enter the Transaction Charge--> "))
            break
        except:
            print("Please Enter a Float Value")

    while True:
        try:
            st = float(input("Enter the Transaction Charge--> "))
            break
        except:
            print("Please Enter a Float Value")

    f = open("tax_rates.txt", mode="r")
    ls = json.load(f)
    f.close()

    ls["tran_charge"] = tran
    ls["stt"] = st

    f = open("tax_rates.txt", mode="w")
    ls = json.dump(ls, f)
    f.close()

    print("Tax Rates Changed Successfully!")
    return True
