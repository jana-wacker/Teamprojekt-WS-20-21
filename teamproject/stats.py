"""
This module contains code to create a statistic on a specific team
"""

import csv
import matplotlib.pyplot as plt
from tkinter.messagebox import showinfo
import os


def analysis(team):
    """
    Calculation of the ratios with the results from before
    Homewinratio(int): Probability that the hometeam wins
    Awaywinratio(int): Probability that the guestteam wins
    Drawratio(int): Probability that the game ends in a draw
    Averagegoalshomewin(int): Average goals for the hometeam
    Averagegoalsawaywin(int): Average goals for the guestteam
    """
    totalgames = 0
    homevictory = 0
    homedefeat = 0
    homedraw = 0
    awayvictory = 0
    awaydefeat = 0
    awaydraw = 0

    # Choose the periode of time you want to analyse

    crawlerdata = os.path.join(os.path.dirname(__file__), 'Crawler.csv')
    with open(crawlerdata, mode='r', encoding="utf8") as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            # Club plays at home
            if str(row['Team1']) == team:
                # Club wins at home
                if row['GoalsTeam1'] > row['GoalsTeam2']:
                    homevictory = homevictory + 1
                    totalgames = totalgames + 1
                else:
                    # Club loses at home
                    if row['GoalsTeam1'] < row['GoalsTeam2']:
                        homedefeat = homedefeat + 1
                        totalgames = totalgames + 1
                    else:
                        # Club plays draw at home
                        homedraw = homedraw + 1
                        totalgames = totalgames + 1
            # Club plays away
            elif str(row['Team2']) == team:
                # Club wins away
                if row['GoalsTeam1'] < row['GoalsTeam2']:
                    awayvictory = awayvictory + 1
                    totalgames = totalgames + 1
                else:
                    # Club loses away
                    if row['GoalsTeam1'] > row['GoalsTeam2']:
                        awaydefeat = awaydefeat + 1
                        totalgames = totalgames + 1
                    # Club plays draw away
                    else:
                        awaydraw = awaydraw + 1
                        totalgames = totalgames + 1
            else:
                continue

    if totalgames == 0:
        showinfo("Statistics", "Sorry, the data set is incomplete and cannot be used for statistics! "
                               "Please choose another team or data frame!")
    else:
        homevictoryratio = (100 / totalgames) * homevictory
        homedefeatratio = (100 / totalgames) * homedefeat
        homedrawratio = (100 / totalgames) * homedraw
        awayvictoryratio = (100 / totalgames) * awayvictory
        awaydefeatratio = (100 / totalgames) * awaydefeat
        awaydrawratio = (100 / totalgames) * awaydraw

        ynumbers = [homevictoryratio, homedefeatratio, homedrawratio, awayvictoryratio, awaydefeatratio, awaydrawratio]
        xnumbers = ['Home' + '\n' + 'Win', 'Home' + '\n' + 'Defeat',
                    'Home' + '\n' + 'Draw', 'Away' + '\n' + 'Victory',
                    'Away' + '\n' + 'Defeat', 'Away' + '\n' + 'Draw']
        font = {'fontname': 'Bahnschrift'}
        plt.figure(num='Statistics ' + team, figsize=(5, 4), frameon=False)
        plt.bar(xnumbers, ynumbers, color=(0.2, 0.4, 0.6, 0.6))
        plt.ylabel('Ratio in %', **font)
        plt.title('Statistics ' + team + '\n' + '(number of total games in selected data frame: ' + str(totalgames)
                  + ')', **font)
        plt.show()
