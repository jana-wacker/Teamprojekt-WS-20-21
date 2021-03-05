"""
This module contains code to fetch required data from the internet and convert
it to our internal format.
"""
from typing import List, Any

import pandas as pd
import requests
import json
from tkinter.messagebox import showinfo
from datetime import datetime

def fetch_matchday():
    """Query data of the next match day and return in our internal format."""
    gameday = 1
    team1 = []
    team2 = []
    nextMatches = []
    match_nr = []

    while gameday <= 34:
        r = requests.get('https://www.openligadb.de/api/getmatchdata/bl1/' + (str(datetime.now().year-1)) + '/' + str(gameday))
        r_dict = r.json()

        for i in r_dict:
            if (i['MatchIsFinished'] == False):
                team1.append(i['Team1']['TeamName'])
                team2.append(i['Team2']['TeamName'])
                nextMatches.append(i['MatchDateTime'])
                match_nr.append(i['Group']['GroupName'])

        gameday = gameday +1

    data = {
        'Matchday': nextMatches,
        'Team1': team1,
        'Team2': team2,
        'MatchNr': match_nr
    }

    # Creating a CSV file to store the information
    df = pd.DataFrame(data)
    df.to_csv('Matchdays.csv', index=False)

def fetch_data(year, gameday, UntilYear, UntilGameday):
    """
    Query data from "the internet" and return in our internal format.
    * Year (int): Year the crawler starts to collect the data
    * Gameday (int): First gameday which is taken into the data collection
    * UntilYear (int): Data is collected until this year
    * UntilGameday (int): Data is collected until this gameday
    """

    # There's an array for every information we want to save in a separate file
    team1 = []
    team1points = []
    team2 = []
    team2points = []
    location = []
    date = []
    matchday = []

    basicyear = year

    # Check if year equals Untilyear and is basicyear as well
    if (year == basicyear) & (year == UntilYear):

        # Loop to go through all the gamedays
        while gameday <= 34:

            # The data from the URL is saved in a dictionary
            r = requests.get('https://www.openligadb.de/api/getmatchdata/bl1/' + str(year) + '/' + str(gameday))
            r_dict = r.json()

            # The loop goes through all the information in the dictionary and adds the information to the right array
            for i in r_dict:
                if i['MatchIsFinished']:
                    team1.append(i['Team1']['TeamName'])
                    team2.append(i['Team2']['TeamName'])
                    if i['MatchResults'][0]['ResultDescription'] == str('Ergebnis nach Ende der offiziellen Spielzeit'):
                        team1points.append(i['MatchResults'][0]['PointsTeam1'])
                    else:
                        team1points.append(i['MatchResults'][1]['PointsTeam1'])
                    if i['MatchResults'][0]['ResultDescription'] == str('Ergebnis nach Ende der offiziellen Spielzeit'):
                        team2points.append(i['MatchResults'][0]['PointsTeam2'])
                    else:
                        team2points.append(i['MatchResults'][1]['PointsTeam2'])
                    date.append(i['MatchDateTimeUTC'])
                    matchday.append(i['Group']['GroupOrderID'])
                    if i['Location'] is None:
                        location.append('Unbekannt')
                    else:
                        location.append(i['Location']['LocationCity'])

                else:
                    continue
            gameday = gameday + 1

    # Check to see if year is smaller than UntilYear
    if (year < UntilYear) & (basicyear == year):

        # Loop to go through all the gamedays
        while gameday <= 34:

            # The data from the URL is saved in a dictionary
            r = requests.get('https://www.openligadb.de/api/getmatchdata/bl1/' + str(year) + '/' + str(gameday))
            r_dict = r.json()

            # The loop goes through all the information in the dictionary and adds the information to the right array
            for i in r_dict:
                if i['MatchIsFinished']:
                    team1.append(i['Team1']['TeamName'])
                    team2.append(i['Team2']['TeamName'])
                    if i['MatchResults'][0]['ResultDescription'] == str('Ergebnis nach Ende der offiziellen Spielzeit'):
                        team1points.append(i['MatchResults'][0]['PointsTeam1'])
                    else:
                        team1points.append(i['MatchResults'][1]['PointsTeam1'])
                    if i['MatchResults'][0]['ResultDescription'] == str('Ergebnis nach Ende der offiziellen Spielzeit'):
                        team2points.append(i['MatchResults'][0]['PointsTeam2'])
                    else:
                        team2points.append(i['MatchResults'][1]['PointsTeam2'])
                    date.append(i['MatchDateTimeUTC'])
                    matchday.append(i['Group']['GroupOrderID'])
                    if i['Location'] is None:
                        location.append('Unbekannt')
                    else:
                        location.append(i['Location']['LocationCity'])

                else:
                    continue
            gameday = gameday + 1

        year = year + 1

    # Check to see if year is smaller than UntilYear
    if year < UntilYear:

        # Loop to collect all data from a while season
        while year < UntilYear:

            # The data from the URL is saved in a dictionary
            r = requests.get('https://www.openligadb.de/api/getmatchdata/bl1/' + str(year))
            r_dict = r.json()

            # The loop goes through all the information in the dictionary and adds the information to the right array
            for i in r_dict:
                if i['MatchIsFinished']:
                    team1.append(i['Team1']['TeamName'])
                    team2.append(i['Team2']['TeamName'])
                    if i['MatchResults'][0]['ResultDescription'] == str('Ergebnis nach Ende der offiziellen Spielzeit'):
                        team1points.append(i['MatchResults'][0]['PointsTeam1'])
                    else:
                        team1points.append(i['MatchResults'][1]['PointsTeam1'])
                    if i['MatchResults'][0]['ResultDescription'] == str('Ergebnis nach Ende der offiziellen Spielzeit'):
                        team2points.append(i['MatchResults'][0]['PointsTeam2'])
                    else:
                        team2points.append(i['MatchResults'][1]['PointsTeam2'])
                    date.append(i['MatchDateTimeUTC'])
                    matchday.append(i['Group']['GroupOrderID'])
                    if i['Location'] is None:
                        location.append('Unbekannt')
                    else:
                        location.append(i['Location']['LocationCity'])

                else:
                    continue

            year = year + 1

    # Condition to see if the year equals UntilYear
    if year == UntilYear:
        gameday = 1

        # The loop goes through all the gamedays in UntilYear
        while gameday <= UntilGameday:

            # The data from the URL is saved in a dictionary
            r = requests.get('https://www.openligadb.de/api/getmatchdata/bl1/' + str(year) + '/' + str(gameday))
            r_dict = r.json()

            # The loop goes through all the information in the dictionary and adds the information to the right array
            for i in r_dict:
                if i['MatchIsFinished']:
                    team1.append(i['Team1']['TeamName'])
                    team2.append(i['Team2']['TeamName'])
                    if i['MatchResults'][0]['ResultDescription'] == str('Ergebnis nach Ende der offiziellen Spielzeit'):
                        team1points.append(i['MatchResults'][0]['PointsTeam1'])
                    else:
                        team1points.append(i['MatchResults'][1]['PointsTeam1'])
                    if i['MatchResults'][0]['ResultDescription'] == str('Ergebnis nach Ende der offiziellen Spielzeit'):
                        team2points.append(i['MatchResults'][0]['PointsTeam2'])
                    else:
                        team2points.append(i['MatchResults'][1]['PointsTeam2'])
                    date.append(i['MatchDateTimeUTC'])
                    matchday.append(i['Group']['GroupOrderID'])
                    if i['Location'] is None:
                        location.append('Unbekannt')
                    else:
                        location.append(i['Location']['LocationCity'])

                else:
                    continue

            gameday = gameday + 1

    # Creating a dictionary with all the relevant information
    data = {
        'Location': location,
        'Date': date,
        'Matchday': matchday,
        'Team1': team1,
        'GoalsTeam1': team1points,
        'GoalsTeam2': team2points,
        'Team2': team2
        }

    # Creating a CSV file to store the information
    df = pd.DataFrame(data)
    df.to_csv('Crawler.csv', index=False)

    return "Selected data fetched."


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
    team2points: List[Any] = []
    location = []
    date = []
    matchday = []

    # Loop to collect all data until the current year
    while year < datetime.now().year:
        r = requests.get('https://www.openligadb.de/api/getmatchdata/bl1/' + str(year))
        r_dict = r.json()

        # The loop goes through all the information in the dictionary and adds the information to the right array
        for i in r_dict:
            if i['MatchIsFinished']:
                team1.append(i['Team1']['TeamName'])
                team2.append(i['Team2']['TeamName'])
                if (i['MatchResults'][0]['ResultDescription']) == str('Ergebnis nach Ende der offiziellen Spielzeit'):
                    team1points.append(i['MatchResults'][0]['PointsTeam1'])
                else:
                    team1points.append(i['MatchResults'][1]['PointsTeam1'])
                if (i['MatchResults'][0]['ResultDescription']) == str('Ergebnis nach Ende der offiziellen Spielzeit'):
                    team2points.append(i['MatchResults'][0]['PointsTeam2'])
                else:
                    team2points.append(i['MatchResults'][1]['PointsTeam2'])
                date.append(i['MatchDateTimeUTC'])
                matchday.append(i['Group']['GroupOrderID'])
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
            'Matchday': matchday,
            'Team1': team1,
            'GoalsTeam1': team1points,
            'GoalsTeam2': team2points,
            'Team2': team2
        }

        # Creating a CSV file to store the information
        df = pd.DataFrame(data)
        df.to_csv('Crawler.csv', index=False)

        year = year + 1
    return "All data fetched."


