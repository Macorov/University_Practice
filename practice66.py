def function_name(word):
    lst = []
    for i in word:
        i = int(i)
        if i not in lst:
            lst.append(i)
    dic = {}
    even_check = ""
    prime_check = "prime"
    perfect_check = ""
    for i in lst:
            
        even_check = ""
        prime_check = "prime"
        perfect_check = ""
        sum1 = 0
        if i % 2 == 0:
            even_check = "even"
        else:
            even_check = "odd"
    
        for k in range(1,round(i)):
            if i %k == 0:
                sum1 += k
        if sum1 == i:
            perfect_check = "perfect"
        else:
            perfect_check = "not perfect"
        for k in range(2,round(i)):

            if i % k ==0:
                prime_check = "not prime"
                break
        if i == 1:
            prime_check = "not prime"
        dic[i] = (even_check,prime_check,perfect_check)
    return dic
print(function_name("2441396"))
        