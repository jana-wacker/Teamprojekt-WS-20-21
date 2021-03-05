# Use this file to test your crawler.

import teamproject.crawler as crawler
import pandas as pd
import csv
import datetime

# Example test:
#def test_fetch_data():
#    data = crawler.fetch_data()
#    assert isinstance(data, pd.DataFrame)
#    assert data.home_score.dtype == 'int64'
#    assert data.guest_score.dtype == 'int64'
#    assert (data.home_score >= 0).all()
#    assert (data.guest_score >= 0).all()
#    assert (data.home_team != data.guest_team).all()


def test_fetch_data():
    """
    Test to check if the teampoints are integers
    Test to check if the teampoints are all equal or bigger than 0
    Test to check if team1 and team2 are different teams
    """
    data = crawler.fetch_data()
    assert isinstance(data, pd.DataFrame)
    assert data.team1points.dtype == 'int64'
    assert data.team2points.dtype == 'int64'
    assert (data.team1points >= 0).all()
    assert (data.team2points >= 0).all()
    assert (data.team1 != data.team2).all()


def test_location():
    """
    Test to see if the name of the location is as string
    """
    data = crawler.fetch_data()
    assert isinstance(data, pd.DataFrame)
    assert type(data.location) == str.all()


def test_date():
    """
    Test to see if the date is realistic
    """
    data = crawler.fetch_data()
    assert isinstance(data, pd.DataFrame)
    assert data.date == datetime.isoformat().all()


def test_number_of_gamedays():
    """
    Test to see if the number of gamedays is between 1 and 34
    """
    data = crawler.fetch_data()
    assert isinstance(data, pd.DataFrame)
    assert (data.matchday > 0 & data.matchday <= 34).all()


def test_team_names():
    """
    Test to see if the team names are strings
    """
    data = crawler.fetch_data()
    assert isinstance(data, pd.DataFrame)
    assert type(data.team1) == str.all()
    assert type(data.team2) == str.all()


def test_year():
    """
    Test to see if the year is realistic
    """
    data = crawler.fetch_data()
    assert isinstance(data, pd.DataFrame)
    assert (data.year >= 2004 & data.year <= 2021).all()


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

def test_fetch_all_data1():
    """
        Test to see if the Location is a String
        Test to see if the amount of goals from team1 is an Integer
        Test to see if the amount of goals from team2 is an Integer
        Test to see if the number of goals is realistic
    """
    data = crawler.fetch_all_data()
    assert isinstance(data, pd.DataFrame)
    assert data.team1points.dtype == 'int64'
    assert data.team2points.dtype == 'int64'
    assert (data.team1points >= 0).all()
    assert (data.team2points >= 0).all()
    assert (data.team1 != data.team2).all()



def test_all_location():
    """
    Test to see if the name of the location is as string
    """
    data = crawler.fetch_all_data()
    assert isinstance(data, pd.DataFrame)
    assert type(data.location) == str.all()



def test_all_date():
    """
    Test to see if the date is realistic
    """
    data = crawler.fetch_all_data()
    assert isinstance(data, pd.DataFrame)
    assert data.date == datetime.isoformat().all()



def test_all_number_of_gamedays():
    """
    Test to see if the number of gamedays is between 1 and 34
    """
    data = crawler.fetch_all_data()
    assert isinstance(data, pd.DataFrame)
    assert (data.matchday > 0 & data.matchday <= 34).all()



def test_all_team_names():
    """
    Test to see if the team names are strings"
    """
    data = crawler.fetch_all_data()
    assert isinstance(data, pd.DataFrame)
    assert type(data.team1) == str.all()
    assert type(data.team2) == str.all()



def test_all_year():
    """
    Test to see if the year is realistic
    """
    data = crawler.fetch_all_data()
    assert isinstance(data, pd.DataFrame)
    assert (data.year >= 2004 & data.year <= 2021).all()