n = int(input())

result = n % 11 == 0 or n % 11 == 1 

if result:
    print("Special Eleven")
else:
    print("Normal Number")