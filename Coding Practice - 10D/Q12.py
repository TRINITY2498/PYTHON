n = int(input())

for i in range(1,n + 1):
    space1 =  (n - i) 
    space2 = (n - i) * 2 
    row = ((" ") * space1 + ("* ") * i + (" ") * space2 + ("* ") * i)
    print(row)