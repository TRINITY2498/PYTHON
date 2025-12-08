n = int(input())

for i in range(1,n + 1):
    left =  n - i 
    if i == 1:
        row = (" ") * left + ("*")
    else:
        mid = (2 * i) - 3
        row = (" ") * left + ("*") + (" ") * mid + ("*")
    print(row)
    
for i in range(1,n):
    left =  i
    if i == (n - 1):
        row = (" ") * left + ("*")
    else:
        mid = 2 * (n - i) - 3
        row = (" ") * left + ("*") + (" ") * mid + ("*")
    print(row)