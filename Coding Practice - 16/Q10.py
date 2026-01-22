m = int(input())
n = int(input())

if m > n:
    big = m 
elif n > m:
    big = n 
else:
    big = m 
    
for i in range(big,m * n + 1):
    
    if i % m == 0 and i % n == 0:
        print(i)
        break