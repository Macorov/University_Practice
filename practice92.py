word = input("Enter a number: ")
in1 = int(input("Enter a number: "))
in2 = int(input("Enter another number: "))
count = 0
fword = ""
if in2 < len(word):
    for i in word:
        k = ord(i)
        k = k +2
        if i == "y":
            i = "a"
        elif i == "z":
            i = "b"
        else:
            i = chr(k)
        if count >= in1 and count <= in2:
            fword += i
        count += 1
    print(fword) 
else:
    print("Invalid Index")
  
