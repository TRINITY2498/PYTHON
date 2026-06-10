n = int(input())

num_list = [(10, 20, 30), (1, 2), (5, 10, 15, 45)]

lis = []

for i in range(len(num_list)):
    
    new_tup = ()
    element_1 = num_list[i]
    
    for j in range(len(element_1)):
        
        if j == (len(element_1) - 1):
            
            new_tup += (n,) 
        
        else:
            
            new_tup += (element_1[j],)
    
    lis += [new_tup] 

print(lis)