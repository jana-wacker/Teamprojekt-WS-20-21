"""
This module contains code to fetch required data from the internet and convert
it to our internal format.
"""

import pandas as pd
import requests
import json


def fetch_data():
    """
    Query data from "the internet" and return in our internal format.
    * Year (int): Year the crawler starts to collect the data
    * Gameday (int): First gameday which is taken into the data collection
    * UntilYear (int): Data is collected until this year
    * UntilGameday (int): Data is collected until this gameday
    """
    year = input
    UntilYear = input()
    UntilGameday = input()

    # There's an array for every information we want to save in a separate file
    team1 = []
    team1points = []
    team2 = []
    team2points = []
    location = []
    date = []

    # Two while loops to go through the different years and gamedays
    while year < UntilYear:
        year = year + 1
        gameday = input()

        while gameday < UntilGameday:

            # The data from the URL is saved in a dictionary
            r = requests.get('https://www.openligadb.de/api/getmatchdata/bl1/' + str(year) + '/' + str(gameday))
            r_dict = r.json()



            # The loop goes through all the information in the dictionary and adds the information to the right array
            for i in r_dict:
                if i['MatchIsFinished']:
                    team1.append(i['Team1']['TeamName'])
                    team2.append(i['Team2']['TeamName'])
                    team1points.append(i['MatchResults'][0]['PointsTeam1'])
                    team2points.append(i['MatchResults'][0]['PointsTeam2'])
                    date.append(i['MatchDateTimeUTC'])
                    if i['Location'] is None:
                        location.append('Unbekannt')
                    else:
                        location.append(i['Location']['LocationCity'])

                else:
                    continue



            # Creating a dictionary with all the relevant information
            data = {
                'Location': location,
                'Date': date,
                'Team1': team1,
                'GoalsTeam1': team1points,
                'GoalsTeam2': team2points,
                'Team2': team2
                }

            # Creating a CSV file to store the information
            df = pd.DataFrame(data)
            df.to_csv('Crawler.csv', index=False)

            gameday = gameday + 1



def fetch_all_data():
    """
    Query data from "the internet" and return in our internal format.
    * Year (int): Year the crawler starts to collect the data
    """
    year = 2004


    # There's an array for every information we want to save in a separate file
    team1 = []
    team1points = []
    team2 = []
    team2points = []
    location = []
    date = []

    while year < 2021:
        r = requests.get('https://www.openligadb.de/api/getmatchdata/bl1/' + str(year))
        r_dict = r.json()



        # The loop goes through all the information in the dictionary and adds the information to the right array
        for i in r_dict:
            if i['MatchIsFinished']:
                team1.append(i['Team1']['TeamName'])
                team2.append(i['Team2']['TeamName'])
                team1points.append(i['MatchResults'][0]['PointsTeam1'])
                team2points.append(i['MatchResults'][0]['PointsTeam2'])
                date.append(i['MatchDateTimeUTC'])
                if i['Location'] is None:
                    location.append('Unbekannt')
                else:
                    location.append(i['Location']['LocationCity'])

            else:
                continue

            # Creating a dictionary with all the relevant information
            data = {
                'Location': location,
                'Date': date,
                'Team1': team1,
                'GoalsTeam1': team1points,
                'GoalsTeam2': team2points,
                'Team2': team2
            }

        # Creating a CSV file to store the information
        df = pd.DataFrame(data)
        df.to_csv('Alldata.csv', index=False)


        year = year + 1

