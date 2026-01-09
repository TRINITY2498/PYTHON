n = int(input())

for i in range(1,n + 1):
    row = ""
    left_spaces = ( " " * ((n - i) * 2))
    print(left_spaces,end = "")
    for j in range(1,i + 1):
        row = ((str(j) + " ") + row)
    print(row)