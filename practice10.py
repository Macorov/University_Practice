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
print(individul_bonus_calculation("Neymar", 1200000, 35, 5))
print(individul_bonus_calculation('Jamal', 700000, 19, 8))
print(individul_bonus_calculation('Luis', 80000, 25, 10))