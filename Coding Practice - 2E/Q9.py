a = input()

first_digit = int(a[0])
sec_digit = int(a[1])
third_digit = int(a[2])

case_1 = ((first_digit == 1) or (sec_digit == 1))
case_2 = ((first_digit + sec_digit + third_digit) < 12)
case_3 = (third_digit == 5)

result = (case_1 and case_2 and case_3)

print(result)