a = int(input())
b = int(input())

a_mod_b = a % b 
b_mod_a = b % a 

if a_mod_b < b_mod_a:
    print(a_mod_b)
else:
    print(b_mod_a)