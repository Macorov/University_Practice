def even_odd_seperator(tup):
    oddlst = []
    evenlst = []
    for val in tup:
        if val % 2 == 0:
            evenlst.append(val)
        else:
            oddlst.append(val)
    oddlst = tuple(oddlst)
    evenlst = tuple(evenlst)
    print("even tuple:",evenlst)
    print("odd tuple",oddlst)
even_odd_seperator((1,4,6,7,8,11,16,19))