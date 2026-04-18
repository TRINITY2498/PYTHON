n = int(input())

list_b = []

for _ in range(n):
    
    s = input().split()
    
    for i in range(len(s)):
        
        list_b.append(s[i])

list_b.sort()

print(list_b)    
    
    