a = input().split(",")
b = input().split(",")

set_a = set()
set_b = set()

intersection_lis = []

for num_a in a:
    
    digit_a = int(num_a)
    
    set_a.add(digit_a)

for num_b in b:
    
    digit_b = int(num_b)
    
    set_b.add(digit_b)

intersection = set_a & set_b

for element in intersection:
    
    intersection_lis += [element]
    
intersection_lis.sort()

print(intersection_lis)


    
    