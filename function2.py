# Display menu and return choice. 
# Store in variable and use this value to determine which function to call next.

# create a function that can be called to run the menu
def menuOptions():

# create the team list
    lstTeams = []

# # boolean and while loop that continues to display the menu while the boolean is true
    bCont = True
    while bCont == True:

# Menu input variable that displays the menu options and collects menu input
        try :
            iMenuOption = int( input( "Menu \n1. Start game \n2. Quit the Program \nEnter one of the numbers associated with the above options: "))

    # depending on the option input, an if statement will run a different set of code
            if iMenuOption == 1 : 
            # collect an integer that will loop the list append function
                iTeamCount = int( input("How many teams would you like to enter? "))
                for iCount in range(0, iTeamCount) :
            # start appending team names to the lstTeams list
                    sTeamName = input("Enter team name: ")
                    lstTeams.append(sTeamName)
                bCont = False
        # quit program by setting boolean to false and ending the while loop
            elif iMenuOption == 2 :
                print("The program has ended.")
                bCont = False

        # all other inputs are not accepted and will return the following message
            else:
                print("Input not accepted, please try again.")
        except :
            print("Input not accepted, please try again.")

    return lstTeams, iMenuOption
    # FOR FUTURE BUILD MORE OPTIONS FOR THE PROGRAM ONCE THE OTHER FUNCTIONS ARE FINISHED 

