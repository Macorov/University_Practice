num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
dic = {}
lst = [1,2,7]
for i in range(num1,num2):
    k = str(i)
    k = k[-1]
    k = int(k)
    if k not in lst:
        if k not in dic.keys():
            dic[k] = [i]
        else:
            temp = dic[k]
            temp.append(i)
            dic[k] = temp
print(dic)