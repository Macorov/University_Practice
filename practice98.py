rotate = int(input("Enter a number: "))
lst = []
for i in range(rotate):
    k = (input("Enter ID: "))
    lst.append(k)
dic = {}
for i in lst:
    k = i[0:2] + "th"
    if k not in dic.keys():
        dic[k] = [i]
    else:
        temp = dic[k]
        temp.append(i)
        dic[k] = temp
print(dic)
