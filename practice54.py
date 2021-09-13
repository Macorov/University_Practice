file = open("task2.txt")
lst = file.readlines()
final = ""
for elm in lst:
    elm = elm.split()
    count = 0
    rep = len(elm) -1
    for val in elm:
        if count ==rep:
            final += val + "\n"
        else:
            final += val + " "
            count += 1
file2 = open("result2.txt","w")
file2.write(final)
file2.close()
