import pandas as pd
import gui
gui_main = gui.main()

#use for plotting data
pd.set_option('display.max_columns', 10)
import matplotlib.pyplot as plt
#%matplotlib inline
import numpy as np
# Used for Regression Modelling
from sklearn.linear_model import LinearRegression
from sklearn import linear_model
from sklearn.model_selection import train_test_split
# Used for Acc metrics
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
# box plots
import seaborn as sns
# pairplot
from seaborn import pairplot


# Load your data
data = pd.read_csv("Crawler.csv")

# adding .head() to your dataset allows you to see the first rows in the dataset.
print(data.shape)
data.head()
print(data)

#################################################################################################
'''These input fields pull which team the user selected to compare  
    (Source: the GUI dropdown fields)
    
!!!  I am not completely sure if it is working, if not I don't know how to access the variables from the gui file'''

homeName = gui_main.homeTeam
guestName = gui_main.guestTeam
# homeName=input("Please write your home team name:")
# guestName=input("Please write your guest team name:")
#######################################################################################################
'''Calculate the number of games 

Variables: homeName, guestName  - both form GUI 
Function: iterates through the dictionary of data, searches for the two respective teams, 
            when found -> add one to the counter of matches 
            
'''


'''Select the proper data from the orginal data source and return the new data 

Variables: original data 
Function: select the data depending on the homeName and guestName by GUI
'''

#Find the home and away teams and form them into a new pandas.
def dataSource(data):
    data2 = data.loc[(data['Team1'] == homeName) & (data['Team2'] == guestName)]
    return data2

print(dataSource(data))
#######################################################################################################
'''count the total number from new data to get the count of matches

Variables: new data 
Function: count the match 
'''

def matchNumber(data):
    # Return rows where Team(User choose)
    count=len(data)
    return count

#print(matchNumber(dataSource(data)))
#######################################################################################################
'''Get the procentage, when the home team win.

Variables: new data
Function: get the win procentage of home team
'''

def ProHomeWin(data):
    procentage =0
    if matchNumber(data)==0:
        return procentage
    else:
        final = data.loc[(data['GoalsTeam1'] > data['GoalsTeam2'])]
        hostWinCount=len(final)
        procentage=hostWinCount/matchNumber(data)
        return(procentage)

#print(ProHomeWin(dataSource(data)))
#######################################################################################################
'''Get the procentage, when the home team lost.

Variables: new data
Function: get the loss procentage of home team
'''

def ProHomeLoss(data):
    procentage =0
    if matchNumber(data)==0:
        return procentage
    else:
        final = data.loc[(data['GoalsTeam1'] < data['GoalsTeam2'])]
        hostWinCount=len(final)
        procentage=hostWinCount/matchNumber(data)
        return(procentage)

#print(ProHomeLoss(dataSource(data)))
#######################################################################################################
'''Get the procentage, when the teams tie.

Variables: new data
Function: get the tie procentage of home team
'''

def ProHomeTied(data):
    procentage =0
    if matchNumber(data)==0:
        return procentage
    else:
        final = data.loc[(data['GoalsTeam1'] == data['GoalsTeam2'])]
        hostWinCount=len(final)
        procentage=hostWinCount/matchNumber(data)
        return(procentage)

#print(ProHomeTied(dataSource(data)))
#######################################################################################################
'''The final method to print out the results 
Variables: new data 

Function: 1. Check if there are any matches, if not, tell user 
          2. If there are matches, create an array with all the results 
          Results: call all the definied methods above with the two variables, store output in array 
          3. print out the array with results 
          
Usage: To be called in the GUI button "Activate the AI" 

'''

#Method for the results to be called in the GUI button to predict results
def algoPrediction(data):
    if matchNumber(data)==0:
        print('Sorry, there was no game between these two teams.')
    else:
        result={'Home Team Name':homeName,
                'Away Team Name': guestName,
                'Total number of matches': matchNumber(data),
                'Home team win ratio': ProHomeWin(data),
                'Home team loss ratio': ProHomeLoss(data),
                'Home and away team tie ratio': ProHomeTied(data)}
        print(result)

#print(algoPrediction(dataSource(data)))
showinfo("Activation Crawler", result)
####################################################################################################
####################################################################################################
####################################################################################################