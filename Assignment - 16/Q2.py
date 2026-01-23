n = int(input())

for i in range(1,n + 1):
    is_prime = True
    a = int(input())
    if a <= 1:
        continue
    
    for j in range(2,a):
        
        if a % j == 0:
            is_prime = False
    
    if is_prime:
        print(a)
        break