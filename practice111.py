word = input("Enter a string: ")
x = 0
y = 0
tup = ()
for i in word:
    if i =="R":
        x += 1
    elif i == "L":
        x -= 1
    elif i =="U":
        y += 1
    elif i == "D":
        y -= 1
tup = (x,y)
print(tup)