n = int(input())

s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


for i in range(n,0,-1):
    
    for j in range(0,i):
        
        print(s[j],end = " ")
    
    print()
    