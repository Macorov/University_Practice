try:
    word = input("Enter your equation: ")
    lst = ["+","-","/","%","*"]
    flag = True
    op = ""
    sum1 = 0
    for i in word:
        if i in lst:
            op = i
            word = word.split(i)
            flag = False
            break
    if len(word) > 2:
        raise IndexError
    if flag:
        raise RuntimeError
    if op == "+":
        for i in word:
            i = int(i.strip())
            sum1 += i
    elif op == "-":
        sum1 = int(word[0].strip()) - int(word[1].strip())
    elif op == "/":
        sum1 = int(word[0].strip()) / int(word[1].strip())
    elif op == "%":
        sum1 = int(word[0].strip()) % int(word[1].strip())
    elif op == "*":
        sum1 = int(word[0].strip()) * int(word[1].strip())
    else:
        raise RuntimeError
    print(sum1)
except IndexError:
    print("Input does not contain 3 elements/Wrong operator")
except ValueError:
    print("Input does not contain numbers.")
except RuntimeError:
    print("Input does not contain 3 elements/Wrong operator")
except ZeroDivisionError:
    print("You cannot devide anything by Zero")
except Exception:
    print("There are some errors")