current_sem_data = {"John":[4.0,3.7,4.0], "Tom":[3.3,3.7,4.0], "Harry":[3.3,3.7,4.0]}
previous_sem_data = {"John":[3.88,90], "Tom":[3.52, 70], "Harry":[3.25,85]}
dic1 = {}
dic2 = {}
dic3 = {}
dicc = {}
dic4 = {}
for k,v in current_sem_data.items():
    m = len(v)
    v = sum(v)/len(v)
    dicc[k] = m*3
    dic1[k] = v
for k,v in previous_sem_data.items():
    temp = dic1[k] + v[0]
    temp = temp/2
    dic2[k] = temp
    dic3[k] = v[1] + dicc[k]
    dic4[k] = dic2[k] * 3
print(dic2)
print(dic3)
print(dic4)