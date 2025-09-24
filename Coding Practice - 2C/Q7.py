a = int(input())
b = int(input())

is_positive = (a > 0 and b > 0)
less_than = (a < 70 and b < 70)

result = (is_positive or less_than)

print(result)