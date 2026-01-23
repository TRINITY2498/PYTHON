n = int(input())
sum_non_prime = 0

for i in range(1,n + 1):
    is_prime = True
    a = int(input())
    
    if a <= 1:
        continue 
    
    for j in range(2,a):
        
        if a % j == 0:
            is_prime = False 
            break 
    
    if is_prime == False:
        
        sum_non_prime = sum_non_prime + a
            

print(sum_non_prime)