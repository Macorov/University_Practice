file = open("task1.txt")
lst = file.readlines()

maxlen = None
maxword = None
count = 0
for elm in lst:
    elm = elm.strip()
    elm = elm.split()
    
    for val in elm:
        
        if count == 0:
            maxlen = len(val)
            maxword = val
            count += 1
        elif len(val) > maxlen:
            maxlen = len(val)
            maxword = val
print(maxword)
#rmsami