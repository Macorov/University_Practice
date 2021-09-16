def print_matrix_list(matrix):
    final = ""
    for i in range(len(matrix)):
        for k in range(len(matrix[i])):
            if i == len(matrix) - 1 and k == len(matrix[i])-1:
                final += str(matrix[i][k])
            elif k ==  len(matrix[i]) -1:
                final += str(matrix[i][k]) + "\n"
            else:
                final += str(matrix[i][k]) + " "
    return final
matrix= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(print_matrix_list(matrix))