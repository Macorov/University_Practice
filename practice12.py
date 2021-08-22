def individul_bonus_calculation(name,year,goal,percent):
    final = 0
    if goal < 20:
        final = goal * ((percent/100)*year)
    elif goal >=20 and goal <= 30:
        final = goal * ((percent/100)*year) + 5000
    else:
        final = goal * ((percent/100)*year) + 10000
    try:
        final = int(final)
    except:
        final = final
    return f"{name} earned a bonus of {final} Taka for {goal} goals."
def all_in_one(*player):
    sum = ""
    count = 0
    for i in player:
        count += 1
    count = count 
    for i in range(0,count,4):
        a = player[i]
        b = player[i+1]
        c = player[i+2]
        d = player[i+3]
        if i+4 == count:
            sum += individul_bonus_calculation(a,b,c,d)
        else:
            sum += individul_bonus_calculation(a,b,c,d) + "\n"
    return sum
print(all_in_one("Neymar", 1200000, 35, 5, 'Jamal', 700000, 19, 8, 'Luis', 80000, 25, 10))