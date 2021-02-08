"""This module contains code to predict the outcome of a match based on Linear Regression.
It returns the probability of home team and away team winning, the probability of a draw and how many
goals each team will most likely score."""
# use for plotting data
import pandas as pd

pd.set_option('display.max_columns', 10)
import matplotlib.pyplot as plt
# %matplotlib inline
import numpy as np
# Used for Regression Modelling
from sklearn.linear_model import LinearRegression
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from tkinter.messagebox import showinfo


#################################################################################################

def homeAndguest(homeName, guestName, data):
    """
    Variables: data from crawler

    Function: 1. Find the designated team (either a home team or an away team)
              2. Mark 1 in the home_or_away column if it is a home team, otherwise 0
              3. Pick out 'Team1','Team2','GoalsTeam1','GoalsTeam2' and 'home_or_away' columns to form a new dataFrame.

    Usage: Filter out user-specified football teams"
    """
    # Create a column titled home or away. This column will add a 1 to the row  where the played at home
    # and a 0 for away games.
    final = data.loc[((data['Team1'] == homeName) & (data['Team2'] == guestName)) |
                     ((data['Team1'] == guestName) & (data['Team2'] == homeName))]
    final.loc[:, ('home_or_away')] = np.where(final.loc[:, ('Team1')] == homeName, 1, 0)
    final = final.filter(['Team1', 'Team2', 'GoalsTeam1', 'GoalsTeam2', 'home_or_away'])
    final = final.dropna()
    final.head()
    return final

#################################################################################################

def matchCount(homeName, guestName, data):
    """
    Variables: data from homeAndguest

    Function: 1. If the number of matches is greater than 0, this outputs the result,
                 otherwise it outputs 0.

    Usage: Calculate the number of matches played by a given team"
    """
    count = homeAndguest(homeName, guestName, data).shape[0]
    if count > 0:
        return count
    else:
        return 0

#################################################################################################

def percentage(homeName, guestName, data):
    """
    The home team percentage is Home team score divided by the total score,
    As there is a possibility that the two teams are tied 0:0, the total in this case is +1.

    Variables: data from homeAndguest

    Function: 1. Calculate the total score, if the total score is 0 (0:0), output 1,
                 otherwise output the corresponding result.
              2.Calculate the percentage of home team wins (home team score divided by total score).
              3.Calculate the average of 2 times the percentage.
              4.The tiedPercentage is 1, where the GoalsTeam1 is equal to GoalsTeam2, otherwise 0.
              5.Construct a new dataFrame, including 'home_or_away','HomeWinPercentage',
                '2_percentage_avg' and 'tiedPercentage'.

    Usage: Data processing to find the data for calculating percentages"
    """
    final = homeAndguest(homeName, guestName, data)
    final['total']= np.where(final['GoalsTeam1']+final['GoalsTeam2']==0, 1, final['GoalsTeam1']+final['GoalsTeam2'])
    final['HomeWinPercentage']=final['GoalsTeam1']/final['total']
    final['2_percentage_avg']=final.HomeWinPercentage.rolling(window=2).mean()
    final['tiedPercentage'] = np.where(final['GoalsTeam1'] == final['GoalsTeam2'], 1, 0)
    final = final.fillna(final.mean())
    final.head()
    df=final[['home_or_away','HomeWinPercentage','2_percentage_avg','tiedPercentage']]
    df.loc[:,('home_or_away')] = df.loc[:,('home_or_away')].astype('float64')
    df.loc[:, ('tiedPercentage')] = df.loc[:, ('tiedPercentage')].astype('float64')
    return df

###############################################################################################

def predicatePercentage(homeName, guestName, data):
    """
    Variables: data from percentage

    Function: 1.Composition of linear programming templates. Impact factors include 'home_or_away'and'2_percentage_avg',
            the result is 'HomeWinPercentage'.
          2.Calculating intercepts and slopes.
          4.Calculate the percentage of home team wins, the percentage of away team wins
            and the percentage of draws respectively.

    Usage: Calculate the percentage of home and away team wins respectively.
    """
    df=percentage(homeName, guestName, data)
    X = pd.DataFrame(df, columns=['home_or_away','2_percentage_avg','tiedPercentage'])
    Y = pd.DataFrame(df, columns=['HomeWinPercentage'])
    # WITH a random_state parameter:
    # (Same split every time! Note you can change the random state to any integer.)
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=1)
    # Create linear regression model
    lin_reg_mod = LinearRegression()
    # Fit linear regression
    lin_reg_mod.fit(X_train, Y_train)
    # Make prediction on the testing data
    return lin_reg_mod


