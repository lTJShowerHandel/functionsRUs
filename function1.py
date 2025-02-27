#Aaron Garry
#Function 1 - Ask for name and dipslay a welcome message


def welcomeMessage():
    sName = input("What is your name?: ")
    print(f"Welcome, {sName} to the womens soccer season simulation! Start by entering the number of teams in the league then select one of the teams to be the home team.
        Follow the promts in the menue to run the simulation. Have fun! ")
    return sName

# Call the function
welcomeMessage()
