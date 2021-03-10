"""
This module contains code to analyse the past bundesliga seasons
"""

import crawler
import csv
import matplotlib.pyplot as plt
import os

"""
    Analyse the data from the collected games in the bundesliga
    Homewin(int): Number how often the hometeam won
    Awaywin(int): Number how often the guestteam won
    Draw(int): Number how often the game ended in a draw
    Linecount(int): Number of games which were analysed 
    Goalshome(int): Total number of goals when the hometeam won
    Goalsaway(int): Total number of goals when the guestteam won
"""

"""
homewin = 0
draw = 0
awaywin = 0
linecount = 0
goalshome = 0
goalsaway = 0

# Crawler fetches the recent data
crawler.fetch_all_data()

# opening the Alldata file
alldata = os.path.join(os.path.dirname(__file__), 'Crawler.csv')
with open(alldata, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    # Loop to go through all lines and rows
    for row in csv_reader:
        # Homewin
        if row['GoalsTeam1'] > row['GoalsTeam2']:
            homewin = homewin + 1
            goalshome = goalshome + int(row['GoalsTeam1'])
            linecount += 1
        else:
            # Awaywin
            if row['GoalsTeam1'] < row['GoalsTeam2']:
                awaywin = awaywin + 1
                goalsaway = goalsaway + int(row['GoalsTeam2'])
                linecount += 1
            else:
                # Draw
                draw = draw + 1
                linecount += 1

    for row in csv_reader:
        if linecount == 0:
            print('No data available for analysing')
            linecount += 1


"""
"""
    Calculation of the ratios with the results from before
    Homewinratio(int): Probability that the hometeam wins
    Awaywinratio(int): Probability that the guestteam wins
    Drawratio(int): Probability that the game ends in a draw
    Averagegoalshomewin(int): Average goals for the hometeam
    Averagegoalsawaywin(int): Average goals for the guestteam
"""
"""

homewinratio = (100 / linecount) * homewin
awaywinratio = (100 / linecount) * awaywin
drawratio = (100 / linecount) * draw
averagegoalshomewin = goalshome / homewin
averagegoalsawaywin = goalsaway / awaywin

print(linecount)
print(homewinratio)
print(awaywinratio)
print(drawratio)
print(goalshome)
print(goalsaway)
print(averagegoalshomewin)
print(averagegoalsawaywin)


# Creating a table for the ratios
ywerte = [homewinratio, awaywinratio, drawratio]
xwerte= ["Homewin", "Awaywin", "Draw"]
plt.bar(xwerte, ywerte)
plt.ylabel("Ratio in %")
plt.title('Ratio Homewin, Awaywin, Draw')
plt.show()

# Creating a table for the amount of Total Goals
ywerte1 = [goalshome, goalsaway]
xwerte1 = ['Homewin', 'Awaywin']
plt.bar(xwerte1, ywerte1)
plt.ylabel('Total Goals')
plt.title('Goals Statistic')
plt.show()

# Creating a table for the amount of average goals
ywerte2 = [averagegoalshomewin, averagegoalsawaywin]
xwerte2 = ['Homewin', 'Awaywin']
plt.bar(xwerte2, ywerte2)
plt.ylabel('Average Goals')
plt.title('Average Goals')
plt.show()
"""


# Analysing for one club (in this example 'VfB Stuttgart')
def analysisoneclub(team):
    totalhomegames = 0
    totalawaygames = 0
    homevictory = 0
    homedefeat = 0
    homedraw = 0
    awayvictory = 0
    awaydefeat = 0
    awaydraw = 0

    # Choose the periode of time you want to analyse
    #crawler.fetch_all_data()
    crawlerdata = os.path.join(os.path.dirname(__file__), 'Crawler.csv')
    with open(crawlerdata, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            # Club plays at home
            if str(row['Team1']) == team:
                # Club wins at home
                if row['GoalsTeam1'] > row['GoalsTeam2']:
                    homevictory = homevictory + 1
                    totalhomegames = totalhomegames + 1
                else:
                    # Club loses at home
                    if row['GoalsTeam1'] < row['GoalsTeam2']:
                        homedefeat = homedefeat + 1
                        totalhomegames = totalhomegames + 1
                    else:
                        # Club plays draw at home
                        homedraw = homedraw + 1
                        totalhomegames = totalhomegames + 1
            # Club plays away
            elif str(row['Team2']) == team:
                # Club wins away
                if row['GoalsTeam1'] < row['GoalsTeam2']:
                    awayvictory = awayvictory + 1
                    totalawaygames = totalawaygames + 1
                else:
                    # Club loses away
                    if row['GoalsTeam1'] > row['GoalsTeam2']:
                        awaydefeat = awaydefeat + 1
                        totalawaygames = totalawaygames + 1
                    # Club plays draw away
                    else:
                        awaydraw = awaydraw + 1
                        totalawaygames = totalawaygames + 1
            else:
                continue

    homevictoryratio = (100 / totalhomegames) * homevictory
    homedefeatratio = (100 / totalhomegames) * homedefeat
    homedrawratio = (100 / totalhomegames) * homedraw
    awayvictoryratio = (100 / totalawaygames) * awayvictory
    awaydefeatratio = (100 / totalawaygames) * awaydefeat
    awaydrawratio = (100 / totalawaygames) * awaydraw

    ynumbers = [homevictoryratio, homedefeatratio, homedrawratio, awayvictoryratio, awaydefeatratio, awaydrawratio]
    xnumbers = ['Home' + '\n' + 'Win', 'Home' + '\n' + 'Defeat',
                'Home' + '\n' + 'Draw', 'Away' + '\n' + 'Victory',
                'Away' + '\n' + 'Defeat', 'Away' + '\n' + 'Draw']
    font = {'fontname': 'Bahnschrift'}
    plt.figure(num='Statistics ' + team, figsize=(5, 4), frameon=False)
    plt.bar(xnumbers, ynumbers, color=(0.2, 0.4, 0.6, 0.6))
    plt.ylabel('Ratio in %', **font)
    plt.title('Statistics ' + team, **font)
    plt.show()


#analysisoneclub('VfB Stuttgart')
