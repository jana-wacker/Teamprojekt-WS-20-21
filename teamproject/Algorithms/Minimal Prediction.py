"""This module contains code to predict the outcome of a match based on their experience.
It returns the probability of home team and away team winning and the probability of a draw."""
import pandas as pd

# use for plotting data
pd.set_option('display.max_columns', 10)


def dataSource(homeName, guestName, data):
    """Calculate the number of games
    Variables: homeName, guestName  - both form GUI
    Function: iterates through the dictionary of data, searches for the two respective teams,
                when found -> add one to the counter of matches

    """
    data2 = data.loc[(data['Team1'] == homeName) & (data['Team2'] == guestName)]
    return data2


def matchNumber(data):
    """Count the total number from new data to get the count of matches
    Variables: new data
    Function: count matches
    """
    count = len(data)
    return count


def ProHomeWin(data):
    """Get the percentage, when the home team win.
    Variables: new data
    Function: get the win percentage of home team
    """
    percentage = 0
    if matchNumber(data) == 0:
        return percentage
    else:
        final = data.loc[(data['GoalsTeam1'] > data['GoalsTeam2'])]
        hostWinCount = len(final)
        percentage = hostWinCount / matchNumber(data)
        return percentage


def ProHomeLoss(data):
    """Get the percentage, when the home team lost.
    Variables: new data
    Function: get the loss percentage of home team
    """
    percentage = 0
    if matchNumber(data) == 0:
        return percentage
    else:
        final = data.loc[(data['GoalsTeam1'] < data['GoalsTeam2'])]
        hostWinCount = len(final)
        percentage = hostWinCount / matchNumber(data)
        return percentage


def ProHomeTied(data):
    """Get the procentage, when the teams tie.
    Variables: new data
    Function: get the tie percentage of home team
    """
    percentage = 0
    if matchNumber(data) == 0:
        return percentage
    else:
        final = data.loc[(data['GoalsTeam1'] == data['GoalsTeam2'])]
        hostWinCount = len(final)
        percentage = hostWinCount / matchNumber(data)
        return percentage


def predict(homeName, guestName, data):
    """The final method to print out the results
    Variables: new data

    Function: 1. Check if there are any matches, if not, tell user
          2. If there are matches, create an array with all the results
          Results: call all the defined methods above with the two variables, store output in array
          3. print out the array with results

    Usage: To be called in the GUI button "Activate the AI"
    """
    data = dataSource(homeName, guestName, data)
    if matchNumber(data) == 0:
        showinfo("Prediction - Minimal Prediction",
                 "Sorry, the data set is incomplete and cannot be used for prediction! "
                 "Please choose other teams or data frame!")
    else:
        result = {'Home Team Name': homeName,
                  'Away Team Name': guestName,
                  'Total number of matches': matchNumber(data),
                  'Home team win ratio': ProHomeWin(data),
                  'Home team loss ratio': ProHomeLoss(data),
                  'Home and away team tie ratio': ProHomeTied(data)}

        output = 'Minimal Algorithm:' + "\n" + "\n" + \
                 homeName + "\n" + ' vs. ' + "\n" + guestName + "\n" + "\n" + \
                 'Number of Matches between the two Teams: ' + \
                 str(result['Total number of matches']) + "\n" + \
                 'Probability of Home Team winning: ' + \
                 str(round(result['Home team win ratio'] * 100)) + ' %' + "\n" + \
                 'Probability of Away Team winning: ' + \
                 str(round(result['Home team loss ratio'] * 100)) + ' %' + "\n" + \
                 'Probability of a Draw: ' + \
                 str(round(result['Home and away team tie ratio'] * 100)) + ' %'

        return output
