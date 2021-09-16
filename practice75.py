word = input("Enter a word: ")
final = ""
ch = ""
dig = ""
for i in word:
    if i.isalpha():
        ch += i
    elif i.isdigit():
        dig += i
ch = sorted(ch)
dig = sorted(dig)
fdig1 = ""
fdig2 = ""
fch1 = ""
fch2 = ""
for i in dig:
    i = int(i)
    if i % 2 != 0:
        fdig1 += str(i)
    else:
        fdig2 += str(i)
for i in ch:
    if i.islower():
        fch1 += i
    else:
        fch2 += i

fdig3 =fch1+fch2+  fdig1 + fdig2
print(fdig3)

    