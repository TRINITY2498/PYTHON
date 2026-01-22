m = int(input())
n = int(input())

if m < n:
    small = m 
elif m > n:
    small = n

elif m == n:
    small = m 
    
for i in range(small,0,-1):
    
    if m % i == 0 and n % i == 0:
        print(i)
        break
