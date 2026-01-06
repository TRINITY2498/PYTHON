n = int(input())

for num in range(2,n + 1):
    Factors = 0
    for i in range(1, num + 1):
        if num % i == 0:
            Factors = Factors + 1
    if Factors == 2:
        print(num)
    
            
        