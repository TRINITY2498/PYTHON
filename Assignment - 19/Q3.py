n = int(input())


for i in range(1,n + 1):
    
    left_space = " " * (n - i) 
    hollow_space = " " * ((i - 1) * 2)
    
    print(left_space + "/" + hollow_space + "\\")
    

for j in range(n,0,-1):
    
    left_space = " " * (n - j) 
    hollow_space = " " * ((j - 1) * 2)
    
    print(left_space + "\\" + hollow_space + "/")
    
    