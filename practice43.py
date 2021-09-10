def dic_sorting(dic):
    lstk = []
    lstv= []
    for key,val in dic.items():
        lstk.append(key)
        lstv.append(val)
    for elm1 in range(len(lstv)):
        max_index = elm1
        for elm2 in range(elm1,len(lstv)):
            if lstv[elm2] > lstv[elm1]:
                max_index = elm2
        tempv = lstv[max_index]
        lstv[max_index] = lstv[elm1]
        lstv[elm1] = tempv
        tempk = lstk[max_index]
        lstk[max_index] = lstk[elm1]
        lstk[elm1] = tempk
    return lstk

lst = [ ["Alan", 95, 87, 91], ["Turing", 92, 90, 83], ["Elon", 87, 92, 80], ["Musk", 85, 94, 90] ]
dic = {}
for elm in lst:
    dic[elm[0]] = elm[1:]
course = input("Enter the name of you course: ")
var = ["CSE110","PHY111","MAT110"]
count = 0
if course in var:
    if course == "CSE110":
        count = 1
    elif course == "PHY111":
        count = 2
    elif course == "MAT110":
        count = 3
    for elm in lst:
        dic[elm[0]] = elm[count]
    flst = dic_sorting(dic)
    for elm in flst:
        print(elm)
else:
    print("Enter a Valid Course")