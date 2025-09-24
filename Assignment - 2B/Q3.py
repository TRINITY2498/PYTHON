a = int(input())
b = int(input())
c = int(input())

result = ((a + b > c) and (b + c > a) and (c + a) > b)

print(result)
