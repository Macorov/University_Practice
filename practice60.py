try:
    word = input("Enter a number: ")
    vowels = ["a", "e", "i", "o", "u"]
    vcount = 0
    ccount = 0
    for elm in word:
        if elm.isalpha():
            if elm in vowels:
                vcount += 1
            else:
                ccount += 1
    if vcount >= ccount:
        raise RuntimeError
    else:
        print("The sentence will work.")
except RuntimeError:
    print("Number of vowels greater/equal to consonants. Please paraphrase.")
except:
    print("Other errors")