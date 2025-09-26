n = int(input())

years = int(n / 365)
remaining_days = (n % 365)
weeks = int(remaining_days / 7)
days = int(remaining_days % 7)

print(years)
print(weeks)
print(days)