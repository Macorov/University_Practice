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
def show_palindromic_triangle(num):
    space = num - 1
    final = ""
    for i in range(1,num+1):
        if i == num:
            final += space*" " + show_palindrome(i)
        else:
            final += space*" " + show_palindrome(i) + "\n"
        space -= 1
    print(final)
show_palindromic_triangle(3)