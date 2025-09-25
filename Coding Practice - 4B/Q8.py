n = input()

first_digit = int(n[0])
second_digit = int(n[1])
third_digit = int(n[2])

cube_first = first_digit ** 3
cube_second = second_digit ** 3
cube_third = third_digit ** 3

n = int(n)

result = cube_first + cube_second + cube_third == n

print(result)