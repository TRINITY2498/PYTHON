d = int(input())

if d <= 40:
    score = d * 2
elif d > 40 and d <= 60:
    score = ((40 * 2) + (d - 40) * 4)
elif d > 60 and d <= 120:
    score = ((40 * 2) + (20 * 4) + (d - 60) * 6)
elif d > 120:
    score = ((40 * 2) + (20 * 4) + (60 * 6) + (d - 120) * 8)

bonus = 50
score = score + bonus
print(score)