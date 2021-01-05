"""Jana: Okay I reworked this module a little bit... There was a fault in the predict()
method, so that all encounters had the same result.
I included the dataSource() method in predict(). That seemed to fix it."""
import pandas as pd
from tkinter.messagebox import showinfo

# use for plotting data
pd.set_option('display.max_columns', 10)


'''Calculate the number of games 
Variables: homeName, guestName  - both form GUI 
Function: iterates through the dictionary of data, searches for the two respective teams, 
            when found -> add one to the counter of matches 
            
'''

'''Select the proper data from the original data source and return the new data 
Variables: original data 
Function: select the data depending on the homeName and guestName by GUI
'''


# Find the home and away teams and form them into a new pandas.
def dataSource(homeName, guestName, data):
    data2 = data.loc[(data['Team1'] == homeName) & (data['Team2'] == guestName)]
    return data2


#######################################################################################################
'''count the total number from new data to get the count of matches
Variables: new data 
Function: count the match 
'''


def matchNumber(data):
    # Return rows where Team(User choose)
    count = len(data)
    return count


#######################################################################################################
'''Get the percentage, when the home team win.
Variables: new data
Function: get the win percentage of home team
'''

def ProHomeWin(data):
    percentage = 0
    if matchNumber(data) == 0:
        return percentage
    else:
        final = data.loc[(data['GoalsTeam1'] > data['GoalsTeam2'])]
        hostWinCount = len(final)
        percentage = hostWinCount / matchNumber(data)
        return percentage

#######################################################################################################
'''Get the procentage, when the home team lost.
Variables: new data
Function: get the loss percentage of home team
'''


def ProHomeLoss(data):
    percentage = 0
    if matchNumber(data) == 0:
        return percentage
    else:
        final = data.loc[(data['GoalsTeam1'] < data['GoalsTeam2'])]
        hostWinCount = len(final)
        percentage = hostWinCount / matchNumber(data)
        return percentage



#######################################################################################################
'''Get the procentage, when the teams tie.
Variables: new data
Function: get the tie percentage of home team
'''


def ProHomeTied(data):
    percentage = 0
    if matchNumber(data) == 0:
        return percentage
    else:
        final = data.loc[(data['GoalsTeam1'] == data['GoalsTeam2'])]
        hostWinCount = len(final)
        percentage = hostWinCount / matchNumber(data)
        return percentage



#######################################################################################################
'''The final method to print out the results 
Variables: new data 
Function: 1. Check if there are any matches, if not, tell user 
          2. If there are matches, create an array with all the results 
          Results: call all the defined methods above with the two variables, store output in array 
          3. print out the array with results 
          
Usage: To be called in the GUI button "Activate the AI" 
'''


# Method for the results to be called in the GUI button to predict results
def predict(homeName, guestName, data):
    data = dataSource(homeName, guestName, data)
    if matchNumber(data) == 0:
        showinfo("Prediction", "Sorry, there was no game between these two teams.")
    else:
        result = {'Home Team Name': homeName,
                  'Away Team Name': guestName,
                  'Total number of matches': matchNumber(data),
                  'Home team win ratio': ProHomeWin(data),
                  'Home team loss ratio': ProHomeLoss(data),
                  'Home and away team tie ratio': ProHomeTied(data)}
        showinfo("Prediction - Minimal", result)
#predict('VfL Wolfsburg', 'VfB Stuttgart', data)
