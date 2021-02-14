import os
import string
my_file = open("C:/Users/Karaken/Desktop/dom.txt")
my_string = my_file.read()
print("Было прочитано:")
print(my_string)
for my_file in string.punctuation:
    my_string = my_string.replace(".","")
    my_string = my_string.replace(",","")
    my_string = my_string.replace("!","")
    my_string = my_string.replace("?","")
    my_string = my_string.replace(":","")
    my_string = my_string.replace(";","")
    my_string = my_string.replace(" \ ","")
    my_string = my_string.replace("/","")
    my_string = my_string.replace("-","")
    my_string = my_string.replace("*","")
    my_string = my_string.replace("“ ","")
    my_string = my_string.replace("” ","")
    print(my_string)
    break


