word = input("Enter a word: ")
count = 0
for i in word:
    count += 1
    if i.isupper():
        break
word = word[count::]
count = 0
for i in word:
    count += 1
    if i.isupper():
        break
word = word[:count-1]
if word == "":
    print("BLANK")
else:
    print(word)