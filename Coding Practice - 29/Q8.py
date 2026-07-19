n = int(input())
main_list = []
result = []
    
for _ in range(n):
    
    list_a = list(map(int, input().split()))
    
    main_list.append(list_a)

for list_a in main_list:
    
    if (len(list_a)) == (len(set(list_a))):
        
        result.append(list_a)

print(result)
