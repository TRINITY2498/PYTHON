n = int(input())
digit = 1
for i in range(1,n + 1):
    if i == 1:
        row = ("* ") * n 
    elif i == n:
        row = ("* ")
    else:
        mid = 2 * (n - i) - 2
        row = (("* ") + (" ") * mid + ("* "))
        digit = digit + 2
    print(row)