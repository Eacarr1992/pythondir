#variable people, cars, trucks assigned the integers 30, 10, 25
people = 30
cars = 10
trucks = 25
#if statement looking for true or false of cars > people
if cars > people:
    #Print a string if there are more cars than people
    print("We should take the cars.")
#else if there are less cars than people, do this.
elif cars < people:
    #print a string if there are less cars than people
    print("We should not take the cars.")
#if there is neither more cars than people or less cars than people do this.
else:
    #print a string if cars are equal to people
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")
