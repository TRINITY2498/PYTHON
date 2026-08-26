# String Rotation Right.

s1 = input()
s2 = input()


if len(s1) != len(s2):
    
    print("No Match")

else:
    
    current = s1 
    
    matched = False 
    

    for i in range(len(s1)):
    
        if current == s2:
        
            print(i)
        
            matched = True 
        
            break
    
        current = current[-1] + current[ : -1]


    if not matched:
    
        print("No Match")