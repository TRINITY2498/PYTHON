first_string = input()

subsequence = input()

len_subseq = len(subsequence)

index_subseq = 0 

for ch in first_string:
    
    if ch == subsequence[index_subseq]:
        
        index_subseq += 1
    
    if index_subseq == len_subseq:
        break 
    
if index_subseq == len_subseq:
    
    print("Yes")

else:
    
    print("No")