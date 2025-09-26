n = int(input())

case_1 = (n % 5 == 0) and (n % 7 == 0)
case_2 = n < 7 

result = case_1 or case_2 

if result:
    print(n)
else: 
    print(n % 5)
    print(n % 7)
