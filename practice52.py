def getNumber():
    try:
        return 12
    finally:
        return 1
x = getNumber()
#print(x)
def feedback():
    try:
        f(x,4)
    finally:
        print("Feedback 1")
    print("Feedback 2")
#feedback()
def temp():
    try:
        print("try block: ")
        return 1
    finally:
        print("finally block: ")
        return 2
#k = temp()
#print(k)
def temp1():
    try:
        print("try block")
    finally:
        print("finally block: ")
#temp1()
try:
    num1 =int(input("enter a number"))
    num2 = int(input("enter another number "))
    print(num1/num2)
except Exception:
    print("Some Exception",end="||")
except ValueError:
    print("enter integer",end="||")
except ZeroDivisionError:
    print("2nd number cannot be zero",end="||")    