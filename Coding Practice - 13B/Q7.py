n = int(input())

for i in range(1,n + 1):
    for j in range(1,i + 1):
        row = str(j) + " "
        print(row,end = "")
    
    for k in range(1,i):
        row = str(k) + " "
        print(row, end = "")
    print()
    
        