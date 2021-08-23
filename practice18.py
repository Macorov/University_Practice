given_dict = { "Normal Skills":[10,10,10], "Ultimate Skill":30 }
sum1 = 0
for i in given_dict["Normal Skills"]:
    sum1 += i
sum1 += given_dict["Ultimate Skill"]
print("Additive Damagage Score is", sum1)
if sum1 <= 70:
    print("The agent's name is Rage")
elif sum1 > 70 and sum1 <= 100:
    print("The agent's name is Jett")
else:
    print("The agent's name is Sage")
