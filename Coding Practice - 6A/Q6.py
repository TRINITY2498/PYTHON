d = int(input())

zero_to_fifty = ((d > 0) and (d <= 50))
above_fifty = (d > 50)

if zero_to_fifty:
    score = d * 3
elif above_fifty:
    score = ((50 * 3) + (d - 50) * 5)

print(score)