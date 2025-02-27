# Henry Tuttle - Group 7

# Display list of all teams and allow user to choose a team using the menu.
# Call the function again to let the user choose the opponent but do not display the team they chose previously.
# Remove that team from the list. 
# Allow the user to select an opponent, and return team name. 
# This function should receive a parameter but give it a default value if none is passed. 
# You can use this function for both choosing the home team and the opponent team.

# Function 3 with list of teams as parameter
def function3 (lstTeams = None) :

    # Show list of available teams
    print( f"Available teams: {lstTeams}")
    
    sSelectedTeam = input( "Select a team: ")

    if sSelectedTeam in lstTeams:
        lstTeams.remove( sSelectedTeam)
    else:
        print( "Team not found, try again.")

    return sSelectedTeam