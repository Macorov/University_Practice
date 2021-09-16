try:
    day = (input("Enter no of days: "))
    month = (input("Enter no of moths: "))
    if day.isdigit() and month.isdigit():
        day = int(day)
        month = int(month)
        distance = 0
        if day > 31 or month > 12:
            raise ValueError
        if day < 10:
            distance = 5+((day*2)/month)
        else:
            distance = 3 + (day/month)
        print(distance,"kilometres")
    else:
        raise TypeError
except ZeroDivisionError:
    print("0 is not a valid month")
except TypeError:
    print("Please do not enter any string as input")
except ValueError:
    if day > 31 and month > 12:
        print(day,"is not a valid day nor the",month, "is a valid month")
    elif day > 31:
        print(day,"is not a valid day of any month")
    else:
        print(month,"is not a valid month")
except:
    print("Other errors")