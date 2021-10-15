from sys import argv

script, user_name, alias = argv
pre_answer = "* "

print(f"Hi {user_name}(if that is your real name), I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {alias}?")
likes = input(pre_answer)

print(f"Where do you live {alias}?")
lives = input(pre_answer)

print("What kind of computer do you have?")
computer = input(pre_answer)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
