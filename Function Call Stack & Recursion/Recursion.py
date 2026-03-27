def multiply_of(n):
    
    if n == 1:
        return 1
    return n * multiply_of(n - 1)
    
num = int(input())

result = multiply_of(num)
print(result)