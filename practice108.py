sen1 = input("Enter a sentence: ")
sen2 = input("Enter a sentence: ")
sen1 = sen1.split(" ")
sen2 = sen2.split(" ")
count = 0
for elm in sen1:
    
    if elm in sen2:
        count += 1
per = (count/(len(sen1)+len(sen2)))*100
stper = str(per)
if stper[-1] == "0":
    stper = stper[:-2]
print("Common percentage: "+stper+"%")
if per >= 30:
    print("Plagiarism detected.")
else:
    print("Good job")