n = int(input())

for i in range(1,n + 1):
    
    a = int(input())
    
    if i == 1:
        
        print(a)
        smallest_so_far = a
    
    elif smallest_so_far >= a:
        
        smallest_so_far = a 
        print(smallest_so_far)
    
    else:
        
        print(smallest_so_far)
        
    

        
        