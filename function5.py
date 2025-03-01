# Mikelle Burnett
# function 5
# receive the home team data and display info

def display_team_record(lstGames, sHomeTeam):
    
    # Create variables to track wins and losses for final record
    iWins = 0
    iLosses = 0
    
    print("\nGame Results:")
    
    # Print the results for each game
    for iGame in range(0, len(lstGames)):
        
        # Put the info from the list into variables
        sAwayTeam, iHomeScore, iAwayScore, sOutCome = lstGames[iGame]

        # Print the results
        print(f"Game vs {sAwayTeam}\n{sHomeTeam}'s score: {iHomeScore} - {sAwayTeam}'s score: {iAwayScore}\nGame Outcome: {sOutCome}\n")
        
        # Track if each game is a win or loss
        if iHomeScore > iAwayScore :
            iWins += 1
        else :
            iLosses += 1

    # print final season record for home team
    print(f"Final season record: {sHomeTeam} {iWins}-{iLosses}")
