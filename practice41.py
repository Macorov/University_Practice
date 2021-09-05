def dic_sorting(dic):
    lstk = []
    lstv= []
    for k,v in dic.items():
        lstk.append(k)
        lstv.append(v)
    for i in range(len(lstv)):
        max_index = i
        for j in range(i,len(lstv)):
            if lstv[j] > lstv[i]:
                max_index = j
        tempv = lstv[max_index]
        lstv[max_index] = lstv[i]
        lstv[i] = tempv
        tempk = lstk[max_index]
        lstk[max_index] = lstk[i]
        lstk[i] = tempk
    return lstk

lst = [ ["Alan", 95, 87, 91], ["Turing", 92, 90, 83], ["Elon", 87, 92, 80], ["Musk", 85, 94, 90] ]
dic = {}
for i in lst:
    dic[i[0]] = i[1:]
course = input("Enter the name of you course: ")
count = 0
if course == "CSE110":
    count = 1
elif course == "PHY111":
    count = 2
elif course == "MAT110":
    count = 3
for i in lst:
    dic[i[0]] = i[count]
flst = dic_sorting(dic)
for i in flst:
    print(i)

