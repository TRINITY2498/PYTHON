m = int(input())
p = int(input())
c = int(input())

cond_one = ((m >= 70) and (p >= 60) and (c >= 60))
cond_two = ((m + p + c) >= 180)

result = (cond_one or cond_two)

print(result)