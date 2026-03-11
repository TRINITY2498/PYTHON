def sum_of_cubes_m_to_n(m, n):
    
    sum_of_cube = 0
    
    for i in range(m,n + 1):
        
        sum_of_cube = sum_of_cube + (i ** 3)
    
    print(sum_of_cube)


m = int(input())
n = int(input())

sum_of_cubes_m_to_n(m,n)