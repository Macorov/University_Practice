file = open("bracufile1.txt")
lst = file.readlines()
for i in lst:
    print(i,end="") # or you can use rstrip()