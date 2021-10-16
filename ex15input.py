filename = input("What is your file name?")
txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())
print("Please type your file name again.")

file_again = input("> ")
txt_again = open(file_again)

print(txt_again.read())
