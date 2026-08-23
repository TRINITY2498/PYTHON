a = input().split()

k = int(input())

result = []

for item in a:
    
    if len(item) != k:
        
        result.append(item)

print(" ".join(result))