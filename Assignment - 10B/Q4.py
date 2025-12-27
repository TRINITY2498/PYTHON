a = int(input())
b = int(input())
count = 0 

for i in range(1,b + 1):
    sq = (i ** 2)
    
    if sq >= a and sq <= b:
        count = count + 1
        if sq > b:
            break
print(count)