#This line imports argv module from sys
from sys import argv
#This line defines the arguments as variables script and filename
scipt, filename = argv
#This line creates variable txt and assigns the open command to the variable filename
txt = open(filename)
#this line prints a string and formats the variable filename to be inside the quotes
print(f"Here's your file {filename}:")
#this line prints the variable txt with the .read command to show the plain text of the file
print(txt.read())
#this line prints a string
print("Type the filename again:")
#this line assigns an input to the variable file_again
file_again = input ("> ")
#this line assigns the open text of file_again as the variable txt_again
txt_again = open(file_again)
#this line prints the read command of the open file_again variable
print(txt_again.read())
