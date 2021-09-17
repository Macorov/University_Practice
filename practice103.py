def function_name(lst, num):
    flst = []
    count = 0
    for i in lst:
        if count == 0:
            temp = i
            count += 1
        else:
            if i > temp:
                sum1 = i - temp
            else:
                sum1 = temp - sum1
            if sum1 == num:
                flst.append([temp,i])
            temp = i
    if len(flst) == 0:
        return f"Not Possible"
    else:
        return flst
print(function_name([1, 5, 9, 13], 5))