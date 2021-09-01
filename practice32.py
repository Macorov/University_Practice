def binary_sorting(lst,x,start,end):
    l = start
    
    r = end
    
    mid =l+(r-l)//2
    if l == r:
        return "GG"

    elif lst[mid] == x:
         return mid
    elif lst[mid] > x:
        return binary_sorting(lst,x,l,mid)
    else:
        return binary_sorting(lst,x,mid+1,r)
    
print(binary_sorting([1,5,7,19,20,100,1222],100,0,6))