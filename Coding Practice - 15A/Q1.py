n = int(input())

for i in range(1,n + 1):
    
    for j in range(1,i + 1):
        
        print("*",end = " ")
    
    print()
    
for p in range(1,n + 1):
    
    for q in range(n,p,-1):
        
        print("*",end = " ")
    print()