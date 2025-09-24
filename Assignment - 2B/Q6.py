m = int(input())
p = int(input())
c = int(input())

case_1 = ((m >= 35) and (p >= 35) and (c >= 35))
case_2 = ((m + p >= 90) or (p + c >= 90) or (m + c) >= 90)

result = case_1 and case_2

print(result)