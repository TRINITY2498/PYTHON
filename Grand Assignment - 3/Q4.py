m, n = map(int, input().split())
matrix = []

for _ in range(m):
    
    row = list(map(int, input().split()))
    matrix.append(row)

for diagonal_sum in range(m + n - 1):
    
    diagonal = []
    
    for i in range(m):
        
        for j in range(n):
            
            if i + j == diagonal_sum:
                
                diagonal.append(matrix[i][j])
        
    print(" ".join(str(x) for x in diagonal))