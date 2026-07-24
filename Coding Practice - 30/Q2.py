def convert_string_to_int(list_a):
    new_list = []
    for item in list_a:
        num = int(item)
        new_list.append(num)
    return new_list


m, n = input().split()
m, n = int(m), int(n)
num_list = []

for i in range(m):
    list_a = input().split()
    list_a = convert_string_to_int(list_a)
    num_list.append(list_a)

# Write your code here

row_maxes = [max(row) for row in num_list]

max_val = max(row_maxes)

for i in range(m):
    
    for j in range(n):
        
        if num_list[i][j] == max_val:
            
            row_index = i 
            
            col_index = j 
        
row = num_list[row_index]

print(row) 

col = []

for k in range(m):
    
    col.append(num_list[k][col_index])

print(col)
    



            