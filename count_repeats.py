i = 1
counter = 0
while i < 32:
    counter = counter + 1
    if 32%i == 0:
        print i, "is a factor of 32", counter
    else:
        print i, "is not a factor of 32", counter
