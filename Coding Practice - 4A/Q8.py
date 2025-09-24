n = input()

case_1 = int(n) % 9 == 0
case_2 = int(n[0]) == 9 or int(n[1]) == 9

result = case_1 or case_2

if result:
    print("Lucky Number")
else:
    print("Unlucky Number")