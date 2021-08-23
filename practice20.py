dic = input("Enter a dictionary: ")
dic = dic[1:-1]
dic = dic.split(", ")
final = {}
for i in dic:
    lst = []
    i = i.split(": ")
    a = i[0].strip('"')
    b = i[1].strip('"')
    if b not in final.keys():
        final[b] = [a]
    else:
        m = final[b]
        m.append(a)
        final[b] = m
print(final)
{"key1": "value1", "key2": "value2", "key3": "value1"}