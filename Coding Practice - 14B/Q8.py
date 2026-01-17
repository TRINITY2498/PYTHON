m = int(input())
n = int(input())
sum_p = 0

for i in range(m,n + 1):
    is_prime = True
    for j in range(2,i):
        
        if i % j == 0:
            is_prime = False 
            break
    if is_prime:
        sum_p = sum_p + i 

print(sum_p)
        