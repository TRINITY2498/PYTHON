def get_transpose_of_matrix(matrix, m, n):
    
    transpose = [[matrix[j][i] for j in range(m)] for i in range(n)]
    
    return transpose


def print_max_min_sum_for_row_wise(num_list):
    
    row_max = [max(row) for row in get_transpose_of_matrix(num_list, m, n)]
        
    print(row_max)
    
    row_min = [min(row) for row in get_transpose_of_matrix(num_list, m, n)]
    
    print(row_min)
    
    row_sum = [sum(row) for row in get_transpose_of_matrix(num_list, m, n)]
    
    print(row_sum)


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

# Call the get_transpose_of_matrix function

# Call the print_max_min_sum_for_row_wise function

print_max_min_sum_for_row_wise(num_list)
