n = int(input())
k = n
sum_k = 0

for i in range(0,n):
    sum_k = sum_k + k
    k = k - 1
    
for j in range(0,n):
    left_spaces = " " * (j * 2)
    print(left_spaces,end = "")
    
    for num in range(1,(n + 1) - j):
        print(str(sum_k) + " ",end = "")
        sum_k = sum_k - 1
    print()
    
        
        