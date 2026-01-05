n = int(input())

sum_of_even = 0 

for i in range(n + 1):
    if i % 2 == 0:
        sum_of_even = sum_of_even + i 
print(sum_of_even)