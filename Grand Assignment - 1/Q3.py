n = int(input())

year = n // 365
remaining_days = n % 365

weeks = remaining_days // 7

days = remaining_days % 7

print(year,"years",weeks,"weeks",days,"days")