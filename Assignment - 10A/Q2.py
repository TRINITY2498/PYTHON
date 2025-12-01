x = int(input())
n = int(input())
neg_digit = -1 
power = 1
ans = 0

for i in range(1,n + 1):
    neg_digit = neg_digit * (-1)
    formula = (neg_digit * (x)) ** ((power))
    ans = ans + formula
    power = power + 2 
print(ans)