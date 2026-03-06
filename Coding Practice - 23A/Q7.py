def sum_of_squares_m_to_n(m, n):
    
    sq = 0 
    
    for i in range(m,n + 1):
        
        sq = sq + (i ** 2)

    return sq 
    
m = int(input())
n = int(input())

print(sum_of_squares_m_to_n(m,n))
