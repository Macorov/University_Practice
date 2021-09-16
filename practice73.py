word = input("Enter a number: ")
lowtask = True
uptask = True
digtask = True
sptask = True
splst = ("_" , "$" ,"#" ,"@")
for i in word:
    if i.islower():
        lowtask = False
    elif i.isupper():
        uptask = False
    elif i.isdigit():
        digtask = False
    elif i in splst:
        sptask = False
final = ""
if lowtask:
    final += "Lowercase charecter missing, "
if uptask:
    final += "Uppercase charecter missing, "
if digtask:
    final += "Digit missing, "
if sptask:
    final += "Special charecter missing, "
if final == "":
    print("OK")
else:

    
    print(final)