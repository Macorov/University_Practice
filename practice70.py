def convert_to_diagonal(square_matrix_dict):
    lst = []
    final = ""
    for k,v in square_matrix_dict.items():
        lst.append(v)
        for i in range(len(v)):
            if i == len(v) - 1:
                final += str(v[i]) + "\n"
            else:
                final += str(v[i]) + " "
    print("Non-diagonal matrix:")
    print("In list of list format:",lst)
    print("in orginal square format:")
    
    print(final,end="")
    print("================")
    dlst = []
    dfinal = ""
    count = 0
    for i in range(len(lst)):
        temp = []
        for k in range(len(lst[i])):
            if k == count:
                temp.append(lst[i][k])
                if k == len(lst[i])-1:
                    dfinal += str(lst[i][k]) + "\n"
                else:
                    dfinal += str(lst[i][k]) + " "
            else:
                temp.append(0)
                if k == len(lst[i])-1:
                    dfinal += str(0) + "\n"
                else:
                    dfinal += str(0) + " "
        dlst.append(temp)
        count += 1
    print("Diagonal matrix:")
    print("In list of list format:",dlst)
    print("in orginal square format:")
    print(dfinal,end="")
square_matrix_dict = {1 : [1,2,3] , 2 : [4,5,6] , 3 : [7,8,9] }
convert_to_diagonal(square_matrix_dict)