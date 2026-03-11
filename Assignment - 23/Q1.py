def calculate_league_points(wins, draws, losses):
    
    wins = wins * 4
    draws = draws * 2 
    losses = losses * 1 
    
    print(wins + draws - losses)


statistics = input().split(",")
wins = int(statistics[0])
draws = int(statistics[1])
losses = int(statistics[2])

calculate_league_points(wins,draws,losses)
