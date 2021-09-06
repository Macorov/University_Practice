def function_name(word):
    lst = []
    for i in word:
        if i not in lst:
            lst.append(i)
    dic = {}
    pindex = 0
    nindex =- len(word)
    count = 0
    for i in lst:
        pindex = 0
        nindex = -len(word)
        count = 0
        for k in word:
            if i == k:
                if count == 0:
                    dic[i] = [pindex,nindex]
                    count += 1
                else:
                    temp = dic[i]
                    temp.append(pindex)
                    temp.append(nindex)
                    dic[i] = temp
            pindex += 1
            nindex += 1
    return dic
print(function_name("pythonbook"))