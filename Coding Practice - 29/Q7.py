n = int(input())

first_index_list = []
second_index_list = []


for _ in range(n):
    
    tup = tuple(map(int, input().split()))
    
    first_index = tup[0]
    second_index = tup[1]
    
    first_index_list.append(first_index)
    second_index_list.append(second_index)


first_index_tuple = (max(first_index_list), min(first_index_list))
second_index_tuple = (max(second_index_list), min(second_index_list))

print(first_index_tuple)
print(second_index_tuple)
    
    