m = int(input())
n = int(input())
index = 0

s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


for i in range(1,m + 1):
    
    for j in range(1,n + 1):
        
        if i == 1 or i == m:
            
            print(s[index],end = " ")
            index = index + 1
        
        elif j == 1 or j == n:
            print(s[index],end = " ")
            index = index + 1
        
        else:
            print(" ",end = " ")
            index = index + 1
    print()