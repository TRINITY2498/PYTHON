a = int(input())
b = int(input())

less_than = (a < 60 or b < 60)
greater_than = (a > 80 or b > 80)

result = (less_than and greater_than)
print(result)