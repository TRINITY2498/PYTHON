m = int(input())
n = int(input())

for num in range(m,n + 1):
    if num == 0 or num == 1:
        continue
    is_prime = True
    
    for j in range(2,num):
        if num % j == 0:
            is_prime = False
            break 
    
    if is_prime:
        print(num)
        