def function_name(matrix_A , matrix_B):
    if len(matrix_A) != len(matrix_B):
        return "No of rows not same"
    for i in range(len(matrix_B)):
        if len(matrix_A[i]) != len(matrix_B[i]):
            return f"No of colums not same"
    flst = []
    temp = []
    sum1 = 0
    for i in range(len(matrix_A)):
        
        for k in range(len(matrix_A[i])):
            sum1 += matrix_A[i][k] + matrix_B[i][k]
            temp.append(sum1)
            sum1 = 0
        flst.append(temp)
        temp = []
    return flst
matrix_A = [ [1,5, 4] , [-4,3] ,[-4,0, 6]]
matrix_B = [ [2,-1, -3] , [4,-1, -4], [2,6] ]
print(function_name(matrix_A , matrix_B))