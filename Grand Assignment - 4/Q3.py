# First Perfect Square.

m = int(input())
n = int(input())

for num in range(m, n + 1):
    
    if(num ** 0.5).is_integer():
        
        print(num)
        break 

else:
        
    print("No Perfect Square")