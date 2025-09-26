n = int(input())

div_by_2 = n % 2 != 0 
div_by_3 = n % 3 != 0 
div_by_5 = n % 5 != 0 
div_by_7 = n % 7 != 0 

result = div_by_2 and div_by_3 and div_by_5 and div_by_7 

if result: 
    print("True")
else: 
    print("False")