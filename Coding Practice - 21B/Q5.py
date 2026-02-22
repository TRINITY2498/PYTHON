s = input()

words = s.split()

len_words = len(words)

if len_words % 2 != 0:
    
    len_words = len_words + 1 
    
len_words = len_words // 2

print(words[ : len_words])

    
    
    
    
    
    