def count_of_uppercase(word):
    count = 0
    
    for ch in word:
        
        if ch.isupper():
            
            count = count + 1 

    return count

word = input()

result = count_of_uppercase(word)

print(result)