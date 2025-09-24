m = int(input())
p = int(input())
c = int(input())

case_1 = ((m >= 60) and (p >= 50) and (c >= 45) and (m + p + c >= 180))
case_2 = ((m + p >= 120) or (c + p >= 110))

result = case_1 or case_2

print(result)

