word = input("Enter a string: ")
word = word.split(" ")
flst = ""
for i in word:
    i = i[::-1]
    flst += i + " "
print(word)
print(flst)