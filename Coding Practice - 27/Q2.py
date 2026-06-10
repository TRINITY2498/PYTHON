numbers = input().split()

set_a = set()
lis = []

for num in numbers:
    
    digit = int(num)
    
    set_a.add(digit)

for element in set_a:
    
    lis += [element]
    
lis.sort()

print(lis)