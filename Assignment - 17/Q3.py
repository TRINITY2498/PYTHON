n = int(input())
sum_of_n = 0.0

for i in range(1,n + 1):
    
    sum_of_n = sum_of_n + (1 / (i))
    
result = round(sum_of_n,2)

print(result)
    