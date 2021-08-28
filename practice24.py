lst = input("Enter a list: ")
lst = lst.split(", ")
final = {}
nlst = []
for i in lst:
    i = int(i)
    if i % 2 ==0:
        if 'Divisible by 2' not in final.keys():
            final['Divisible by 2'] = [i]
        else:
            nlst = final['Divisible by 2']
            nlst.append(i)
            final['Divisible by 2'] = nlst
    if i % 3 == 0:
        if 'Divisible by 3' not in final.keys():
            final['Divisible by 3'] = [i]
        else:
            nlst = final['Divisible by 3']
            nlst.append(i)
            final['Divisible by 3'] = nlst
    if i % 5 == 0:
        if 'Divisible by 5' not in final.keys():
            final['Divisible by 5'] = [i]
        else:
            nlst = final['Divisible by 5']
            nlst.append(i)
            final['Divisible by 5'] = nlst
    elif i % 2 != 0 and i % 3 != 0 and i % 5 !=0:
        if "None" not in final.keys():
            final["None"] = [i]
        else:
            nlst = final["None"]
            nlst.append(i)
            final["None"] = nlst
print(final)