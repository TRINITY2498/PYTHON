m = int(input())
n = int(input())
count = 0
sum_of_num = 0

for i in range(m,n + 1):
    
    # calculating count 
    
    count = count + 1 
    
    # calculating sum 
    
    sum_of_num = sum_of_num + i 

# calculating Average 

avg_of_sum = sum_of_num / count 

# printing sum and Avg 

print(sum_of_num)
print(avg_of_sum)