my_list = [4, 2, 3, 1, 6, 5]
old_list = my_list.copy()
count = 0
remain = 0
for i in range(len(my_list)-1):
    min_index = i
    for j in range(i,len(my_list)):
        if my_list[j] < my_list[min_index]:
            min_index = j
    
    temp = my_list[min_index]
    my_list[min_index] = my_list[i]
    my_list[i] = temp


for i in old_list:
    if i != my_list[count]:
        remain += 1
    count += 1
print(remain)
