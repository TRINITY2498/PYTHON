o = input()
a = int(input())
b = int(input())

plus = (o == "+")
sub = (o == "-")
prod = (o == "*")
div = (o == "/")
mod = (o == "%")

if plus:
    print(a + b)
elif sub:
    print(a - b)
elif prod:
    print(a * b)
elif div:
    print(a / b)
elif mod:
    print(a % b)