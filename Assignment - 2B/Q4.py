n = input()
first_digit = int(n[0])
n = int(n)
is_between = ((n > 50) and (n < 100))
is_greater = (first_digit == 7)

result = is_between or is_greater

print(result)