#+:addition
#-:subtraction
#/:division
#*:multiplication
#%:modulus
#<:less-than
#>:greater-than
#<=:less-than-equal
#>=:greater-than-equal

#this line prints a string
print("I will now count my chickens:")

#this line print a string "Hens" and then uses proper order of operations to do 30/6 followed by 25+5
print("Hens", 25.0+30.0 / 6.0)
#this line print a string "Roosters" and then uses proper order of operations to do 25*3 followed by 75%4 followed by 100-3
print("Roosters", 100. - 25.0 * 3.0 % 4.0)

#this line prints a string
print("Now I will count the eggs:")
#this line prints the math done in parenthesis in order or operations. -1/4 then 4%2 then all addition and subtration
print(3.0 + 2.0 + 1.0 - 5.0 + 4.0 % 2.0 - 1.0 / 4.0 + 6.0)
#this line prints a string
print("Is it true that 3 + 2 < 5 - 7?")
#this line checks if 3+2 is less than 5-7 and returns False
print(3.0 + 2.0 < 5.0 - 7.0)
#this line prints a string, then prints 3+2
print("What is 3 + 2?", 3.0 + 2.0)
#this line prints a string, then prints 5-7
print("What is 5 - 7?", 5.0 - 7.0)
#this line prints a string
print("Oh, that's why it's False.")
#this line prints a string
print("How about some more.")
#this line prints a string then prints True or False of 5 > 2
print("Is it greater?", 5.0 > -2.0)
#this line prints a string then prints True of False for 5 >= -2
print("Is it greater or equal?", 5.0 >= -2.0)
#this line prints a string then prints True or False for 5 <= -2
print("Is it less or equal?", 5.0 <= -2.0)
