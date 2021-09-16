lst1 = input("Enter a list: ")
lst1 = lst1[1:-1]
lst1 = lst1.split(",")
flst = []
try:
    for elm in lst1:
        elm = int(elm.strip())
        elm = elm * 1050
        flst.append(elm)
    print(flst)
except ValueError:
    print("Wrong input type")
except Exception:
    print("Other errors")
