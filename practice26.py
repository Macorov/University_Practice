num = input("Enter a lst: ")
num = num.split(" ")
final = {}
for i in num:
    
    i = i.strip(",")
    i = i.strip(".")
    m = len(i)
    if i.isalpha():
        if m not in final.keys():
            final[m] = [i]
        else:
            p = final[m]
            p.append(i)
            final[m] = p
print(final)