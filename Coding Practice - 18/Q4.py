x = float(input())
n = int(input())
sum_of_series = 0

for i in range(1,n + 1):
    
    term = (x ** i)
    
    sum_of_series = sum_of_series + term

round_of_sum = round(sum_of_series,4)

print(round_of_sum)