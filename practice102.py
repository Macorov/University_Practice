rotate = int(input("Enter a number: "))
lst = []
dic = {}
for i in range(rotate):
    k = (input("Enter ID: "))
    lst.append(k)
for i in lst:
    m = i[2]
    if m == "3":
        k = "Summer"
        if k not in dic.keys():
            dic[k] = [i]
        else:
            temp = dic[k]
            temp.append(i)
            dic[k] = temp
    elif m == "1":
        k = "Spring"
        if k not in dic.keys():
            dic[k] = [i]
        else:
            temp = dic[k]
            temp.append(i)
            dic[k] = temp
    elif m == "2":
        k = "Fall"
        if k not in dic.keys():
            dic[k] = [i]
        else:
            temp = dic[k]
            temp.append(i)
            dic[k] = temp
print(dic)
    