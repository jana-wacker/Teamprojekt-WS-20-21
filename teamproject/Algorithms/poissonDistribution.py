import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn
from scipy.stats import poisson, skellam
# importing the tools required for the Poisson regression model
import statsmodels.api as sm
import statsmodels.formula.api as smf

# load and read the csv data
data = pd.read_csv("Crawler.csv")
data.head()
# print(data)

###########################################################################################################

'''Take the input csv and process it.
Variables: csv data 

Function: 1. Select the required data content
          2. Rename each column
          3. print out the final data 

Replace the data with four columns, including home team, away team, home goals and away goals. 
'''


def encapsulation(data):
    data2 = data[['Team1', 'Team2', 'GoalsTeam1', 'GoalsTeam2']]
    final = data2.rename(columns={'GoalsTeam1': 'HomeGoals', 'GoalsTeam2': 'AwayGoals',
                                  'Team1': 'HomeTeam', 'Team2': 'AwayTeam'})
    final.head()
    return final


print(encapsulation(data))

#############################################################################################################

homeName = input("Please enter the home team name:")
guestName = input("Please enter the away team name:")

#############################################################################################################

'''Build a more general Poisson regression model
Variables: new data 

Function: 1. Separate home and away teams are drawn and two modules are created: 
             assume 1 for the home team and 0 for the away team.
          2. Define own side and the opponent's side to calculate.
          3. The output format is passion_model: whether home or not + own team + opponent, 
             and the result is calculated by the number of score.
'''


def goal_model(data):
    goal_model_data = pd.concat([data[['HomeTeam', 'AwayTeam', 'HomeGoals']].assign(home=1).rename(
        columns={'HomeTeam': 'team', 'AwayTeam': 'opponent', 'HomeGoals': 'goals'}),
        data[['AwayTeam', 'HomeTeam', 'AwayGoals']].assign(home=0).rename(
            columns={'AwayTeam': 'team', 'HomeTeam': 'opponent', 'AwayGoals': 'goals'})])

    poisson_model = smf.glm(formula="goals ~ home + team + opponent", data=goal_model_data,
                            family=sm.families.Poisson()).fit()
    return poisson_model


# print(goal_model(encapsulation(data)))

#############################################################################################################

'''Predict the scored by the home team
Variables: new data 

Function: 1. Use the previous Possion distribution model
          2. Estimated score based on user input of home team name
'''


def HomeTeamWin(data):
    PredictionHomeGoals = goal_model(data).predict(
        pd.DataFrame(data={'team': homeName, 'opponent': guestName, 'home': 1}, index=[1]))
    return PredictionHomeGoals


# print(HomeTeamWin(encapsulation(data)))

#############################################################################################################

'''Predict the scored by the away team
Variables: new data 

Function: 1. Use the previous Possion distribution model
          2. Estimated score based on user input of away team name
'''


def AwayTeamWin(data):
    PredictionAwayGoals = goal_model(data).predict(
        pd.DataFrame(data={'team': guestName, 'opponent': homeName, 'home': 0}, index=[1]))
    return PredictionAwayGoals


# print(AwayTeamWin(encapsulation(data)))

#############################################################################################################

'''Wrap this in a simulate_match function
Variables: possion_model, homeTeam, awayTeam 

Function: 1. We have two different possion distribution from home team and away team
          2. Use simulate_match to encapsulate these information together
          3. Use GoalRatio to show the procentage based on these two team score
'''


def simulate_match(foot_model, homeTeam, awayTeam, max_goals=10):
    home_goals_avg = foot_model.predict(pd.DataFrame(data={'team': homeTeam, 'opponent': awayTeam, 'home': 1},
                                                     index=[1])).values[0]
    away_goals_avg = foot_model.predict(pd.DataFrame(data={'team': awayTeam, 'opponent': homeTeam, 'home': 0},
                                                     index=[1])).values[0]
    team_pred = [[poisson.pmf(i, team_avg) for i in range(0, max_goals + 1)] for team_avg in
                 [home_goals_avg, away_goals_avg]]
    return (np.outer(np.array(team_pred[0]), np.array(team_pred[1])))


def GoalRatio(data):
    result = simulate_match(goal_model(data), homeName, guestName, max_goals=3)
    return result


# print(GoalRatio(encapsulation(data)))

#############################################################################################################

'''Predicte the procentage of home team win
Variables: new data 

Function: 1. Get the procentage based on the simulate_match
          2. the unten-right procentage is the ration of the home team win
'''


def PredictHomeTeamGoal(data):
    Home_sum = simulate_match(goal_model(data), homeName, guestName, max_goals=10)
    result = np.sum(np.tril(Home_sum, -1))
    return result


# print(PredictHomeTeamGoal(encapsulation(data)))

#############################################################################################################

'''Predicte the procentage of teams tied
Variables: new data 

Function: 1. Get the procentage based on the simulate_match
          2. the diagonale procentage is the ration of teams tied
'''


def PredictTied(data):
    Home_sum = simulate_match(goal_model(data), homeName, guestName, max_goals=10)
    result = np.sum(np.diag(Home_sum))
    return result


# print(PredictTied(encapsulation(data)))

#############################################################################################################
'''Predicte the procentage of away team win
Variables: new data 

Function: 1. Get the procentage based on the simulate_match
          2. the oben-left procentage is the ration of the away team win
'''


def PredictAwayTeamGoal(data):
    Home_sum = simulate_match(goal_model(data), homeName, guestName, max_goals=10)
    result = np.sum(np.triu(Home_sum, 1))
    return result


# print(PredictAwayTeamGoal(encapsulation(data)))

#############################################################################################################

'''The final method to print out the results 
Variables: new data 

Function: 1. Check if there are any matches, if not, tell user 
          2. If there are matches, create an array with all the results 
          Results: call all the definied methods above with the two variables, store output in array 
          3. print out the array with results 

Usage: To be called in the GUI button "Activate the AI" 

'''


# Method for the results to be called in the GUI button to predict results
def algoPrediction(data):
    result = {'Home Team': homeName,
              'Away Team': guestName,
              'Home team win ratio': PredictHomeTeamGoal(data),
              'Home and away team tie ratio': PredictTied(data),
              'Away team win ratio': PredictAwayTeamGoal(data),
              'Home team score': HomeTeamWin(data),
              'Away team score': AwayTeamWin(data)}
    print(result)


print(algoPrediction(encapsulation(data)))
