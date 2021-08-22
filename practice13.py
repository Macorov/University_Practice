word = input("Enter a number: ")
word = word.split(", ")
count = 0
sum1 = 0
sum2 = 0
lst1 = []
lst2 = []
for i in word:
    for k in i:
        k = int(k)
        if count % 2 ==0:
            sum1 += k
        else:
            sum2 += k
        count += 1
    if sum1 == sum2:
        lst1.append(int(i))
    else:
        lst2.append(int(i))
    sum1 = 0
    sum2 = 0
    count = 0
lst1 = tuple(lst1)
lst2 = tuple(lst2)
final = (lst1,lst2)
print(final)