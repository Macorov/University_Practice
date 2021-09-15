file1 = open("task7.txt")
lst1 = file1.readlines()


lim = len(lst1) - 1
dic = {}
flst = []
for i in lst1:

    k = i.strip("\n")
    k = k.split(",")
    flst.append(k)
    

count = 0
hscore_count = 0
hlife_count = 0
hkill_count = 0
hscore = None
hlife = None
hkill = None
namelst = []
for i in flst:
    namelst.append(i[0])
    score = int(i[1])
    life = int(i[2])
    kill = int(i[3])
    if hscore ==None:
        hscore_count = count
        hscore = score
    elif  score> hscore:
        hscore = score
        hscore_count = count
    else:
        pass
    if hlife == None:
        hlife_count = count
        hlife = life
    elif life < hlife:
        hlife_count = count
        hlife = life
    else:
        pass
    if hkill == None:
        hkill = kill
        hkill_count = count
    elif kill <hkill:
        hkill = kill
        hkill_count = count
    else:
        pass
    count += 1

hname = None
hname_count = 0
count = 0
for i in namelst:
    count = 0
    for k in namelst:
        if i == k:
            count += 1
        if count > hname_count:
            hname = i
            hname_count = count
score_str ="Name: "+ flst[hscore_count][0]+", Score:"+ str(hscore)+'\n'
lives_str ="Name: "+ flst[hlife_count][0]+", Lives used:"+ str(hlife)+"\n"
game_str ="Name: "+ hname + ", Games Played:"+ str(hname_count)+"\n"
file2 = open("result3.txt","w")
file2.write(score_str)
file2.write(lives_str)
file2.write(game_str)
file2.close()
