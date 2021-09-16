num = int(input("Enter a number: "))
dic = {}
for i in range(2,11):
    
    if num % i == 0:
        flag = True
    else:
        flag = False
    dic[i] = flag
print(dic)