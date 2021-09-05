sitting_list = [10,30,20,70,11,15,22,16,58,100,12,56,70,80]
for i in range(0,len(sitting_list),2):
    min_index = i
    for j in range(i,len(sitting_list),2):
        if sitting_list[j] < sitting_list[min_index]:
            min_index = j
    temp = sitting_list[min_index]
    sitting_list[min_index] = sitting_list[i]
    sitting_list[i] = temp
for i in range(1,len(sitting_list),2):
    max_index = i
    for j in range(i,len(sitting_list),2):
        if sitting_list[j] > sitting_list[max_index]:
            max_index = j
    temp = sitting_list[max_index]
    sitting_list[max_index] = sitting_list[i]
    sitting_list[i] = temp
print(sitting_list)

