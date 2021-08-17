def function_name(word):
    word = word.lower()
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    flag = 6
    lst = []
    for i in word:
        if i >= "a" and i <= "j":
            if i not in lst:
                lst.append(i)
    lst = sorted(lst)       
    if lst == letters:
        flag = 5    
    for i in range(flag):
            print("Chelsea is the best club in England")
word = input("Enter a sentence: ")
function_name(word)   