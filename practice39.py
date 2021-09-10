lst1 = input("Enter a list: ")
lst1 = lst1[1:-1]
lst1 = lst1.split(", ")
lst2 = input("Enter a list: ")
lst2 = lst2[1:-1]
lst2 = lst2.split(", ")
tmplst = lst1 + lst2
flst = []
for i in tmplst:
    i = int(i)
    flst.append(i)
for i in range(len(flst)-1):
    for j in range(len(flst)-i-1):
        if flst[j] > flst[j+1]:
            temp = flst[j]
            flst[j] = flst[j+1]
            flst[j+1] = temp
print("Sorted list=",flst)
if len(flst) % 2 != 0:
    median = (len(flst)+1)//2
    
    final = flst[median-1]
else:
    median = (len(flst)//2)
     
    final1 = flst[median-1]
    median = (len(flst)//2)+1
    
    final2 = flst[median-1]
    final = (final1+final2)/2
print("Median=",final)
