rotate = int(input("Enter a number: "))
sum1 = ""
for i in range(1,rotate+1):
    if i % 4 == 0:
        sum1 += "Penny!"
    else:
        sum1 += "Knock!"
print(sum1)
