def shuffle_string(string, indexes_list):
    
    indexes_list = indexes_list.split()
    row = ""
    
    for i in indexes_list:
        
        i = int(i)
        
        row = row + string[i]
    
    return row


string = input()
indices_list = input()

result = shuffle_string(string,indices_list)
print(result)