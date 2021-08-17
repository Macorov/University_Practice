def rangeanddivisor(a,b,x,y):
    sum = 0
    for i in range(a,b):
        if (i % x == 0 or i % y==0) and not(i % x == 0 and i % y==0):
            sum += i
    return sum
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))
num4 = int(input("Enter a number: "))
print(rangeanddivisor(num1,num2,num3,num4))
