a = input()

first_digit = int(a[0])
sec_digit = int(a[1])
third_digit = int(a[2])

case_1 = ((first_digit > 7) and (sec_digit > 7) and (third_digit > 7))
case_2 = ((first_digit * sec_digit <= 30) and (sec_digit * third_digit <= 30) and (third_digit * first_digit <= 30))

result = (case_1 or case_2)

print(result)