try:    
    sentence = input("Enter a sentence: ")
    cha = input("Character to be removed: ")
    sindex = int(input("Starting index: "))
    eindex = int(input("Ending index: "))
    fsentence = ""
    count = 0
    incount = 0
    if eindex > len(sentence):
        raise IndexError
    for i in sentence:
        if count >=sindex and count < eindex:
            if cha == i:
                incount += 1
                fsentence += str(incount)
            else:
                fsentence += i
        else:
            fsentence += i
        count += 1
    print(fsentence)
except ValueError:
    print("Value Error: Wrong input, please enter an integer value.")
except IndexError:
    print("Index Error: Index is outside the range of sentence length.")
except TypeError: 
    print("Type Error: Cannot add integer value with string.")
except NameError:
    print("Name Error: Variable not defined")
except Exception:
    print("Other Errors")
finally:
    print("The program execution is complete")