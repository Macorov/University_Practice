word = input("Enter a sentence: ")
word = word.split(" ")
print(word)
dic = {}
for i in word:
    if i.isalpha() or i.isdigit():
        k = len(i)
        if k not in dic.keys():
            dic[k] = [i]
        else:
            temp = dic[k]
            temp.append(i)
            dic[k] = temp
print(dic)