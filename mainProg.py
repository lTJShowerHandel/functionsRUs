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
        print("\n6 foot dungeons, chill bot")
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


    # Loop to prompt user to play again
        valid_input_received = False
        while not valid_input_received:
            play_again = input("\nWould you like to play again? (yes/no): ").lower()
            if play_again == 'yes':
                valid_input_received = True  # Valid input received; exit loop
            elif play_again == 'no':
                print("Thanks for playing!")
                valid_input_received = True  # Valid input received; exit loop
                bCont = False  # Exit the main loop
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
    else:
        print("Goodbye.")
        bCont = False  # Exit the main loop
