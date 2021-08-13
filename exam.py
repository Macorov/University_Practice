val_1=input("Enter a string: ")
val_2=int(input("Enter a number: "))
val_3=input("Enter a word: ")
count=0
count_2=0
count_3=0
flag=True
for elm1 in val_1:
    count+=1
for elm1 in val_3:
    count_2+=1
if " " in val_1:
    flag=False
elif count>=val_2:
    for elm2 in val_3:
        if elm2 in val_1:
            count_3+=1

elif count<val_2:

    flag=False

if flag and count_2==count_3:
    print('"' +val_1+'"is a valid password')
else:
    print('"' +val_1+'"is an invalid password')
