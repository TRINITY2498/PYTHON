n = int(input())
counter = 0 
digit = 1
sum = 0

while counter < n: 
    square = (digit ** 2)
    digit = digit + 1 
    sum = sum + square
    counter = counter + 1
print(sum)