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


#######################################################################################################

def newData(data):
    """
    Input: data from percentage()

    Function: 1. create the new column for score, which is subtracted from the away team's score
              2. positve score proves that the home team won,
              while 0 indicates a fight and a negative number represents a win for the away team.
    """
    final=homeAndguest(data)
    # merge score_away & score_home into column 'score'
    final['score'] = final['GoalsTeam1']-final['GoalsTeam2']
    # Before showing our final dataset we will drop any rows with NA values.
    final = final.dropna()
    final['score'] = final.score.astype('float64')
    return final

#print(newData(data))
########################################################################################################
"""
Input: data homeAndguest()

Function: 1. creat a new column for total score in 2 teams
          2. creat a new column for percentage, which is score divided by the total score
          3. As there is a possibility that the two teams are tied 0:0, the total in this case is +1.
          4. If the percentage is larger than 0, the home team won; if percentage is 0, then they tie. 
          Otherwise, the home team loss.
"""
def percentage(data):
    final = newData(data)
    final['total']= np.where(final['GoalsTeam1']+final['GoalsTeam2']==0, 1, final['GoalsTeam1']+final['GoalsTeam2'])
    final['percentage']=final['score']/final['total']
    final['2_game_avg'] = final.percentage.rolling(window=2).mean()
    final = final.dropna()
    return final['percentage'].iloc[-1]
print(percentage(data))


#######################################################################################################
"""
Input: final 

Function: 1. After testing, the element with an impact factor is obtained
          2. predictions are made using this element, here using linear regression.
"""
def CalRatio(data):
    X = pd.DataFrame(percentage(data), columns=['date'])
    Y = pd.DataFrame(percentage(data), columns=['percentage'])
    # WITH a random_state parameter:
    # (Same split every time! Note you can change the random state to any integer.)
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=1)
    # Create linear regression model
    lin_reg_mod = LinearRegression()
    # Fit linear regression
    lin_reg_mod.fit(X_train, Y_train)
    result=lin_reg_mod.intercept_
    return (result)
#print(CalRatio(data))
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
def algoPrediction(homeName, guestName,data):
     print('Home Team Name:'+homeName)
     print('Away Team Name:'+guestName)
     result = CalRatio(data)
     if result>0:
         print('Home team may win and the ratio is:' + percentage(data)['percentage'].iloc[-1])
     if result==0:
         print('Two team may tie')
     else:
        print('Home team may loss')




####################################################################################################
####################################################################################################
####################################################################################################

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
def AssessModel(data):
    """
    Input: final

    Function: 1. Use RMSE and R2 to evaluate the model
    """
    X = pd.DataFrame(percentage(data), columns=['percentage'])
    Y = pd.DataFrame(percentage(data), columns=['score'])
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
#print(AssessModel(data))

################################################################################