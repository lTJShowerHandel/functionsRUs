# function 5
# receive the home team data and display info

def display_team_record(lstGames, homeTeam):
    print("Game Results:")
    for game in lstGames():
        awayTeam, home, away, outcome = game # unpack the list
        print(f"Game vs {awayTeam} - {homeTeam}'s score: {home}, {awayTeam}'s score: {away}, {outcome}")
    
    global wins
    global losses

    # print final season record for home team
    print(f"Final season record: {homeTeam} {wins}-{losses}")
