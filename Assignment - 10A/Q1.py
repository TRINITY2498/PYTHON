n = int(input())
count = 0
sum_of_count = 0

for i in range(1,n + 1):
    
    count = count + 1 
    sum_of_count = sum_of_count + len(str(count))
print(sum_of_count)
