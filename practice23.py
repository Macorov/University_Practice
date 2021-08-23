lst1 = input("Enter a list: ")
lst1 = lst1[1:-1]
lst1 = lst1.split(", ")
lst2 = input("Enter a list: ")
lst2 = lst2[1:-1]
lst2 = lst2.split(", ")
sum = 0
final = []
for i in lst1:
    i = int(i)
    for k in lst2:
        k = int(k)
        sum1 = i*k
        final.append(sum1)
        sum1 = 0
print(final)