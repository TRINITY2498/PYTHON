s = input()

first_space_index = 0

for char in s:
    
    if char == " ":
        
        break 
    else:
        first_space_index = first_space_index + 1
    
first_word = s[ :first_space_index]

upper_word = first_word.upper()

new_sentence = upper_word + s[first_space_index : ]

print(new_sentence)