num_set = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100}

numbers = input().split()

lis = []

for num in numbers:
    
    digit = int(num)
    
    num_set.discard(digit)


for element in num_set:
    
    lis += [element]

lis.sort()

print(lis)