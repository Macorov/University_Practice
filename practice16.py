dict1 = input("Enter a number: ")
dict2 = input("Enter another number: ")
dict1 = dict1[1:-1]
dict1 = dict1.split(", ")
dict2 = dict2[1:-1]
dict2 = dict2.split(", ")
lst = []
final = {}
flag = True
for i in dict1:
    m = i.split(": ")
    for k in dict2:
        j = k.split(": ")
        if m[0] == j[0]:
            lst.append(m[1].strip("'"))
            lst.append(j[1].strip("'"))
            flag = False
    if flag:
        lst.append(m[1].strip("'"))
    f = m[0]
    f = f[1:-1]
    final[f] = lst
    flag = True
    lst = []
for k in dict2:
    j = k.split(": ")
    m = j[0]
    m = m.strip("'")
    if m not in final.keys():
        final[m] = [j[1].strip("'")]
print(final)
        