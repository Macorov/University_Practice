def function_name(word):
    word = word.split()
    word = sorted(word)
    lst =[]
    for i in word:
        if i not in lst:
            lst.append(i)
    dic = {}
    for i in lst:
        count = 0
        for k in word:
            if i == k:
                count += 1
        dic[i] = count
    fdic = {}
    lst = []
    for k,v in dic.items():
        newtemp = (v,k)   #best thing you can do with dic and tuple combo
        lst.append(newtemp)
    lst = sorted(lst)
    for v,k in lst:
        fdic[k] = v
    return fdic

print(function_name("go there come and go here and there go care"))