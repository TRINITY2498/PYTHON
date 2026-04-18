n = input().split()
lis_even = []
lis_odd = []

for i in n:
    
    i = int(i)
    
    if i % 2 == 0:
        
        lis_even.append(i)
    
    else:
        
        lis_odd.append(i)

lis_even.sort()
lis_odd.sort()

print(lis_even)
print(lis_odd)
    