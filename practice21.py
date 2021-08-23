word1 = input("Enter a word: ")
word2 = input("Enter another word: ")
dic1 = {}
dic2 = {}
flag = True
for i in word1:
    if i not in dic1.keys():
        dic1[i] = 1
    else:
        m = dic1[i] + 1
        dic1[i] = m
for i in word2:
    if i not in dic2.keys():
        dic2[i] = 1
    else:
        m = dic2[i] + 1
        dic2[i] = m
print(dic1)
print(dic2)
for k,v in dic1.items():
    try:
        if dic2[k] != v:
            flag = False
            break
    except:
        flag = False
if flag:
    print("Those strings are anagrams")
else:
    print("Those strings are not anagrams")