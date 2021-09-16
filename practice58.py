my_dictionary={"Potato":12, "Onion":16, "Ginger":15, "Garlic":12, "Tomato":15}
word = input("Enter the groceries: ")
word = word.split(",")
try:
    sum1 = 0
    for elm in word:
        sum1 += my_dictionary[elm]
    print(sum1)
except NameError:
    print("Initialize the summation variable.")
except KeyError:
    print("Some groceries are not available in the dictionary.")
