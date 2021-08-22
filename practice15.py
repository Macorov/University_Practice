tup = input("Enter a tuple:")
tup = tup[1:-1]
tup = eval(tup)
hsum = 0
htup = ()
sum1 = 0
final = []
count = 0
for i in tup:
    for k in i:
        sum1 += k
    m = sum1 / len(i)
    final.append(m)
    if count == 0:
        hsum = sum1
        htup = i
    elif sum1 > hsum:
        hsum = sum1
        htup = i
    sum1 = 0
    count += 1
print("Average of tuples:",tuple(final))
print("Tuple with maximum sum is",htup)

