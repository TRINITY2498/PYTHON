first_string = input()
subsequence = input()

subseq_index = 0 # red arrow 

subseq_len = len(subsequence)

for char in first_string: # blue arrow
        
        # check if red arrow and blue arrow point to the same string.
        
        if char == subsequence[subseq_index]:
            
            subseq_index += 1 # red arrow increases  
            
            if subseq_index == subseq_len:
                break 

if subseq_index == subseq_len:
    
    print("Yes")

else:
    
    print("No")
     
    
