# Henry Tuttle - Group 7

# Display list of all teams and allow user to choose a team using the menu.
# Call the function again to let the user choose the opponent but do not display the team they chose previously.
# Remove that team from the list. 
# Allow the user to select an opponent, and return team name. 
# This function should receive a parameter but give it a default value if none is passed. 
# You can use this function for both choosing the home team and the opponent team.

# Function 3 with list of teams as parameter
def function3 (lstTeams = None) :
    
    # Create continue loop to keep running if a wrong team is entered
    bCont = True
    while bCont == True :
        # Show list of available teams
        print("Available teams:")
        for team in lstTeams:
            print(f"- {team}")

        # User selects a team from list
        sSelectedTeam = input( "Select a team: ")

        if sSelectedTeam in lstTeams:
            # Remove the chosen team from the list
            lstTeams.remove(sSelectedTeam)
            # Return the selected team and the updated list
            return sSelectedTeam, lstTeams
        else:
            print("Team not found, please try again.")

