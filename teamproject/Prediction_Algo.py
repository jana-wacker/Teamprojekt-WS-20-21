# Class for defining Teams
class Team:
    """
    Creates a team.
    """

    def __init__(self, name, val, win, exp, comp):
        """
        Initialises a new object as a team consisting of:
        * Name (string): Name of the team
        * Value (int): Team member value in total (€)
        * WinRate (float): Percentage of overall win rate of the last 3 seasons
        * Experience (int): Number of games played in total
        * Complete (boolean): Are there injured or excluded players in team
        """

        self.name = name
        self.value = val
        self.winrate = win
        self.experience = exp
        self.complete = comp

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

    def get_winrate(self):
        return self.winrate

    def get_experience(self):
        return self.experience

    def get_complete(self):
        return self.complete


#Two test teams for the calculation
team1 = Team("FC Bayern", 9999999, 100, 10, True)
team2 = Team("VfB Stuttgart", 555555, 50, 5, False)


# Predicts winner based on team value
def predict_winner(team1, team2):
    if Team.get_value(team1) < Team.get_value(team2):
        return print("Vermutlich gewinnt", Team.get_name(team2))
    else:
        return print("Vermutlich gewinnt", Team.get_name(team1))

#I removed that, because it is run in the main file
#predict_winner(team1, team2)

