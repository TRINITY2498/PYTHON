list_a = [('apple', 'banana', 'orange', 'grapes'), ('cricket', 'football', 'hockey'), ('car', 'bicycle', 'bus')]

n = int(input())
main_list = []

for i in range(n):
    
    index = list(map(int, input().split()))
    
    a = index[0]
    b = index[1]

    main_list.append(list_a[a][b] )

print(main_list)
        
        
        
    