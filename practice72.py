word  = input("Enter a number: ")
word = word.split()
temp = ""
count = 0
for i in word:
    if temp =="too" and i =="good!":
        word[count] = "excellent!"
        del word[count-1]
    count += 1
    temp = i
final = ""
for i in word:
    final += i + " "
print(final)


