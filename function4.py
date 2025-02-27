
# Function that recieves home team and away team
# Generates a score for each team
# Uses that score to determine game outcome

# Create function with parameters of home team and away team (home team parameter can potentially be removed)
def function4(awayTeam) :

    # Add random function for score generation
    import random

    # Create variables for home score and away score
    home = 0
    away = 0

    # Generate scores in a while loop that prevents ties
    while home == away :
        home = random.randrange(0,10)
        away = random.randrange(0,10)

    # Use the score to determine if the home team wins
    if home > away :
        
        # Outcome of the game is W for home team
        outcome = "W"
        
        # Add global variable for wins counter and increase it by 1
        global wins
        wins += 1
    
    # Use the score to determine if the home team loses
    else :
        
        # Outcome of the game is L for home team
        outcome = "L"

        # Add global variable for losses counter and increase it by 1
        global losses
        losses += 1
    
    # Create a list containg the home team name, away team name, home team score, away team score, and outcome for home team
    score = [awayTeam, home, away, outcome]

    # Return previously mentioned list
    return score
