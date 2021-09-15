file = open("task3.txt")
count = 0 
lst = file.readlines()
for elm in lst:
    count+= 1
print(count)