s = input()

case_1 = s[0 : 3] == "NXT"
case_2 = ((int(s[3 : ]) % 2 == 0) or (int(s[3 : ]) % 7 == 0))

result = case_1 and case_2

if result:
    print("Special String")
else:
    print("Not a Special String")
    