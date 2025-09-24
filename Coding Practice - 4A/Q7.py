n = input()

first_digit = int(n[0])
second_digit = int(n[1])
n = int(n)

result = ((n % first_digit == 0) and (n % second_digit == 0))

if result:
    print(n * 2)
else:
    print(n)