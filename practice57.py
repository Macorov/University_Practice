def rangeditector(num):
    my_list=[10,20,30,40,60,100,2,5]
    try:
        final = my_list[num]
        print(final)
    except IndexError:
        print("Index out of range")
    finally:
        print("Program ended")
num = int(input("Enter a number: "))
rangeditector(num)