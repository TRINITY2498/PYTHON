a = int(input())
b = int(input())

case_1 = ((a % 3 == 0) and (b % 3 == 0))
case_2 = ((a % 12 == 0) or (b % 12 == 0))

result = case_1 and case_2

if result:
    print("Pair")
else:
    print("Not a Pair")