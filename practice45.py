file = open("bracufile1.txt")
lst = file.readlines()
for i in lst:
    print(i,end="")