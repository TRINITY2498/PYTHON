s = int(input())
n = int(input())

for i in range(1,n + 1):
    for j in range(1,n + 1):
        
        if i == 1 or i == n:
            print(s,end = " ")
            s = s + 1 
        
        elif j == 1 or j == n:
            print(s,end = " ")
            s = s + 1 
        
        else: 
            print(" ",end = " ")
            s = s + 1
    print()
        