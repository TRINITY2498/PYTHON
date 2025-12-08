n = int(input())

mid = 0

for i in range(1,n + 1):
    left_space = (2 * n) - (2 * i)
    if i == 1:
        row = (" ") * left_space + ("* ")
    elif i == n:
        row = ("* ") * n 
    else:
        row = (" ") * left_space + ("* ") + (" ") * mid + ("* ")
        mid = mid + 2
    print(row)