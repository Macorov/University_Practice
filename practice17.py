dict_1 = {"a":[5,2,55,17],"P":(11,121,222),"B":(37,53,71),"c":[45,92,50]}
count = 0
lst = []
flag = True
final = {}
for k,v in dict_1.items():
    for i in v:
         for m in range(2,i):
             div = i % m
             if div == 0:
                 flag = False
                 break
         if flag:
             lst.append(i)
         flag = True
    if k.isupper():
        final[k] = tuple(lst)
    else:
        final[k] = lst
    lst = []
print(final)

            
