lst = [2,53,-2,6,2]
for i in range(len(lst)-1):
    for j in range(len(lst)-i-1): #bubble sorting 
        if lst[j]>lst[j+1]:
            temp = lst[j]
            lst[j] = lst[j+1]
            lst[j+1] = temp
print(lst)