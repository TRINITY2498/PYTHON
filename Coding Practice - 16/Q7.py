m = int(input())
n = int(input())
found_prime = False

for i in range(m,n + 1):
    
    is_prime = True 
    if i <= 1:
        continue 
    
    for j in range(2,i):
        
        if i % j == 0:
            is_prime = False
            break
            
    if is_prime:
        found_prime = True
        print(i)
        break 
    
if found_prime == False:
    print("No prime numbers in the given range")
