n = int(input())

counter = 0
digit = n + 1 

while counter < n:
    diff = digit - 1
    digit = digit - 1
    counter = counter + 1 
    print(diff)