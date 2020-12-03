
# Jana: We don't need that here. The crawler should only be started from the gui.
#importing the csv module
#import csv
import pandas as pd
from tkinter.messagebox import showinfo


# my data rows as dictionary objects
achiveForms =[{'date': '2009-08-07T20:30:00', 'host': 'Hannover', 'guest': 'Dusseldorf', 'hostScores': '2','guestScores':'0'},
                {'date': '2009-08-08T15:30:00', 'host': 'Munich', 'guest': 'Dusseldorf', 'hostScores': '2','guestScores':'1'},
                {'date': '2009-08-08T15:30:00', 'host': 'Munich', 'guest': 'Dusseldorf', 'hostScores': '2','guestScores':'3'},
                {'date': '2009-08-08T15:30:00', 'host': 'Munich', 'guest': 'Dusseldorf', 'hostScores': '1','guestScores':'1'},
                {'date': '2009-08-08T15:30:00', 'host': 'Munich', 'guest': 'Dusseldorf', 'hostScores': '3','guestScores':'1'},
                {'date': '2009-08-08T15:30:00', 'host': 'Munich', 'guest': 'Hannover', 'hostScores': '2','guestScores':'1'}]

df = pd.DataFrame(achiveForms)
#print(df)

# field names
#fields = ['date', 'host', 'guest', 'hostScores','guestScore']

# name of csv file
#filename = "football.csv"

# writing to csv file
#with open(filename, 'w') as csvfile:
    # creating a csv dict writer object
    #writer = csv.DictWriter(csvfile, fieldnames=fields)

    # writing headers (field names)
    #writer.writeheader()

    # writing data rows
    #writer.writerows(mydict)


'''These input fields pull which team the user selected to compare  
    (Source: the GUI dropdown fields)
    
!!!  I am not completely sure if it is working, if not I don't know how to access the variables from the gui file'''


#homeName=input('Please enter the home team name:')
#guestName = input("Please enter the visiting team name:")


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
def ProHomeWin(aList, homeName, guestName):
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
def ProHomeLoss(aList, homeName, guestName):
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
def ProHomeTied(aList, homeName, guestName):
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
    # Jana: Added Info-Box to display result, since I am not sure, how it will work if you use the "print"-command
    #print(result)
    showinfo("Activation Crawler", result)
    #input('Please enter the probability of your prediction:')
