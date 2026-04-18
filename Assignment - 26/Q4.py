s = input().split()
lis = []

for ch in s:
    
    lis.append(ch)
    
    if ch[0] == "a":
        
        lis.remove(ch)
    
print(lis)


    