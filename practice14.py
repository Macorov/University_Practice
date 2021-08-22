color = input("Enter a number: ")
sumr = 0
sumg = 0
sumb = 0
lst = []
for i in color:
    if i == "R":
        sumr += 1
    elif i == "G":
        sumg += 1
    elif i == "B":
        sumb += 1
if sumr > 1:
    lst.append(("Red",sumr))
if sumg > 1:
    lst.append(("Green",sumg))
if sumb > 1:
    lst.append(("Blue",sumb))
print(tuple(lst))