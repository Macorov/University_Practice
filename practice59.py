lst1 = input("Enter a list: ")
lst1 = lst1[1:-1]
lst1 = lst1.split(", ")
lst2 = input("Enter a list: ")
lst2 = lst2[1:-1]
lst2 = lst2.split(", ")
flst1 = []
flst2 = []
final = 0
try:
    for elm in lst1:
        elm = int(elm)
        flst1.append(elm)
    for elm in lst2:
        elm = int(elm)
        flst2.append(elm)
    count = len(flst1)
    if count < len(flst2):
        count = len(flst2)
    for elm in range(count):
        final += flst1[elm]*flst2[elm]
    print(final)
except ValueError:
    print("The list has some non number values")
except IndexError:
    print("Index out of bound")