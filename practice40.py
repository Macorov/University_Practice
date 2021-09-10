lst = input("Enter a list: ")
lst = lst[1:-1]
lst = lst.split(", ")
lst1 = []
for i in lst:
    i = int(i)
    lst1.append(i)
minsum = None
min_index1 = None
min_index2 = None
count = 0
for i in range(len(lst1)):
    for j in range(i+1,len(lst1)):
        sum = lst1[i] + lst1[j]
        sum = abs(sum)
        if count == 0:
            minsum = sum
            min_index1 = lst1[i]
            min_index2 = lst1[j]
        elif sum < minsum:
            minsum = sum
            min_index1 = lst1[i]
            min_index2 = lst1[j]
        count += 1
print("Two pairs which have the smallest sum =",min_index1,"and",min_index2)


