n = int(input())
out_counter = 0
in_counter = 0
digit = 1
in_digit = 1

while out_counter < n:
    out_counter = out_counter + 1 
    print((str(digit)) * out_counter)
    digit = digit + 1 
while in_counter < n:
    in_counter = in_counter + 1 
    print((str(in_digit)) * in_counter)
    in_digit = in_digit + 1 