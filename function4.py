
# Function that recieves home team and away team
# Generates a score for each team
# Uses that score to determine game outcome

# Create function with parameters of home team and away team (home team parameter can potentially be removed)
def function4(sAwayTeam) :

    # Add random function for score generation
    import random

    # Create variables for home score and away score
    iHomeScore = 0
    iAwayScore = 0

    # Generate scores in a while loop that prevents ties
    while iHomeScore == iAwayScore :
        iHomeScore = random.randrange(0,10)
        iAwayScore = random.randrange(0,10)

    # Use the score to determine if the home team wins
    if iHomeScore > iAwayScore :
        
        # Outcome of the game is W for home team
        lstOutcome = "W"

    # Use the score to determine if the home team loses
    else :
        
        # Outcome of the game is L for home team
        lstOutcome = "L"

    
    # Create a list containg the home team name, away team name, home team score, away team score, and outcome for home team
    lstScore = [sAwayTeam, iHomeScore, iAwayScore, lstOutcome]

    # Return previously mentioned list
    return lstScore
