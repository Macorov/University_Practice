word = input("Enter a sentence: ")
word = word.lower()
dic = {}
for i in word:
    if i.isdigit():
        if 1 not in dic.keys():
            dic[1] = [i]
        else:
            temp = dic[1]
            if i not in temp:
                temp.append(i)
            dic[1] = temp
    elif i.isalpha():
        if 2 not in dic.keys():
            dic[2] = [i]
        else:
            temp = dic[2]
            if i not in temp:
                temp.append(i)
            dic[2] = temp
print(dic)