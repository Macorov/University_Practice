def function_name(word,lstnum,lstsp):
    final = ""
    for i in word:
        k = ord(i)
        count =0
        num1 = False
        num2 = False
        for m in lstnum:
            if k % m ==0:
                if count == 0:
                    num1 = True
                else:
                    num2 = True
            count += 1
        if num1 == True and num2 == True:
            final += lstsp[-1]
        elif num1 and num2 == False:
            final += lstsp[0]
        elif num2:
            final += lstsp[1]
        else:
            final += i
    return final
print(function_name("Programming is fun. Let’s code.", [6, 8], ['$', '#', '@']))
print(function_name('Python is easy', [3, 5], ['@', '*', '+']))                