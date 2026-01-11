m = int(input())
n = int(input())
found = False 

for i in range(m,n + 1):
    sum_k = 0
    s = str(i)
    k = len(s)
    for j in range(k):
        digit = s[j]
        sum_k = sum_k + (int(digit) ** k)
    
    if sum_k == i:
        print(i,end = " ")
        found = True
  
if found == False:
    print("-1")