n = input()
k = len(n)
sm = 0

for i in n:
    sm = sm + (int(i) ** k)
print(sm)