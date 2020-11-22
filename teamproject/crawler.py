"""
This module contains code to fetch required data from the internet and convert
it to our internal format.
"""
""""
import pandas as pd


def fetch_data():
    """
"""
    Query data from "the internet" and return in our internal format.
"""
"""
    # For now just return some example data in some example format:
    columns = ['home_team', 'home_score', 'guest_score', 'guest_team']
    return pd.DataFrame([
        ['Bayern', 0, 7, 'Tübingen'],
        ['Tübingen', 3, 2, 'Borussia'],
        ['Tübingen', 0, 0, 'Bremen'],
        ['Bremen', 0, 1, 'Leverkusen'],
    ], columns=columns)

"""

import pandas as pd
import requests
import json


def fetch_data():
    year = 2003
    # Two while loops to go through the different years and gamedays
    while year < 2021:
        year = year + 1
        gameday = 1

        while gameday < 35:

            # The data from the URL is saved in a dictionary
            r = requests.get('https://www.openligadb.de/api/getmatchdata/bl1/' + str(year) + '/' + str(gameday))
            r_dict = r.json()

            # There's an array for every information we want to save in a separate file
            team1 = []
            team1points = []
            team2 = []
            team2points = []
            location = []
            date = []

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
            print(team1)
            print(team2)
            print(team1points)
            print(team2points)
            print(location)
            print(date)


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


fetch_data()