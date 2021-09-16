word = input("Enter a number: ")
word = word.split(",")
num = int(input("Enter a number: "))
flst = []
count = 0
if num < len(word)/2:
    for i in range(len(word)//2):
        if i == 0:
            temp = word[0]
            word[0] = word[-1]
            word[-1] = temp
        elif count % num == 0:
            k = -count - 1
            temp = word[count]
            word[count] = word[k]
            word[k] = temp
        else:
            pass
        count +=1 
    print(word)
else:
    print("Step size is not suitable")