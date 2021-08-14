def function_name(lst):
    final = []
    count = 0
    for i in lst:
        if final.count(i) < 2:
            final.append(i)
        else:
            count += 1
    print("Removed:",count)
    return(final)
print(function_name([1, 2, 3, 3, 3, 3, 4, 5, 8, 8]))
print(function_name([10, 10, 15, 15, 20]))