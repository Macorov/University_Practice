num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
k = ""
sum1 = ""
for i in range(1,num1+1):
    num2 -= 1
    k += str(i)
    sum1 += k + "="*num2 + '\n'
print(sum1,end="")

