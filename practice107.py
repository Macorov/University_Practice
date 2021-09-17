def function_name(word):
    dic = {}
    count = 0
    for k in word:
        if k.isdigit() or k.isalpha():
            if k not in dic.keys():
                dic[k] = [count]
            else:
                temp = dic[k]
                temp.append(count)
                dic[k] = temp
        count += 1
    return dic
print(function_name("this is my first semester."))
print(function_name("my student id is 010101."))
