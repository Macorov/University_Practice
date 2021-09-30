def replacer(str_0,str_1):
    str_2 = ""
    list_0 = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    if str_1 == "vowels":
        for elm in str_0:
            if elm in list_0:
                str_2 += "V"
            else:
                str_2 += elm
    elif str_1 == "consonants":
        for elm in str_0:
            if elm.isalpha():
                if elm not in list_0:
                    str_2 += "C"
                else:
                    str_2 += elm
            else:
                str_2 += elm
    return str_2

print(replacer("It is MAT110 final", "vowels"))
print(replacer("It is CSE110 final", "consonants"))