def percentageIntercept(homeName, guestName, data):
    """
    Variables: data， homeName, guestName

    Function: 1.Using linear regression model (from predicatePercentage) to derive intercepts.

    Usage: Obtain the intercept for calculating the percentage.
    """
    intercept = predicatePercentage(homeName, guestName, data).intercept_
    return intercept[0]


def percentageCoefhomeoraway(homeName, guestName, data):
    """
    Variables: data， homeName, guestName

    Function: 1.Using linear regression model (from predicatePercentage) to derive coefficient of home_or_away.

    Usage: Obtain the coefficient for calculating the percentage.
    """
    coef_home_or_away = predicatePercentage(homeName, guestName, data).coef_[0][0]
    return coef_home_or_away


def percentageCoefavg(homeName, guestName, data):
    """
    Variables: data， homeName, guestName

    Function: 1.Using linear regression model (from predicatePercentage) to derive coefficient of average of last two scores.

    Usage: Obtain the coefficient for calculating the percentage.
    """
    coef_percentage_avg = predicatePercentage(homeName, guestName, data).coef_[0][1]
    return coef_percentage_avg


def percentageCoeftied(homeName, guestName, data):
    """
    Variables: data， homeName, guestName

    Function: 1.Using linear regression model (from predicatePercentage) to derive coefficient of draw.

    Usage: Obtain the coefficient for calculating the percentage.
    """
    coef_percentage_tied = predicatePercentage(homeName, guestName,data).coef_[0][2]
    return coef_percentage_tied


def homePercentage(homeName, guestName, data):
    """
    Variables: data， homeName, guestName

    Function: 1.The final linear equation is obtained by intercept and slope.
                percentage = intercept + coefficient1 * 1
                             + coefficient2 * average percentage of last 2 matches
                             + coefficient3 * 0
              2.If the percentage is negative, then take zero.
              3.If the percentage is more than 1, then take 1.

    Usage: Get the final percentage of the home team.
    """
    df = percentage(homeName, guestName, data)
    homePercentagePre = percentageIntercept(homeName, guestName, data) \
                        + percentageCoefhomeoraway(homeName, guestName, data) * 1 \
                        + percentageCoefavg(homeName, guestName, data) * df['2_percentage_avg'].values[-1] \
                        + percentageCoeftied(homeName, guestName,data) * 0
    if homePercentagePre < 0:
        homePre = 0
    elif homePercentagePre > 1:
        homePre = 1
    else:
        homePre = homePercentagePre
    return homePre


def awayPercentage(homeName, guestName, data):
    """
    Variables: data， homeName, guestName

    Function: 1.The final linear equation is obtained by intercept and slope.
                percentage = intercept + coefficient1 * 0
                             + coefficient2 * average percentage of last 2 matches
                             + coefficient3 * 0
              2.If the percentage is negative, then take zero.
              3.If the percentage is more than 1, then take 1.

    Usage: Get the final percentage of the away team.
    """
    df = percentage(homeName, guestName, data)
    awayPercentagePre = percentageIntercept(homeName, guestName, data) \
                        + percentageCoefhomeoraway(homeName, guestName, data) * 0 \
                        + percentageCoefavg(homeName, guestName, data) * df['2_percentage_avg'].values[-1]\
                        + percentageCoeftied(homeName,guestName,data) * 0
    if awayPercentagePre < 0:
        awayPre = 0
    elif awayPercentagePre > 1:
        awayPre = 1
    else:
        awayPre = awayPercentagePre
    return awayPre


