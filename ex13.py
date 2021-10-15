from sys import argv
script, chicken, soup = argv

print("The first variable is called:", chicken)
print("Your second variable is called:", soup)
print("Your script is called:", script)

recipe = input("What soup would you like to make?\n\tChicken soup?\n\tBroccoli soup?\n\tRabbit soup?")

print("The recipe for", recipe, "is not too difficult.")
