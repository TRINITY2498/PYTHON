n = int(input())
L = []

for i in range(n):
    
    a = int(input())
    
    L = L + [a]
    

for j in range(2):
    
    lis1 = L[ :2]

for k in range(2):
    
    lis2 = L[(len(L) - 2) : ]


print(lis1 + lis2)