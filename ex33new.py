def addition(n, s):
    numbers1 = range (0, n, s)
    for i in numbers1:
        print("Item: %d" %i)
    print(numbers1)

print(addition(14, 4))
