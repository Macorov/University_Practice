tik = input("Enter a number: ")
long = len(tik)

sum1 = 0
sum2 = 0
p1 = ""
p2 = ""
if long % 2 == 0:
    p1 = tik[:(long//2)]
    p2 = tik[long//2::]
else:
    k = long -1
    k = k//2
    p1 = tik[:k]
    p2 = tik[k+1::]
for i in p1:
    i = int(i)
    sum1 += i
for i in p2:
    sum2 += int(i)
if sum1 == sum2:
    print("You won the lottery!")
else:
    print("You lost")