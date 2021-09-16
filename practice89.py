word = input("Enter a sentence: ")
lst = []
for i in word:
    k = ord(i)
    if k >47 and k < 58:
        lst.append(i)
if len(lst) == len(word):
    print("There is no alphabet in the string")
elif len(lst) > 0:

    for i in range(len(lst)):
        min_index = i
        for k in range(i,len(lst)):
            if lst[k] < lst[min_index]:
                min_index = k
        temp = lst[i]
        lst[i] = lst[min_index]
        lst[min_index] = temp
    print(lst)
else:
    print("There is no digit in the string")