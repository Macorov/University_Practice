file = open("bracufile1.txt",mode="r")
#if we dont mention a size it will read out the whole file 
m = file.read(11) #mentioning size 
print(m)
file = open("bracufile1.txt","a") #starts writing from the end of the text if file exist
file = open("bracufile1.txt","x") #if there is a file naming same as this then it will cause an error
print(file.readline()) # print the first line of the text
print(file.readline()) # print the second line of the text
lst = file.readlines() # make a list of text but there is a \n after every elements

file.close()