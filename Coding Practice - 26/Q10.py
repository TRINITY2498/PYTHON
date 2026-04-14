n = int(input())
nums_list = []

for _ in range(n):
    
    commands = input().split()
    
    if commands[0] == "append":
        
        nums_list.append(int(commands[1]))
    
    elif commands[0] == "insert":
        
        nums_list.insert(int(commands[1]), int(commands[2]))
    
    elif commands[0] == "sort":
        
        nums_list.sort()
    
    elif commands[0] == "pop":
        
        nums_list.pop()
    
    elif commands[0] == "remove":
        
        nums_list.remove(int(commands[1]))
    
    elif commands[0] == "print":
        
        print(nums_list)

