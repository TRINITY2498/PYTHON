s = input().split()
lis = []

for num in s:
    
    count = s.count(num)
    
    num = int(num)
    
    if count % 2 != 0 and num not in lis:
        
        lis.append(num)

lis.sort()

print(lis)