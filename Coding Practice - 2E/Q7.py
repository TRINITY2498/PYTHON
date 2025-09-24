a = input()

each_digit_greater = (int(a[0]) > 4) and (int(a[1]) > 4) and (int(a[2]) > 4)
first_digit_equals = (int(a[0]) == 6)

result = (each_digit_greater or first_digit_equals)

print(result)