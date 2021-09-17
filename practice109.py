inpacket = int(input("Enter chocolate: "))
empacket = int(input("Empty packet: "))
repacket = int(input("Returned chocolate: "))
sum1 = 0
leftpacket = 0
while inpacket > 0:
    sum1 += inpacket
    inpacket = (inpacket // empacket)*repacket
    leftpacket += inpacket % empacket
    if leftpacket >= empacket:
        k = leftpacket // empacket
        sum1 += k*repacket
        leftpacket -= k*leftpacket
    #print(inpacket)
    #print(leftpacket)
print(sum1)

    