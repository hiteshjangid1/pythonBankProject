import json

f = open("company.txt", mode="r")
com = f.read()
if(len(com) != 0):
    f.seek(0)
    companies = json.load(f)
    f.close()

for x, y in companies.items():
    print(x, y)
