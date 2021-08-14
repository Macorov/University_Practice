def splitting_money(money):
    result = ""
    note500 = money // 500
    remain = money % 500
    note100 = remain // 100
    remain = remain % 100
    note50 = remain // 50
    remain = remain % 50
    note20 = remain // 20
    remain = remain % 20
    note10 = remain // 10
    remain = remain % 10
    note5 = remain // 5
    remain = remain % 5
    note2 = remain // 2
    remain = remain % 2
    note1 = remain // 1
    remain = remain % 1
    if note500 > 0:
        result+= "500 Taka: "+ str(note500)+" note(s)"+"\n"
           
    if note100 > 0:
        result+= "100 Taka: "+ str(note100)+" note(s)"+"\n"
        
    if note50 > 0:
        result+= "50 Taka: "+ str(note50)+" note(s)"+"\n"
        
    if note20 > 0:
        result+= "20 Taka: "+ str(note20)+" note(s)"+"\n"
        
    if note10 > 0:
        result+= "10 Taka: "+ str(note10)+" note(s)"+"\n"
        
    if note5 > 0:
        result+= "5 Taka: "+ str(note5)+" note(s)"+"\n"
    if note2 > 0:
        result+= "2 Taka: "+ str(note2)+" note(s)"+"\n"
        
    if note1 > 0:
        result+= "1 Taka: "+ str(note1)+" note(s)"+"\n"
        
    return result
num1 = int(input("Enter the amount of money: "))
print(splitting_money(num1))