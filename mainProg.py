# IS303 - 004
# Team 7: Aaron Garry, Blane Santilli, Henry Tuttle, Asher Swartzberg, Mikellle Burnett, Silviano Gaona
# Functions R Us Women's Soccer Project
# Program asks for user's name then starts the game which gets them to input the teams and runs a soccer season simulation

# Import functions
from function1 import welcomeMessage
from function2 import menuOptions
from function3 import function3
from function4 import function4
from function5 import display_team_record

# Call function 1
welcomeMessage()
bCont = True

while bCont == True :
    # Call function 2, returns list of teams that is stored in variable lstTeams
    lstTeams, iMenuOption = menuOptions()

    if iMenuOption == 1 :
        # Function 3. Run first for home team, then loop for away teams. Returns select team from list.
        print("\nChoose a home team:")
        sHomeTeam, lstTeams = function3(lstTeams)

        # Intialize list of games
        lstGames= []

        # Loop and call function 3 for away teams
        while len(lstTeams) > 0 :  
            print(f"\nChoose team for {sHomeTeam} to play:")
            sAwayTeam, lstTeams = function3(lstTeams)

            # Call Function 4 to generate scores for the match between home team and chosen away team
            lstGames.append(function4(sAwayTeam))

        # Call Function 5 to display the game outcomes and season record for home team
        display_team_record(lstGames, sHomeTeam)

        # Create a boolean variable for play again message loop
        bCont2 = True
        while bCont2 == True :

            #try and except to deal with incorrect inputs
            try :

                # Give user a menu with options to play again and get input of number assosicated with choice
                iPlayAgain = int(input("\nWould you like to play again?\n1. Yes\n2. No\nEnter number assoicated with choice: "))
                if iPlayAgain == 1 :
                    print("Go again:")
                elif iPlayAgain == 2 :

                    # End both loops which ends the program
                    print("Thanks for playing!")
                    bCont = False
                    bCont2 = False
                else :
                    print("Input not accepted, please try again.")
            except :
                print("Input not accepted, please try again.")

    # End the loop which ends the program if quit the program menu option was chosen
    else :
        bCont = False
