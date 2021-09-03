try:
    a = int(input("Enter a number:"))
    b = int(input("Enter a number:"))
    c = a / b
    print(c)
except ValueError:
    print("Enter a valid number fool")
except ZeroDivisionError:
    print("Can not devide a number with zero fool")
except:
    print("There are other exeptions")
finally:
    print("bye Bye")