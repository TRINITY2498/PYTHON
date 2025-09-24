a = input()

first_digit = int(a[0])
sec_digit = int(a[1])
third_digit = int(a[2])

same_digit = ((first_digit == sec_digit) and (sec_digit == third_digit))

print(same_digit)