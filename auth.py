import json



def admin_login(username, password):
    f = open("admin_cred.txt", mode="r")
    admin_credential = json.load(f)
    f.close()
    if(username == admin_credential["username"] and password == admin_credential["password"]):
        return True
    else:
        return False


def demat_login(accNo, password):
    f = open("DematAccounts.txt", mode="r")
    x = f.read()
    accounts = {}
    if(len(x) != 0):
        f.seek(0)
        accounts = json.load(f)
        f.close()
    else:
        print("No Account is present!")
        return False

    for y in accounts.values():
        if(y[0] == int(accNo) and y[3] == password):
            return True
    return False


def bank_admin_login(username, password):
    f = open("bank_admin_cred.txt", mode="r")
    admin_credential = json.load(f)
    f.close()
    if(username == admin_credential["username"] and password == admin_credential["password"]):
        return True
    else:
        return False
