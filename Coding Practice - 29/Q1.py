n = int(input())
list_main = []

for _ in range(n):
    
    list_a = list(map(int, input().split()))
    
    list_main.append(list_a)
    
print(list_main)
