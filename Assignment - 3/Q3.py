a = input()
b = input()

first_three_char = ((a[0 : 3] == "DIS") or (b[0 : 3] == "DIS"))

if first_three_char:
    print("Discount")
else: 
    print("No Discount")