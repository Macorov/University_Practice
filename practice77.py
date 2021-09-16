def last_vowel(word):
    vlst = ("a", "e", "i", "o", "u")
    final = ""
    if len(word) <2:
        return word
    elif word[-1] in vlst:
        final = "yay" + word
        return final
    else:
        count = 0
        lim = len(word) -1
        final = word[-1]
        for elm in word:
            if count != lim:
               final += elm
            else:
                final += "ay"
            count += 1 
        return final
print(last_vowel("dalek"))
print(last_vowel("b"))
print(last_vowel("apple"))