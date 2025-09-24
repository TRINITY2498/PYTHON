a = input()

first_two = (a[ :2] == "19")

last_two = int(a[2 :])
last_two_check = (30 < last_two < 60)

result = first_two and last_two_check

print(result)