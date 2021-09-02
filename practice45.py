file = open("abcd.txt")
lst = file.readlines()
for i in lst:
    print(i,end="") # or you can use rstrip()