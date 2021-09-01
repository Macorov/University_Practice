my_list = [10,1,20,3,6,2,5,11,15,2,12,14,17,18,29]
for i in range(len(my_list)):
    min_index = i
    for j in range(i,len(my_list)):
        if my_list[min_index] > my_list[j]:
            min_index = j
    temp = my_list[i]
    my_list[i] = my_list[min_index]
    my_list[min_index] = temp
print(my_list)