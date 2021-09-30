lst = input("Enter a string: ")
lst = lst.split(" ")
nlst = []
slst = []
dic = {}

for i in lst:
    i = int(i)
    if i % 2 == 0:
        nlst.append(i)
k = max(nlst)
jj = ""
for i in range(len(nlst)):
    k = input("Enter a word: ")
    dic[k] = nlst[i]
    if nlst[i] == k:
        jj = k
print("Input list:",lst)
print("Even list: ",nlst)
print("Length of even list:",len(nlst))
print("Dictionary: ",dic)
print(jj)
    