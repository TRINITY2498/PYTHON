a = int(input())
b = int(input())

cond_one = ((a + b) < 10)
cond_two = ((a - b ) < 10)
cond_three = (a > 5 and a < 30)

result = (cond_one or cond_two or cond_three)

print(result)