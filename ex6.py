#assigning integer 10 to a variable "types_of_people"
types_of_people = 10
#assigning a formatted string including a nested variable(string) to a variable "x"
x = f"There are {types_of_people} types of people."

#assigning a string to a variable "binary"
binary = "binary"
#assigning a string to a variable "do_not"
do_not = "don't"
#assigning a formatted string with two nested variables(string) to a variable "y"
y = f"Those who know {binary} and those who {do_not}."

#print variable "x"
print(x)
#print variable "y"
print(y)

#print a formatted string including a nested variable(string) "x"
print(f"I said: {x}")
#print a formatted string including a nested variable(string) "y" and adding single quotes around the "y" phrase
print(f"I also said: '{y}'")

#assigning a boolean False to a variable "hilarious"
hilarious = False
#assigning a string to a variable "joke_evaluation". not sure of what empty brackets inside the quote means.
joke_evaluation = "Isn't that joke so funny?! {}"
#printing a formatted "joke_evaluation" with "hilarious" as the parameter
print(joke_evaluation.format(hilarious))

#assigning a string to variable "w"
w = "This is the left side of..."
#assigning a string to variable "e"
e = "a string with a right side."

#print string "w" plus string "e", which puts them next to each other
print(w + e)
