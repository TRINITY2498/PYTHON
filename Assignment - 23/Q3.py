def check_is_prime(m, n):
    
    for i in range(m,n + 1):
    
        count = 0
        
        for j in range(1,i + 1):
            
            if i % j == 0:
                
                count = count + 1
    
        if count == 2:
            print(i,end = " ")
        
m = int(input())
n = int(input())

check_is_prime(m,n)