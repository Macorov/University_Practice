word1 = input("Enter a word: ")
word2 = input("Enter a word: ")
final = ""
for i in word1:
    if i in word2:
        final += i
for i in word2:
    if i in word1:
        final += i
if final =="":
    print("Nothing in common.")
else:
    print(final)