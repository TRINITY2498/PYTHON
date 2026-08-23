

board = []

for _ in range(3):
    
    board.append(input().split())


combos = [
    
    board[0], board[1], board[2],
    
    [board[0][0], board[1][0], board[2][0]],
    [board[0][1], board[1][1], board[2][1]],
    [board[0][2], board[1][2], board[2][2]],
    
    [board[0][0], board[1][1], board[2][2]],
    [board[0][2], board[1][1], board[2][0]],
    ]

for combo in combos:
    
    if all(c == 'O' for c in combo):
        
        print("Abhinav Wins")
        break
    
    elif all(c == 'X' for c in combo):
        
        print("Anjali Wins")
        break 
    
else:
        
    print("Tie")
    

    