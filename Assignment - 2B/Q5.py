a = int(input())
b = int(input())

is_less = ((a < 20) or (b < 20))
is_greater = ((a > 30) or (b > 30))

result = is_less and is_greater 

print(result)