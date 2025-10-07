n = int(input())
counter = 0 
digit = 1

while counter < n:
    counter = counter + 1
    print((str(digit)) * counter)
    digit = digit + 1
    while counter < n:
        counter = counter + 1
        print((str(digit)) * counter)
        digit = digit + 1