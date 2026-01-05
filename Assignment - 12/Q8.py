m = int(input())
n = int(input())

for i in range(1,m + 3):
    if i == 1 or i == m + 2:
        row = "+" + "-" * n + "+"
    
    else:
        row = "|" + " " * n + "|"

    print(row)