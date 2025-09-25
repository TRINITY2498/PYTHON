n = int(input())

square = n * n 

square = str(square)
n = str(n)

last_digit_square = int(square[-1])
last_digit_n = int(n[-1])

result = last_digit_square == last_digit_n

if result:
    print("Equal")
else:
    print("Not Equal")