n = input()
case_1 = ((int(n[0]) != 5) or (int(n[1]) != 5) or (int(n[2]) != 5))
n = int(n)
case_2 = ((n > 300) and (n < 700))

if (case_1 and case_2):
    print("Valid Number")
else:
    print("Not a Valid Number")
    