n = input()

case_1 = int(n[0]) + int(n[1]) == 7
case_2 = int(n[0]) == 7 or int(n[1]) == 7
n = int(n)
case_3 = n % 7 == 0

result = case_1 or case_2 or case_3

if result:
    print("Special Number")
else:
    print("Normal Number")