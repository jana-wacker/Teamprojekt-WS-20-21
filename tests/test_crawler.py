"""This module tests all functions of crawler.py"""

import teamproject.crawler as crawler
import pandas as pd
import csv
import datetime
import unittest


def test_fetch_matchday():
    """Jana: Fehler ist #TypeError: string indices must be integers#"""
    data = crawler.fetch_matchday()
    #assert isinstance(data, pd.DataFrame)
    with open('../teamproject/Matchdays.csv', mode='r') as csv_file:

        for row in csv_file:
            # Test to see if Matchday is a string
            assert type(row['Matchday']) == str
            # Test to see if Team1 is a string
            assert type(row['Team1']) == str
            # Test to see if Team2 is a string
            assert type(row['Team2']) == str
            # Test to see if Team1 is not the same as Team2
            assert row(['Team1']) != row(['Team1'])
            # Test to see if MatchNr is an int
            assert type(row['Team2']) == 'int64'

def test_fetch_data():
    """
    Test to check if the Locations are a strings
    Test to check if the Dates are from the type datetime
    Test to check if the Teamnames are strings
    Test to check if the Goals are integers
    Test to check if the Matchdays are integers
    """
    data = crawler.fetch_data()
    with open('../teamproject/Crawler.csv', mode='r') as csv_file:
        for row in csv_file:
            assert type(row['Location']) == str
            assert type(row['Date']) == datetime.isoformat()
            assert type(row['Team1']) == str
            assert type(row['Team2']) == str
            assert type(row['GoalsTeam1']) == int
            assert type(row['GoalsTeam2']) == int
            assert type(row['Matchday']) == int

def test_teamnames():
    """
    Test to check if team1 and team2 are different teams
    """
    data = crawler.fetch_data()
    with open('../teamproject/Crawler.csv', mode='r') as csv_file:
        for row in csv_file:
            assert str(row['Team1']) != str(row['Team2'])

def test_goals():
    """
    Test to check if the Goals are all equal or bigger than 0 and smaller than 12
    """
    data = crawler.fetch_data()
    with open('../teamproject/Crawler.csv', mode='r') as csv_file:
        for row in csv_file:
            assert (int(row['GoalsTeam1'])) >= 0
            assert (int(row['GoalsTeam1'])) <= 12
            assert (int(row['GoalsTeam2'])) >= 0
            assert (int(row['GoalsTeam2'])) <= 12

def test_date():
    """
    Test to see if the year is realistic
    """
    data = crawler.fetch_data()
    with open('../teamproject/Crawler.csv', mode='r') as csv_file:
        for row in csv_file:
            assert (row['Date']) <= datetime.now()
            assert (row['Date']) >= datetime(2004, 8, 6)

def test_gamedays():
    """
    Test to see if the number of gamedays is between 1 and 34
    """
    data = crawler.fetch_data()
    with open('../teamproject/Crawler.csv', mode='r') as csv_file:
        for row in csv_file:
            assert (int(row['Matchday'])) > 0
            assert (int(row['Matchday'])) <= 34

def test_fetch_all_data():
    """
    Test to check if the Locations are a strings
    Test to check if the Dates are from the type datetime
    Test to check if the Teamnames are strings
    Test to check if the Goals are integers
    Test to check if the Matchdays are integers
    """
    data = crawler.fetch_all_data()
    with open('../teamproject/Crawlercopy.csv', mode='r') as csv_file:
        for row in csv_file:
            assert type(row['Location']) == str
            assert type(row['Date']) == datetime.isoformat()
            assert type(row['Team1']) == str
            assert type(row['Team2']) == str
            assert type(row['GoalsTeam1']) == int
            assert type(row['GoalsTeam2']) == int
            assert type(row['Matchday']) == int

def test_all_teamnames():
    """
    Test to check if team1 and team2 are different teams
    """
    data = crawler.fetch_all_data()
    with open('../teamproject/Crawlercopy.csv', mode='r') as csv_file:
        for row in csv_file:
            assert str(row['Team1']) != str(row['Team2'])

def test_all_goals():
    """
    Test to check if the Goals are all equal or bigger than 0 and smaller than 12
    """
    data = crawler.fetch_all_data()
    with open('../teamproject/Crawlercopy.csv', mode='r') as csv_file:
        for row in csv_file:
            assert (int(row['GoalsTeam1'])) >= 0
            assert (int(row['GoalsTeam1'])) <= 12
            assert (int(row['GoalsTeam2'])) >= 0
            assert (int(row['GoalsTeam2'])) <= 12


def test_all_date():
    """
    Test to see if the date is realistic
    """
    data = crawler.fetch_all_data()
    with open('../teamproject/Crawlercopy.csv', mode='r') as csv_file:
        for row in csv_file:
            assert (row['Date']) <= datetime.now()
            assert (row['Date']) >= datetime(2004, 8, 6)



def test_all_gamedays():
    """
    Test to see if the number of gamedays is between 1 and 34
    """
    data = crawler.fetch_all_data()
    with open('../teamproject/Crawlercopy.csv', mode='r') as csv_file:
        for row in csv_file:
            assert (int(row['Matchday'])) > 0
            assert (int(row['Matchday'])) <= 34

if __name__ == '__main__':
    unittest.main()