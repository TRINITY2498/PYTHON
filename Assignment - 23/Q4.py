def get_lower_and_upper_case_letters(word):
    
    for i in word:
        
        if i.isupper():
            
            print(i,end = "")
    
    print()
    
    for j in word:
        
        if j.islower():
            
            print(j,end = "")


word = input()

get_lower_and_upper_case_letters(word)
