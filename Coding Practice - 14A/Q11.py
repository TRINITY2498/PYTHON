n = int(input())

for i in range(1,n + 1):
    left_space = " " * (n - i)
    print(left_space,end = "")
    
    for j in range(1,i + 1):
        
        if i == 1:
            print("* ",end = "")
        
        elif i == n:
            print("* ", end = "")
        
        elif i == j or j == 1:
            print("* ",end = "")
        
        else:
            print(" ",end = " ")
    
    print()
        