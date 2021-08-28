lst = [2,53,-2,6,2]
for i in range(len(lst)-1):
    min_index = i
    for j in range(i,len(lst)): #efficient way in python to sort lst 
        if lst[j] < lst[i]:
            min_index = j
    lst[i],lst[min_index] = lst[min_index],lst[i]
print(lst)