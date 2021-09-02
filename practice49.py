file = open("bracufile2.txt")
nfile = open("bracuresult1.txt","w")
dic = {}
for i in file:
    temp = i.split(":")
    dic[int(temp[-1].strip())] = temp[0]

lst = []
for i in dic.keys():
    lst.append(i)
lst.sort(reverse=True)

fdic = {}
for i in lst:
    temp = dic[i]
    fdic[temp] = i
print(fdic)
for k,v in fdic.items():
    p = k+" : "+str(v)+"\n"
    nfile.write(p)
nfile.close()
