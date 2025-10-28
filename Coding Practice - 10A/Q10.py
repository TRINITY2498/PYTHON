n = int(input())
sm = 0

for i in range(1,n):
    if n % i == 0:
        sm = sm + i 
if sm == n:
    print("Perfect Number")
else:
    print("Not a Perfect Number")