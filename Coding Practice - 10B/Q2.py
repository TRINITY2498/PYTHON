m = int(input())
n = int(input())
count = 0 

for i in range(m,n + 1):
    if i % 6 == 0:
        count = count + 1
        print(i,end = " ")
        
if count == 0:
    print("No Numbers Found")
