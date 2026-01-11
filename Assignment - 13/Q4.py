n = int(input())
k = 0

for i in range(1,n + 1):
    left_space = " " * (n - i)
    print(left_space,end = "")
    for j in range(1,i + 1):
        print((str(j) + " "),end = "")
    print()
        
for p in range((n - 1), 0, - 1):
    k = k + 1
    left_space = " " * k
    print(left_space,end = "")
    for q in range(1,p + 1):
        print((str(q) + " "),end = "")
    print()