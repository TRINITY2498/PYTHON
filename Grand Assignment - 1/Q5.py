a = input()
b = input()

if a == "Rock" and b == "Scissors":
    print("Abhinav Wins")
elif a == "Rock" and b == "Paper":
    print("Anjali Wins")
elif a == "Rock" and b == "Rock":
    print("Tie")
elif a == "Scissors" and b == "Rock":
    print("Anjali Wins")
elif a == "Scissors" and b == "Paper":
    print("Abhinav Wins")
elif a == "Scissors" and b == "Scissors":
    print("Tie")
elif a == "Paper" and b == "Scissors":
    print("Anjali Wins")
elif a == "Paper" and b == "Rock":
    print("Abhinav Wins")
elif a == "Paper" and b == "Paper":
    print("Tie")