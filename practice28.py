lst = [2,53,-2,6,2]
for i in range(len(lst)):
    min_index = i
    for j in range(i+1,len(lst)): #section sort 
        if lst[j] < lst[i]:
            min_index = j
    temp = lst[min_index]
    lst[min_index] = lst[i]
    lst[i] = temp
print(lst)