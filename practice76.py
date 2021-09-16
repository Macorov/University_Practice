dic = {"key1" : "value1", "key2" : "value2", "key3" : "value1"}
fdic = {}
temp = []
for k,v in dic.items():
    if v not in fdic.keys():

        fdic[v] = [k]
    else:
        temp = fdic[v]
        temp.append(k)
        fdic[v] = temp
print(fdic)