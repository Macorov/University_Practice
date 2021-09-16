file1 = open("task4.txt")
file2 = open("task5.txt")
lst1 = file1.readlines()
lst2 = file2.readlines()
lim = len(lst1) -1
count = 0
final = ""
for elm in range(len(lst1)):
    word1 = lst1[elm].strip()
    word2 = lst2[elm].strip()
    if count == lim:
        final += word1 + " " + word2
    else:
        final += word1 + " " + word2 + "\n"
        count += 1
file3 = open("result2.txt","w")
file3.write(final)
file3.close()