def tiedPrecentage(homeName, guestName, data):
    """
    Variables: data， homeName, guestName

    Function: 1.The final linear equation is obtained by intercept and slope.
                percentage = intercept + coefficient1 * 0
                             + coefficient2 * average percentage of last 2 matches
                             + coefficient3 * 1
              2.If the percentage is negative, then take zero.
              3.If the percentage is more than 1, then take 1.

    Usage: Get the final percentage of draw.
    """
    df = percentage(homeName, guestName, data)
    tiedPre = percentageIntercept(homeName, guestName, data) \
              + percentageCoefhomeoraway(homeName, guestName, data) * 0 \
              + percentageCoefavg(homeName, guestName, data) * df['2_percentage_avg'].values[-1] \
              + percentageCoeftied(homeName, guestName, data) * 1
    if tiedPre < 0:
        tiedPre = 0
    elif tiedPre > 1:
        tiedPre = 1
    else:
        tiedPre = tiedPre
    return tiedPre

def sumofPercentage(homeName, guestName, data):
    """
        Variables: data， homeName, guestName

        Function: 1.Calculate the sum of all percentages.

        Usage: Make sure the sum of all percentage is not 0. That is easy for the final output.
        """
    sum=(homePercentage(homeName, guestName, data)
         +awayPercentage(homeName, guestName, data)
         +tiedPrecentage(homeName, guestName, data))
    return sum

def ratioHomeWin(homeName, guestName, data):
    """
    Variables: data， homeName, guestName

    Function: 1.Calculate the home team win ratio.

    Usage: Make sure the sum of home team win ratio, away team win ratio and draw ratio is 1.
    """
    homeWinRatio=homePercentage(homeName, guestName, data)\
                 /sumofPercentage(homeName, guestName, data)
    return homeWinRatio


def ratioAwayWin(homeName, guestName, data):
    """
    Variables: data， homeName, guestName

    Function: 1.Calculate the away team win ratio.

    Usage: Make sure the sum of home team win ratio, away team win ratio and draw ratio is 1.
    """
    awayWinRatio=awayPercentage(homeName, guestName, data)\
                 /sumofPercentage(homeName, guestName, data)
    return awayWinRatio


def ratioTied(homeName, guestName, data):
    """
    Variables: data， homeName, guestName

    Function: 1.Calculate the tied ratio.

    Usage: Make sure the sum of home team win ratio, away team win ratio and draw ratio is 1.
    """
    tiedRatio=tiedPrecentage(homeName, guestName, data)\
              /sumofPercentage(homeName, guestName, data)
    return tiedRatio

###############################################################################################

def predict(homeName, guestName, data):
    """
    Variables: data from homeAndguest， homeName, guestName

    Function: 1.Pre-processed data using the homeAndguest method.
              2.Check the count of matches, if the matches is less than 2, show the infomation:
                "Prediction - Linear Regression",
                "Sorry, the data is incomplete and cannot be used for prediction! "
                "Please choose other teams or time!"
              3.Otherwise, output the score and percentage using linear Regression.

    Usage: Output the results.
    """
    final = homeAndguest(homeName, guestName, data)
    if ((matchCount(homeName, guestName, final) <= 2) | (sumofPercentage(homeName, guestName, data)==0)):
        showinfo("Prediction - Linear Regression",
                 "Sorry, the data is incomplete and cannot be used for prediction! "
                 "Please choose other teams or time!")
    else:
        result = {'Home Team': homeName,
                  'Away Team': guestName,
                  'Home team win ratio': ratioHomeWin(homeName, guestName, data),
                  'Home and away team tie ratio': ratioTied(homeName, guestName, data),
                  'Away team win ratio': ratioAwayWin(homeName, guestName, data)}
        output = homeName + ' vs. ' + guestName + "\n" + "\n" + \
                 'Probability of Home Team winning: ' + \
                 str(round(result['Home team win ratio'] * 100)) + ' %' + "\n" + \
                 'Probability of Away Team winning: ' + \
                 str(round(result['Away team win ratio'] * 100)) + ' %' + "\n" + \
                 'Predicted Goals of Away Team: ' + \
                 'Probability of a Draw: ' + \
                 str(round(result['Home and away team tie ratio'] * 100)) + ' %'

        showinfo("Prediction - Linear Regression", output)
