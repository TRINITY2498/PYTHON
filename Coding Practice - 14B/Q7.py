n = int(input())

for i in range(1,n + 1):
    sum_k = 0
    a = int(input())
    k = str(a)
    len_k = len(k)
    
    for j in range(0,len_k):
        
        sum_k = sum_k + (int(k[j]) ** len_k)

    if sum_k == a:
        print(a)
        