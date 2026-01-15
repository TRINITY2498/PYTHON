n = int(input())
s = 5 

for i in range(1,n + 1):
    if i == 1:
        row = "" 
        row += (" " * (n - i) + str(s)) + " "
        print(row)
    
    elif i == n:
        s = 5
        row = ""
        for j in range(1,n + 1):
            row =  str(s) + " "
            s = s + 1
            print(row,end = "")
    
    else:
        row = ""
        left_space = n - i 
        mid = 2 * i - 4
        s = s + 1
        row +=  (" " * left_space) + "5 " + " " * mid + str(s)
        print(row)