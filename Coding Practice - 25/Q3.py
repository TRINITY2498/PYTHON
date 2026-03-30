def compute_factorial(n):
    
    if n == 0:
        return 1 
    
    else:
        
        return n * compute_factorial(n - 1)


num = int(input())

factorial = compute_factorial(num)

print(factorial)
