n = int(input())
k = n 

for i in range(0,n):
    left_space = " " * i 
    print(left_space,end = "")
    for j in range(1,k + 1):
        print((str(j) + " "),end = "")
    k = k - 1
    print()
    