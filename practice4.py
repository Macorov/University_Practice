def function_name(days):
    years = days//365
    remain = days%365
    months = remain // 30
    remain = remain % 30
    print(years,"years,",months,"months and",remain,"days")
num1 = int(input("Enter a number: "))
function_name(num1)    