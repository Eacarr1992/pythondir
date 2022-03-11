def addition(n, s):
    i = 0
    numbers1 = [ ]
    while i < n:
        print(f"Item: %d" %i)
        numbers1.append(i)
        i = i + s
    print(numbers1)

print (addition(12, 3))
