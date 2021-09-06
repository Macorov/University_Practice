def function_name(word):
    #word = word.split()
    
    lst = []
    for i in word:
        if i not in lst:
            lst.append(i)
    flst = []
    num = 0
    for i in lst:
        num = ord(i)
        temp = str(num)+str(i)+str(num)
        flst.append(temp)
    return(flst)
print(function_name("pythonbook"))
