def convert_to_list(square_matrix_dict):
    lst = []
    for k,v in square_matrix_dict.items():
        lst.append(v)
    return lst
square_matrix_dict = {1 : [1,2,3] , 2 : [4,5,6] , 3 : [7,8,9] }
print(convert_to_list(square_matrix_dict))