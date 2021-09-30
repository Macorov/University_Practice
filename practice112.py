#q2
given_data = [["Alice", ["A","C","C","A"]], ["Sam", [ "A", "C", "B"]], 
["Amy", ["A","E"]],["Robin", ["A"] ] ]
dic = {}
count = 0
temp = ""
sum1 = 0
flag = True
fdic = {}
for elm in given_data:
    dic[elm[0]] = elm[1]

for key,value in dic.items():
    value = sorted(value)
    if len(value) == 1:
        print(key+":"+"You must have at least 2 subjects in A level.")
    else:
        sum1 = 0
        for elm2 in range(2):
            val = value[elm2]
            if val == "A":
                sum1 += 5
            elif val == "B":
                sum1 += 4
            elif val == "C":
                sum1 += 3
            elif val == "D":
                sum1 += 2
            else:
                print("Sorry",key,"the grades allowed in your top 2 grades are only A/B/C/D")
                flag = False
                break
        if flag:
            sum1 = sum1 /2
            print("Based on the A level result"+" "+key+"'s "+ "minimum GPA is "+str(sum1))
            fdic[key] = sum1
print(fdic)