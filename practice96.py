def Chocolatey(st,en):
    st = st.split("/")
    en = en.split("/")
    for i in range(len(st)):
        d1 = int(st[i])
        d2 = int(en[i])
        if i == 0:
            dsum = d2 - d1
        elif i == 1:
            msum = d2 - d1
        else:
            ysum = d2 - d1
    final = dsum + msum * 20 + ysum*240 + 1
    return final
print(Chocolatey("3/8/2018", "10/8/2020"))
