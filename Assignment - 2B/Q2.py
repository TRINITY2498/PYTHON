a = int(input())
b = int(input())

sum_of = (a + b < 0)
prod_of = (a * b < 0)

result = sum_of or prod_of 

print(result)