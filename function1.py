#Aaron Garry
#Function 1 - Ask for name and dipslay a welcome message


def welcomeMessage():
    sName = input("What is your name?: ")
    print(f"Welcome {sName}, to the womens soccer season simulation!"
        "\n\nStart by entering the number of teams in the league and enter all the team names."
        "\nAfter that you will select one of the teams to be the home team."
        "\nOne by one, you will be promted with teams to play. Scores will be generated automaticaly." 
        "\nHave fun!\n")