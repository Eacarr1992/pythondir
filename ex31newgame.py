print("""Welcome to Two Roosters!\nWhat would you like today?\nWe have the following options available:
\t*1. Peppermint Crack Bar
\t*2. Moravian Sugar Cookie
\t*3. Butterscotch Haystack
\t*4. Non Dairy Cranberry Orange Sorbet
\t*5. Whiskey Pecan
\t*6. Bourbon Eggnog Latte""")

first_choice = input(": ")

if first_choice == "1" or first_choice == "5":
    print("Employee angrily points to 'Masks Required' sign and says nothing.")
    print("What do you do?")
    print("1. Flip her off and leave.")
    print("2. Comply and re-order.")

    angry = input(": ")

    if angry == "1":
        print("No ice cream for you. Freedom in tact.")
        print("Good choice!")
    elif angry == "2":
        print("Enjoy your ice cream, commie.")

else:
    print("That isn't what you would normally order.\nAre you feeling alright?")
    print("1. Yes")
    print("2. No")

    feeling = input(": ")

    if feeling == "1":
        print("Ok great! Enjoy your nasty ice cream.")
    elif feeling == "2":
        print("That's too bad. I hope this cheers you up.*hands over ice cream*")
