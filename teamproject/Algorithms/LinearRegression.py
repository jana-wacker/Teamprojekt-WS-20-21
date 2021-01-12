
#use for plotting data
import pandas as pd
pd.set_option('display.max_columns', 10)
import matplotlib.pyplot as plt
#%matplotlib inline
import numpy as np
# Used for Regression Modelling
from sklearn.linear_model import LinearRegression
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from tkinter.messagebox import showinfo


# Load your data
#data = pd.read_csv("Crawler.csv")

# adding .head() to your dataset allows you to see the first rows in the dataset.
#print(data.shape)
#data.head()
#print(data)

#################################################################################################
"""
When the user enters only the name of a team without defining whether it is a home or away team
"""
#homeName=input("Please input the home team name:")
#guestName=input("Please input the guest team name:")
#################################################################################################
"""
Variables: data from crawler

Function: 1. Find the designated team (either a home team or an away team)
          2. Mark 1 in the home_or_away column if it is a home team, otherwise 0 
          3. Pick out 'Team1','Team2','GoalsTeam1','GoalsTeam2' and 'home_or_away' columns to form a new dataFrame.

Usage: Filter out user-specified football teams" 
"""
def homeAndguest(homeName, guestName, data):
    # Create a column titled home or away. This column will add a 1 to the row  where the played at home
    # and a 0 for away games.
    final = data.loc[((data['Team1'] == homeName) & (data['Team2'] == guestName))|
                     ((data['Team1'] == guestName) & (data['Team2'] == homeName))]
    final.loc[:,('home_or_away')] = np.where(final.loc[:,('Team1')] == homeName, 1, 0)
    final=final.filter(['Team1','Team2','GoalsTeam1','GoalsTeam2','home_or_away'])
    final = final.dropna()
    final.head()
    return final

#print(homeAndguest(data))
#################################################################################################
"""
Variables: data from homeAndguest

Function: 1. If the number of matches is greater than 0, this outputs the result, 
             otherwise it outputs 0.
          
Usage: Calculate the number of matches played by a given team" 
"""
def matchCount(homeName, guestName, data):
    count = homeAndguest(homeName, guestName, data).shape[0]
    if count>0:
        return count
    else:
        return 0

#print(matchCount(data))
#################################################################################################
"""
The home team percentage is Home team score divided by the total score,
As there is a possibility that the two teams are tied 0:0, the total in this case is +1.
"""
"""
Variables: data from homeAndguest

Function: 1. Calculate the total score, if the total score is 0 (0:0), output 1, 
             otherwise output the corresponding result.
          2.Calculate the percentage of home team wins (home team score divided by total score).
          3.Calculate the average of 2 times the percentage.
          4.Construct a new dataFrame, including 'home_or_away','HomeWinPercentage' and '2_percentage_avg'.

Usage: Data processing to find the data for calculating percentages" 
"""
def percentage(homeName, guestName, data):
    final = homeAndguest(homeName, guestName, data)
    final['total']= np.where(final['GoalsTeam1']+final['GoalsTeam2']==0, 1, final['GoalsTeam1']+final['GoalsTeam2'])
    final['HomeWinPercentage']=final['GoalsTeam1']/final['total']
    final['2_percentage_avg']=final.HomeWinPercentage.rolling(window=2).mean()
    final = final.fillna(final.mean())
    final.head()
    df=final[['home_or_away','HomeWinPercentage','2_percentage_avg']]
    df.loc[:,('home_or_away')] = df.loc[:,('home_or_away')].astype('float64')
    return df
#print(percentage(data))

###############################################################################################
'''Variables: data from homeAndguest

Function: 1.Find the corresponding score
          2.Calculate the average of 2 times the scores.
          4.Construct a new dataFrame, including 'home_or_away','2_score_avg' and 'score'.

Usage: Data processing for calculating score.'''
def score(homeName, guestName, data):
    final = homeAndguest(homeName, guestName, data)
    final['score'] = np.where(final['Team2'] == homeName, final['GoalsTeam2'], final['GoalsTeam1'])
    final = final.dropna()
    final['2_score_avg'] = final.score.rolling(window=2).mean()
    final = final.dropna()
    final.head()
    df = final[['home_or_away','2_score_avg','score']]
    df.loc[:,('home_or_away')]=df.loc[:,('home_or_away')].astype('float64')
    df.loc[:,('score')]=df.loc[:,('score')].astype('float64')
    return df

#print(score(data).info())

###############################################################################################
'''Variables: data from score

Function: 1.Composition of linear programming templates. Impact factors include 'home_or_away' and '2_score_avg',
            the result is 'score'.
          2.Calculating intercepts and slopes.
          4.Calculate the score of home team and the score of away team respectively.

Usage: Calculate the score of home and away team respectively.'''
def predicateScore(homeName, guestName, data):
    df=score(homeName, guestName, data)
    X = pd.DataFrame(df, columns=['home_or_away','2_score_avg'])
    Y = pd.DataFrame(df, columns=['score'])
    # WITH a random_state parameter:
    # (Same split every time! Note you can change the random state to any integer.)
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=1)
    # Create linear regression model
    lin_reg_mod = LinearRegression()
    # Fit linear regression
    lin_reg_mod.fit(X_train, Y_train)
    return lin_reg_mod

def scoreIntercept(homeName, guestName, data):
    intercept=predicateScore(homeName, guestName, data).intercept_
    return intercept[0]
#print(scoreIntercept(data))

