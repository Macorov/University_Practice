#que no 3
def function_name(num1):
    count = 0
    sum1 = ""
    for i in range(num1):
        if count == 0:
            sum1 += "A"*num1 + "\n"
        elif count == num1-1:
            sum1 += "#"*(num1-1) + "A"*num1
        else:
            sum1 += "#"*count +"A" +"*"*(num1-2) + "A"+'\n'
        count += 1
    return sum1
print(function_name(4))
#print(function_name(3))
print(function_name(5))
        