num = int(input("Enter a number: "))
lst = []
final = {}
val = []
for i in range(num):   
    k = input("Enter the years: ")
    
    lst.append(k)

for i in lst:
    k = i[0:2]
    m = k + "th"
    if m not in final.keys():
        
        final[m] = [i]
    else:
        
        val = final[m]
        print(val)
        val.append(i)
        final[m] = val
print(final)