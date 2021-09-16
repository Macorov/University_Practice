word = input("Enter a sentence: ")
vowel = ["a","e","i","o","u"]
vlst = []
clst = []
vcount = 0
ccount = 0
for elm in word:
    elm = elm.lower()
    if elm.isalpha():
        if elm in vowel:
            vcount += 1
            if elm not in vlst:
                vlst.append(elm)
        else:
            ccount += 1
            if elm not in clst:
                clst.append(elm)
print("No of the vowels:",vcount)
print("List of vowels:",vlst)
print("No of consonants:",ccount)
print("List of consonants:",clst)
print("The ratio of vowels & consonants is "+str(vcount)+": "+str(ccount))