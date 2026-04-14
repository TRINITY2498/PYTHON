def fibonacci(n):
    if n <= 1:
        return n 
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def get_fibonacci_series(n):
    if n == 1:
        return [0]
    
    elif n == 2:
        return [0, 1]
    
    else:
    
        return get_fibonacci_series(n - 1) + [fibonacci(n - 1)]

n = int(input())

print(get_fibonacci_series(n))
