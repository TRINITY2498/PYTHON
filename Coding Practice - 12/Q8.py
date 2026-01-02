n = int(input())

factors = 2

for i in range(2,n):
    if n % i == 0:
        factors = factors + 1 

if factors == 2:
    print("Prime Number")
else:
    print("Not a Prime Number")