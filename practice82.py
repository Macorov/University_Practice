rotate = int(input("Enter a number: "))
sum1 = 0
count1 = 0
count2 = 0
for i in range(rotate):
    num = int(input("Enter a number: "))
    if num < 101 and num>-1:
        sum1 += num
        count1 += 1
    else:
        count2 += 1
avg = sum1 / count1
err = (count2 / rotate)*100
print("Average:",avg)
print("Error Raate(%):",err)
