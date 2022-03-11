print("""You enter a dark room with two doors.
Do you go through door #1, door #2, or door #3?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

elif door == "3":
    print("""This door is safe.\nYou walk through and your mother makes you a grilled cheese.""")
    print("...but then a ninja breaks in.")
    print("What do you do?")
    print("1. Run away.")
    print("2. Turn on the tv and hope he goes away.")

    ninja = input("> ")

    if ninja == "1":
        print("You run away but the ninja throws a star into your back.")
        print("Great job!")
    else:
        print("Your television tactics were very effective!")
        print("You and the ninja watch anime until you fall asleep.")
        print("Great job!")

else:
    print("You stumble around and fall on a knife and die. Good job!")
