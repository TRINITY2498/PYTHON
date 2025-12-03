n = int(input())

for i in range(1,n + 1):
    if i == 1:
        row = (". ")
    elif i == n:
        row = (". ") * n 
    else:
        row = (". ") + ("0 ") * (i - 2) + (". ")
    print(row)