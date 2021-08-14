def show_palindrome(num):
    final = ""
    count = 0
    for i in range(1,num+1):
        i = str(i)
        final += i
        count += 1
    for i in range(1,num):
        count -= 1
        final += str(count)
    return final
print(show_palindrome(5))
print(show_palindrome(3))