try:
    file1 = open("task8.txt")
    lst1 = file1.readlines()
    dic = {}
    sum1 = 0
    for i in lst1:
        i = i.strip("\n")
        i = i.split(" ")
        dic[i[0]] = int(i[1])
        sum1 += int(i[1])
    print(dic)
    print(sum1)
except FileNotFoundError:
    print("Plese enter a proper file")
except IndexError:
    print("Plese enter the salary")
except ValueError:
    print("Salary cannot be string")
except Exception:
    print("There are some errors cannot run the code!")