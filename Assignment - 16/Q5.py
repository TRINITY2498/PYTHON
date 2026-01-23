n = int(input())
s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


for i in range(1,n + 1):
    index = 0
    left_space = "  " * (n - i) 
    print(left_space,end = "")
    
    for j in range(1,n + 1):
        if i == 1 and j == n:
            print(s[index],end = " ")
            index = index + 1
        elif i == n:
            print(s[index],end = " ")
            index = index + 1
        
        elif j > (n - i):
            print(s[index],end = " ")
            index = index + 1 
    print()