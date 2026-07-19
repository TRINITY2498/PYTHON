num_list = [(1, 2, 3, 4, 5, 6), (2, 4, 6, 8), (1, 3, 5, 7)]

n = int(input())

main_list = []

for num in num_list:
    
    list_a = list(num)
    
    if n in list_a:
        list_a.remove(n)
    
    tup = tuple(list_a)
    
    main_list.append(tup)

print(main_list)