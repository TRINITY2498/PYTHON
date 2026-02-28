def count_the_vowels(word):
    count = 0
    for ch in word:
        
        if ch in ("aeiou"):
            
            count = count + 1
        
    print(count)


word = input()

result = count_the_vowels(word)
