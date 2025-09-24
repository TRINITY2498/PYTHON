m = int(input())
p = int(input())

is_greater_than_35 = ((m > 35) and (p > 35))
sum_is_greater_than_100 = (m + p >= 100)

if (is_greater_than_35 or sum_is_greater_than_100):
    print("Qualified")
else:
    print("Not Qualified")
    