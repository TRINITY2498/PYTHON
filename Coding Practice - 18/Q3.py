n = int(input())
s = float(input())
sum_of_a = 0

for i in range(n):
    # Taking n inputs
    a = float(input())
    
    # finding sum of A 
    sum_of_a = sum_of_a + a 

# Rounding sum at N decimals
round_of_sum = round(sum_of_a,3)

# Comparing and printing output
if round_of_sum == s:
    print("True")
else:
    print("False")