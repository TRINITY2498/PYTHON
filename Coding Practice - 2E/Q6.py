a = int(input())
b = int(input())
c = int(input())

sum_greater_than = ((a + b > 10) and (b + c > 10) and (c + a > 10))
print(sum_greater_than)