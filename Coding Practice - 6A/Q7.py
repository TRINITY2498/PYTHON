d = int(input())

if d <= 20:
    score = d * 2 
elif d > 20 and d <= 60:
    score = ((20 * 2) + (d - 20) * 4)
elif d > 60:
    score = ((20 * 2) + (40 * 4) + (d - 60) * 6)

bonus = 30 
score = score + bonus 
print(score)