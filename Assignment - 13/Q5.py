n = int(input())
count = 0
for i in range(1,n + 1):
    is_div = False
    for j in range(2,11):
        if i % j == 0:
            is_div = True
            break
          
    if is_div == False:
        count = count + 1
        
print(count)