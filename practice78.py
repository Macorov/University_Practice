def function_name(word):
    word = word.split(",")
    dic = {}
    sum = 0
    count = 0
    for i in word:
        i = int(i)
        sum += i
        dic[count] = sum
        count += 1
    return dic
print(function_name("3,1,5,4,6,7,8"))
print(function_name("5,1,3,7,4,8"))