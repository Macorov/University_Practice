def function_name(lst):
    lst = lst.split(",")
    sum1 = 0
    count = 0
    dic = {}
    for i in lst:
        i = int(i)
        sum1 += i
        dic[count] = sum1
        count += 1
    return dic
print(function_name("3,1,5,4,6,7,8"))
print(function_name("5,1,3,7,4,8"))