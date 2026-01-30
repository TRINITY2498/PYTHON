n = int(input())

# Printing first Line 

left_spaces_count = n - 1
left_spaces = " " * left_spaces_count
row_output = left_spaces + "*"

print(row_output)

# Printing Upper Triangle

hollow_spaces_count = 1 

for row in range(2,n + 1):
    
    left_spaces_count = n - row 
    left_spaces = " " * left_spaces_count
    
    hollow_spaces = " " * hollow_spaces_count
    hollow_spaces_count = hollow_spaces_count + 2 
    
    row_output = left_spaces + "*" + hollow_spaces + "*"
    
    print(row_output)
    
# Printing Lower Triangle 

for row in range(1,n - 1):
    
    left_spaces_count = row 
    left_spaces = " " * left_spaces_count
    
    hollow_spaces_count = hollow_spaces_count - 3
    hollow_spaces = " " * hollow_spaces_count
    
    row_output = left_spaces + "*" + hollow_spaces + "*"
    
    print(row_output)
    
# Printing Last Line 

left_spaces_count = n - 1
left_spaces = " " * left_spaces_count
row_output = left_spaces + "*"

print(row_output)

