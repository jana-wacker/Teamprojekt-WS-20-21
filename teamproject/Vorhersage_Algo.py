# importing the csv module
#import csv
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
# Correlation plot
from statsmodels.graphics.correlation import plot_corr



# my data rows as dictionary objects
achiveForms =[{'date': '2009-08-07T20:30:00', 'host': 'Hannover', 'guest': 'Dusseldorf', 'hostScores': '2','guestScores':'0'},
                {'date': '2009-08-08T15:30:00', 'host': 'Munich', 'guest': 'Dusseldorf', 'hostScores': '2','guestScores':'1'},
                {'date': '2009-08-08T15:30:00', 'host': 'Munich', 'guest': 'Dusseldorf', 'hostScores': '2','guestScores':'3'},
                {'date': '2009-08-08T15:30:00', 'host': 'Munich', 'guest': 'Dusseldorf', 'hostScores': '1','guestScores':'1'},
                {'date': '2009-08-08T15:30:00', 'host': 'Munich', 'guest': 'Dusseldorf', 'hostScores': '3','guestScores':'1'},
                {'date': '2009-08-08T15:30:00', 'host': 'Munich', 'guest': 'Hannover', 'hostScores': '2','guestScores':'1'}]

df = pd.DataFrame(achiveForms)
print(df)


#################################################################################################



'''These input fields pull which team the user selected to compare  
    (Source: the GUI dropdown fields)
    
!!!  I am not completely sure if it is working, if not I don't know how to access the variables from the gui file'''

homeName = gui_main.homeTeam
guestName = gui_main.guestTeam


#######################################################################################################
'''Calculate the number of games 

Variables: homeName, guestName  - both form GUI 
Function: iterates through the dictionary of data, searches for the two respective teams, 
            when found -> add one to the counter of matches 
            
'''


#Calculate the number of games for a particular home and away team, and form it into a new list.
def matchNumber(homeName, guestName):
    newAchiveForms=[]
    count=0
    for i in range(len(achiveForms)):
        if (achiveForms[i]['host']==homeName) & (achiveForms[i]['guest']==guestName):
            count=count+1
            newAchiveForms.append(achiveForms[i])
    return count


#######################################################################################################


#Find the home and away teams and form them into a new list.
def newAchiveForms(homeName, guestName):
    newList=[]
    if matchNumber(homeName, guestName)==0:
        return newList
    else:
        for i in range(len(achiveForms)):
            if (achiveForms[i]['host']==homeName) & (achiveForms[i]['guest']==guestName):
                newList.append(achiveForms[i])
        return newList

#print(newAchiveForms(homeName,guestName))
########################################################################################################


#######################################################################################################
#Counts the number of times the home team has won, drawn, and lost.
def ProHomeWin(aList):
    hostWinCount = 0
    if matchNumber(homeName, guestName)==0:
        return 0
    else:
        for i in range(len(aList)):
            if(int(aList[i]['hostScores']))>(int(aList[i]['guestScores'])):
                hostWinCount=hostWinCount+1
        return(hostWinCount/matchNumber(homeName, guestName))

#print(ProHomeWin(newAchiveForms(homeName,guestName)))
#######################################################################################################


#######################################################################################################
#Counts the number of times the home team has lost.
def ProHomeLoss(aList):
    hostLossCount = 0
    if matchNumber(homeName, guestName)==0:
        return 0
    else:
        for i in range(len(aList)):
            if(int(aList[i]['hostScores']))<(int(aList[i]['guestScores'])):
                hostLossCount=hostLossCount+1
        return(hostLossCount/matchNumber(homeName, guestName))

#print(ProHomeLoss(newAchiveForms(homeName,guestName)))
#######################################################################################################


#######################################################################################################
#Counts the number of times the home team has drawn.
def ProHomeTied(aList):
    tiedCount = 0
    if matchNumber(homeName, guestName)==0:
        return 0
    else:
        for i in range(len(aList)):
            if(int(aList[i]['hostScores']))==(int(aList[i]['guestScores'])):
                tiedCount=tiedCount+1
        return(tiedCount/matchNumber(homeName, guestName))

#print(ProHomeTied(newAchiveForms(homeName,guestName)))
#######################################################################################################



'''The final method to print out the results 
Variables: homeName, guestName - the teams chosen from the GUI 

Function: 1. Check if there are any matches, if not, tell user 
          2. If there are matches, create an array with all the results 
          Results: call all the definied methods above with the two variables, store output in array 
          3. print out the array with results 
          
Usage: To be called in the GUI button "Activate the AI" 

'''


#Method for the results to be called in the GUI button to predict results
def algoPrediction(homeName, guestName):
    if matchNumber(homeName, guestName)==0:
        print('Sorry, there was no game between these two teams last quarter.')
    else:
     result={'Home Team Name':homeName,
            'Away Team Name': guestName,
            'Total number of matches': matchNumber(homeName, guestName),
            'Home team win ratio': ProHomeWin(newAchiveForms(homeName,guestName)),
            'Home team loss ratio': ProHomeLoss(newAchiveForms(homeName,guestName)),
            'Home and away team tie ratio': ProHomeTied(newAchiveForms(homeName,guestName))}
    print(result)
    input('Please enter the probability of your prediction:')

