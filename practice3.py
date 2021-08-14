def fibonacci(num):
    count = 0
    a = 0
    b = 1
    if num == 1:
        print(a)
    else:
        print(a,end=" ")
        print(b,end=" ")
        for i in range(2,num):
            count = a + b
            a = b
            b = count
            print(count,end=" ")

    print("") 
fibonacci(10)