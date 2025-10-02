n = int(input())

week_start = n in [1,2]
mid_week = n in [3,4,5]
weekend = n in [6,7]

if week_start:
    print("Week Start")
elif mid_week:
    print("Midweek")
elif weekend:
    print("Weekend")