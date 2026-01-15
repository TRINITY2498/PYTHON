n = int(input())

for i in range(1,n + 1):
    left_space = (2 * n) - (2 * i)
    print(" " * left_space,end = "")
    for j in range(1,i + 1):
        if i == n:
            print(i - j + 1,end = " ")
            
        elif j == 1:
            print(i,end = " ")
        
        elif j == i:
            print(1,end = " ")
        
        else:
            print(" ",end = " ")
    print()