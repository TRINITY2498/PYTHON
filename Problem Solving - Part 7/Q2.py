n = int(input())
s = 5

for i in range(1,n + 1):
    if i == 1:
        row = ""
        row = row + (" " * (n - 1) + (str(s) + " "))
        print(row)
    
    elif i == n:
        row = ""
        for j in range(n):
            print(s + j, end = " ")
    
    else:
        row = ""
        left_space = n - i 
        mid =  2 * i - 4 
        
        row = row + (" " * left_space) + "5 " +  (" " * mid) + str(i + 4)
        print(row)    
     