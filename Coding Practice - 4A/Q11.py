n = int(input())

case_1 = n % 6 == 0
case_2 = n % 3 == 0
case_3 = n % 2 == 0

if case_1: 
    print("Number is divisible by 6")
elif case_2:
    print("Number is divisible by 3")
elif case_3:
    print("Number is divisible by 2")
else:
    print("Number is not divisible by 2, 3 or 6")
    