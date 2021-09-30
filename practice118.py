def function_name(num,word):
    word = word.split(" ")
    lst = []
    for i in word:
        lst.append(int(i))
    sum1 = 0
    prevcount = 0
    count = 1
    maxsum = 0
    base = 0
    hight = 0
    for i in range(num):
        sum1 = lst[count]*lst[prevcount] * 0.5
        if sum1 > maxsum:
            maxsum = sum1
            base = lst[prevcount]
            hight = lst[count]

        prevcount += 2
        count += 2
    return f"The area of the largest triangle is {maxsum} with a base of {base} and a height of {hight}"
print(function_name(3, "20 3 33 7 11 14"))
print(function_name(4, "15 5 6 3 6 10 15 2"))
