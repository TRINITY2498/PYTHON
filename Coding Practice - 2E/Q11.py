m = int(input())
p = int(input())
c = int(input())

case_1 = ((m + p >= 100) or (p + c >= 100) or (c + m >= 100))
case_2 = (m + p + c >= 180)

result = case_1 and case_2

print(result)