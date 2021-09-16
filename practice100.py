word = input("Enter a list ")
word = word.split(", ")
lst = []
dic = {}
for i in word:
    lst.append(int(i))
for i in lst:
    if i % 2 ==0:
        if 'Divisible by 2' not in dic.keys():
            dic['Divisible by 2'] = [i]
        else:
            temp = dic['Divisible by 2']
            temp.append(i)
            dic['Divisible by 2'] = temp
    if i % 3 ==0:
        if 'Divisible by 3' not in dic.keys():
            dic['Divisible by 3'] = [i]
        else:
            temp = dic['Divisible by 3']
            temp.append(i)
            dic['Divisible by 3'] = temp
    if i % 5 ==0:
        if 'Divisible by 5' not in dic.keys():
            dic['Divisible by 5'] = [i]
        else:
            temp = dic['Divisible by 5']
            temp.append(i)
            dic['Divisible by 5'] = temp
    if i % 2 != 0 and i % 3 != 0 and i% 5 != 0:
        if 'None' not in dic.keys():
            dic['None'] = [i]
        else:
            temp = dic['None']
            temp.append(i)
            dic['None'] = temp
print(dic)
        