####################################################################################################
####################################################################################################
####################################################################################################
# Load your data
data = pd.read_csv("Crawler.csv")

# adding .head() to your dataset allows you to see the first rows in the dataset.
print(data.shape)
data.head()
print(data)

"""
Input: data from csv, homeName and guestName from user(GUI)

Function: 1. creat a new dataFrame according to itineraries entered by the user. 
          2. if there are not enough data, print "Sorry, there is not enough data for analysis".
          3. return the new dataFrame
"""
def homeAndguest(data):
    data2 = data.loc[(data['Team1'] == homeName) & (data['Team2'] == guestName)]
    if data2.shape[0]>0:
        return data2
    else:
        print("Sorry, there is not enough data for analysis")
#################################################################################################
"""
Input: data homeAndguest()

Function: 1. creat a new column for total score in 2 teams
          2. creat a new column for percentage, which is Home team score divided by the total score
          3. As there is a possibility that the two teams are tied 0:0, the total in this case is +1.
"""
def percentage(data):
    final = homeAndguest(data)
    final['total']= np.where(final['GoalsTeam1']+final['GoalsTeam2']==0, 1, final['GoalsTeam1']+final['GoalsTeam2'])
    final['percentage']=final['GoalsTeam1']/final['total']
    return final
#print(percentage(data))


def newData(data):
    """
    Input: data from percentage()

    Function: 1. create the new column for score, which is subtracted from the away team's score
              2. positve score proves that the home team won, while 0 indicates a fight and a negative number represents a win for the away team.
              3. extract the useful data into final dataFrame
    """

    final = percentage(data)
    # merge score_away & score_home into column 'score'
    final['score'] = final['GoalsTeam1']-final['GoalsTeam2']
    # Before showing our final dataset we will drop any rows with NA values.
    final = final.dropna()
    final['2_game_avg'] = final.score.rolling(window=2).mean()
    final['5_game_avg'] = final.score.rolling(window=5).mean()
    final.head()
    final=final.fillna(final.mean())
    final['score'] = final.score.astype('float64')
    return final

#print(newData(data))


#############################################################################################
"""
Input: final 

Function: 1. Each element, such as the last 2 match average score, is measured based on the final score. 
             These elements, which have an impact, are selected.
          2. These elements, which have an impact, are selected.
"""
def TestFactor(data):

    sns.boxplot(x='percentage', y='score', data=data)
    plt.show()

    pairplot(data)
    plt.show()
#print(TestFactor(newData(data)))

def TestFactorLastGame(data):
    plt.scatter(data['2_game_avg'], data['percentage'], color='red')
    plt.title( 'percentage Vs Score', fontsize=14)
    plt.xlabel('percentage', fontsize=14)
    plt.ylabel('Score', fontsize=14)
    plt.grid(True)
    plt.show()
#print(TestFactorLastGame(newData(data)))

###############################################################################################
"""
Input: final 

Function: 1. After testing, the element with an impact factor is obtained
          2. predictions are made using this element, here using linear regression.
"""
def CalRatio(data):
    X = pd.DataFrame(newData(data), columns=['percentage','2_game_avg'])
    Y = pd.DataFrame(newData(data), columns=['score'])
    # WITH a random_state parameter:
    # (Same split every time! Note you can change the random state to any integer.)
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=1)
    # Create linear regression model
    lin_reg_mod = LinearRegression()
    # Fit linear regression
    lin_reg_mod.fit(X_train, Y_train)
    # Make prediction on the testing data
    pred = lin_reg_mod.predict(X_test)
    return (pred)
#print(CalRatio(data))



###############################################################################################
def AssessModel(data):
    """
    Input: final

    Function: 1. Use RMSE and R2 to evaluate the model
    """
    X = pd.DataFrame(newData(data), columns=['percentage','2_game_avg',])
    Y = pd.DataFrame(newData(data), columns=['score'])
    # WITH a random_state parameter:
    # (Same split every time! Note you can change the random state to any integer.)
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=1)
    # Create linear regression model
    lin_reg_mod = LinearRegression()
    # Fit linear regression
    lin_reg_mod.fit(X_train, Y_train)
    # Make prediction on the testing data
    pred = lin_reg_mod.predict(X_test)
    # Calculate the Root Mean Square Error between the actual & predicted
    test_set_rmse = (np.sqrt(mean_squared_error(Y_test, pred)))
    # Calculate the R^2 or coefficent of determination between the actual & predicted
    test_set_r2 = r2_score(Y_test, pred)
    # Note that for rmse, the lower that value is, the better the fit
    # The closer towards 1, the better the fit
    result={'test RMSE':test_set_rmse,'test R^2':test_set_r2}
    return result
print(AssessModel(data))

################################################################################