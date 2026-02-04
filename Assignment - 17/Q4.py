a = int(input())
b = int(input())
c = int(input())

d = (b ** 2 - 4 * a * c)

r_1 = (-b + d ** 0.5) / (2 * a)

r_2 = (-b - d ** 0.5) / (2 * a)

print(round(r_1,2))
print(round(r_2,2))