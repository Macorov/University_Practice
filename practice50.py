a = 5
b = 4

try:
    print("start")
    c = a/b #code will not execute from here if it has some sort of errors
    print(c)  
except Exception:
    print("Cannot devide by zero")
else:
    print("No exeption")   # if try blocks executes this block also get executed
finally:
    print("end") #it will execute no matter what
   

