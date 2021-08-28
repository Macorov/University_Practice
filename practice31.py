def binary_search(lst,x):
    r = len(lst) - 1
    l = 0
    while l <= r:
        mid = (l+r)//2
        if x == lst[mid]:
            return mid
        elif lst[mid] > x:
            r = mid - 1
        else:
            l = mid + 1
    return "GG"
print(binary_search([1,5,7,19,20,100,1222],25))
