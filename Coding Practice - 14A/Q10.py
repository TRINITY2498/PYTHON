n = int(input())

for i in range(1,n + 1):
    cols = n - i + 1
    for j in range(1,cols + 1):
        if i == 1:
            print(j,end = " ")
        
        elif j == 1:
            print(j,end = " ")
        
        elif j == cols:
            print(j,end = " ")
        else:
            print(" ", end = " ")
    print()