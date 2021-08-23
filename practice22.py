dic = {".,?!": 1,"ABC":2,"DEF":3,"GHI":4,"JKL":5,"MNO":6,"PQRS":7,"TUV":8,"WXYZ":9," ":0}
word = input("Enter a number: ")
word = word.upper()
final = ""
for i in word:
    for k,v in dic.items():
        if i in k:
            num = k.index(i) +1
            m = str(v) * num
            final += m
print(final)