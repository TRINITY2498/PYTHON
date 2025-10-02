d = int(input())

if d <= 50:
    score = d * 3
elif d > 50 and d <= 100:
    score = ((50 * 3) + (d - 50) * 5)
elif d > 100 and d <= 200:
    score = ((50 * 3) + (50 * 5) + (d - 100) * 6)
elif d > 200: 
    score = ((50 * 3) + (50 * 5) + (100 * 6) + (d - 200) * 10)

bonus = 100 
score = bonus + score 

print(score)