def scoreCoefhomeoraway(homeName, guestName, data):
    coef_home_or_away=predicateScore(homeName, guestName, data).coef_[0][0]
    return coef_home_or_away
#print(scoreCoefhomeoraway(data))

def scoreCoefavg(homeName, guestName, data):
    coef_2_score_avg=predicateScore(homeName, guestName, data).coef_[0][1]
    return coef_2_score_avg
#print(scoreCoefavg(data))

def homeScore(homeName, guestName, data):
    df=score(homeName, guestName, data)
    homeScorePre=scoreIntercept(homeName, guestName, data)+\
                 scoreCoefhomeoraway(homeName, guestName, data)*\
                 1+scoreCoefavg(homeName, guestName, data)*df['2_score_avg'].values[-1]
    if homeScorePre<0:
        homeScorePre=0
    return homeScorePre
#print(homeScore(data))

def awayScore(homeName, guestName, data):
    df=score(homeName, guestName, data)
    awayScorePre=\
        scoreIntercept(homeName, guestName, data)+scoreCoefhomeoraway(homeName, guestName, data)\
        *0+scoreCoefavg(homeName, guestName, data)*df['2_score_avg'].values[-1]
    if awayScorePre<0:
        awayScorePre=0
    return awayScorePre
#print(awayScore(data))

###############################################################################################
'''Variables: data from percentage

Function: 1.Composition of linear programming templates. Impact factors include 'home_or_away'and'2_percentage_avg',
            the result is 'HomeWinPercentage'.
          2.Calculating intercepts and slopes.
          4.Calculate the percentage of home team wins, the percentage of away team wins 
            and the percentage of draws respectively.

Usage: Calculate the percentage of home and away team wins respectively.'''
def predicatePercentage(homeName, guestName, data):
    df=percentage(homeName, guestName, data)
    X = pd.DataFrame(df, columns=['home_or_away','2_percentage_avg'])
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
    intercept = predicatePercentage(homeName, guestName, data).intercept_
    return intercept[0]
#print(percentageIntercept(data))

def percentageCoefhomeoraway(homeName, guestName, data):
    coef_home_or_away = predicatePercentage(homeName, guestName,data).coef_[0][0]
    return coef_home_or_away
#print(percentageCoefhomeoraway(data))

def percentageCoefavg(homeName, guestName, data):
    coef_2_percentage_avg = predicatePercentage(homeName, guestName,data).coef_[0][1]
    return coef_2_percentage_avg
#print(percentageCoefavg(data))

def homePercentage(homeName, guestName, data):
    df = percentage(homeName, guestName, data)
    homePercentagePre = percentageIntercept(homeName, guestName, data) + \
                        percentageCoefhomeoraway(homeName, guestName, data) * 1 \
                        + percentageCoefavg(homeName, guestName, data) \
                        * df['2_percentage_avg'].values[-1]
    if homePercentagePre < 0:
        homePre = 0
    elif homePercentagePre > 1:
        homePre = 1
    else:
        homePre = homePercentagePre
    return homePre
#print(homePercentage(data))

def awayPercentage(homeName, guestName, data):
    df = percentage(homeName, guestName, data)
    awayPercentagePre = percentageIntercept(homeName, guestName, data) + \
                        percentageCoefhomeoraway(homeName, guestName, data) * 0 + \
                        percentageCoefavg(homeName, guestName, data) * df['2_percentage_avg'].values[-1]
    if awayPercentagePre < 0:
        awayPre = 0
    elif awayPercentagePre > 1:
        awayPre = 1
    else:
        awayPre = awayPercentagePre
    return awayPre
#print(awayPercentage(data))

def tiedPrecentage(homeName, guestName, data):
    tiedPre=1-homePercentage(homeName, guestName, data)-awayPercentage(homeName, guestName, data)
    if tiedPre<0:
        tiedPre=0
    return tiedPre
#print(tiedPrecentage(data))
###############################################################################################
'''
'''
def predict(homeName, guestName, data):
    final=homeAndguest(homeName, guestName, data)
    if(matchCount(homeName, guestName, final))==0:
        showinfo("Prediction - Poisson Distribution",
                 "Sorry, the data is incomplete and cannot be used for prediction! "
                 "Please choose other teams or time!")
    else:
        result = {'Home Team': homeName,
                  'Away Team': guestName,
                  'Home team win ratio': homePercentage(homeName, guestName, final),
                  'Home and away team tie ratio': tiedPrecentage(homeName, guestName, final),
                  'Away team win ratio': awayPercentage(homeName, guestName, final),
                  'Home team score': homeScore(homeName, guestName, final),
                  'Away team score': awayScore(homeName, guestName, final)}
        output = homeName + ' vs. ' + guestName + "\n" + "\n" + \
                 'Probability of Home Team winning: ' + \
                 str(round(result['Home team win ratio']*100)) + ' %' + "\n" + \
                 'Predicted Goals of Home Team: ' + \
                 str(round(result['Home team score'])) + "\n" + \
                 'Probability of Away Team winning: ' + \
                 str(round(result['Away team win ratio']*100)) + ' %' + "\n" + \
                 'Predicted Goals of Away Team: ' + \
                 str(round(result['Away team score'])) + "\n" + \
                 'Probability of a Draw: ' + \
                 str(round(result['Home and away team tie ratio']*100)) + ' %'

        showinfo("Prediction - Linear Regression", output)
#print(predict(data))
###############################################################################################



