a = int(input())
b = int(input())

is_positive = ((a > 0) and (b > 0))
is_greater = ((a > 5) or (b > 5))

result = (is_positive and is_greater)
print(result)