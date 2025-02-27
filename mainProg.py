# Import functions
from function1 import welcomeMessage
from function2 import menuOptions
from function3 import function3
from function4 import function4
from function5 import display_team_record

# Call function 1
welcomeMessage()

# Call function 2, returns list of teams that is stored in variable lstTeams
lstTeams = menuOptions()

# Intialize wins/losses for function 4
wins = 0
losses = 0

# Function 3. Run first for home team, then loop for away teams. Returns select team from list.
sHomeTeam = function3(lstTeams)

# Removes selected team from list
if sHomeTeam in lstTeams:
    lstTeams.remove( sHomeTeam)
else:
    print( "Team not found, try again.")

# Intialize list of games
lstGames= []

# Loop and call function 3 for away teams
while len(lstTeams) > 0 :  
    sAwayTeam = function3(lstTeams)

    # Remove selected team
    if sAwayTeam in lstTeams:
        lstTeams.remove(sAwayTeam)
    else:
        print("Team not found, try again.")

    lstGames.append(function4(sAwayTeam))
    

# Function 4
function4()



#Function 5
display_team_record(lstGames, sHomeTeam)

