final = {}
while True:
    num = input("Enter a number: ")
    if num == "STOP":
        break
    else:
        num = int(num)
    
    if num not in final.keys():
        final[num] = 1
    else:
        m = final[num] + 1
        final[num] = m
for k,v in final.items():
    print(k,"-",v,"times")