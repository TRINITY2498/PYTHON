n = int(input())
L = []

for i in range(n):
    
    char = input()
    
    L = L + [char]
    
lis_1 = L[ : 3]
lis_2 = L[-3 : ]

print(lis_1 + lis_2)