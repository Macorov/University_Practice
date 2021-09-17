def function_name(lst):
    numlst = []
    chrlst = []
    flst = []
    for i in lst:
        if i.isalpha():
            chrlst.append(i)
        elif i.isdigit():
            numlst.append(i)
    if len(numlst) > len(chrlst):
        pcount = len(numlst)//len(chrlst)
        count = pcount
        prevcount = 0
        lowcount = 0
        lim = len(numlst)//2
        for i in range(lim):
            for k in range(prevcount,count):
                flst.append(numlst[k])
            flst.append(chrlst[lowcount])
            prevcount = count
            count += pcount
            lowcount += 1
            if lowcount > len(chrlst):
                flst += numlst[prevcount::-1]
                break
    elif len(numlst) < len(chrlst):
        pcount = len(chrlst)//len(numlst)
        count = pcount
        prevcount = 0
        lowcount = 0
        lim = len(chrlst)//pcount
        for i in range(lim):
            for k in range(prevcount,count):
                flst.append(chrlst[k])
            try:
                flst.append(numlst[lowcount])
            except:
                pass
            prevcount = count
            count += pcount
            lowcount += 1
            if lowcount > len(numlst):
                flst += chrlst[prevcount:-1] 
                flst +=  chrlst[-1]
                break


    return flst
print(function_name(['r', 'g', '3', 'u', 's', 'f', '8', '6', 's', 'a', 'f', 'i']))