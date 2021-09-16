word = input("Enter a word: ")
count = 0
temp = "1"
fword = ""
for elm in word:
    k = ord(elm)
    if k %2 == 0:
        fword += temp
    else:
        fword += elm
    count += 1
    temp = elm
print(fword)