n = int(input())

for i in range(1,n + 1):
    
    a = int(input())
    
    if i == 1:
        
        maxi = a 
        print(maxi)
    
    elif maxi >= a:
        
        print(maxi)
    
    else:
        
        maxi = a 
        print(maxi)