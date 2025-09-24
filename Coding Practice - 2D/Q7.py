a = int(input())
b = int(input())

is_negative = ((a < 0 ) or (b < 0))
is_equals = ((a * b ) >= -46)

print(is_negative and is_equals)