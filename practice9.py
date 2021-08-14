def remove_odd(lst):
    final = []
    for i in lst:
        if i % 2 ==0:
            final.append(i)
    return(final)
print(remove_odd ([21, 33, 44, 66, 11, 1, 88, 45, 10, 9]))
print(remove_odd ([11,2,3,4,5,2,0,5,3]))