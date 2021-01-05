"""
This module contains code to analyse the past bundesliga seasons
"""

from teamproject import crawler
import csv

"""
    Analyse the data from the collected games in the bundesliga
    Homewin(int): Number how often the hometeam won
    Awaywin(int): Number how often the guestteam won
    Draw(int): Number how often the game ended in a draw
    Linecount(int): Number of games which were analysed 
    Goalshome(int): Total number of goals when the hometeam won
    Goalsaway(int): Total number of goals when the guestteam won
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
with open('Alldata.csv', mode='r') as csv_file:
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


""""
    Calculation of the ratios with the results from before
    Homewinratio(int): Probability that the hometeam wins
    Awaywinratio(int): Probability that the guestteam wins
    Drawratio(int): Probability that the game ends in a draw
    Averagegoalshomewin(int): Average goals for the hometeam
    Averagegoalsawaywin(int): Average goals for the guestteam
    
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


