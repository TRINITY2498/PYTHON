n = int(input())
L = []

for i in range(n):
    
    a = int(input())
    
    if a % 5 == 0:
        
        L = L + [a]

print(L)
        