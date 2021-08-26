numbers = [-1,-12,64,2,0,222]
numbers = sorted(numbers) # outer place sort
numbers = sorted(numbers,reverse=True) #it will reverse 
final = numbers.sort(reverse=True)
print(final) # it will return none
print(numbers) # it will return sorted list so final = numbers.sorted() was not necessary
