n = input()

first_digit = int(n[0])
sec_digit = int(n[1])
third_digit = int(n[2])
fourth_digit = int(n[3])

first_pow = first_digit ** 4 
sec_pow = sec_digit ** 4 
third_pow = third_digit ** 4
fourth_pow = fourth_digit ** 4

n = int(n)

sum_of_all = (first_pow + sec_pow + third_pow + fourth_pow) 

result = sum_of_all == n

if result:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")