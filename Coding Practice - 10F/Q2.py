n = int(input())
digit_mid = 0

for i in range(1,n + 1):
    mid = (2 * (n - i) - 2)
    if i == 1:
        row = ("# ") * n
    elif i == n:
        row = ("+ ")
    else: 
        row = ("+ ") + (" ") * mid + ("+ ")
    digit_mid = digit_mid + 2
    
    print(row)
 