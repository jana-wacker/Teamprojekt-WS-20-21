# Use this file to test your crawler.

from teamproject import crawler
import pandas as pd
import csv


# Example test:
def test_fetch_data():
    data = crawler.fetch_data()
    assert isinstance(data, pd.DataFrame)
    assert data.home_score.dtype == 'int64'
    assert data.guest_score.dtype == 'int64'
    assert (data.home_score >= 0).all()
    assert (data.guest_score >= 0).all()
    assert (data.home_team != data.guest_team).all()


def test_fetch_all_data():
    data = crawler.fetch_data()
    print(data)
    assert isinstance(data, pd.DataFrame)
    assert data.team1points.dtype == 'int64'
    assert data.team2points.dtype == 'int64'
    assert (data.team1points >= 0).all()
    assert (data.team2points >= 0).all()
    assert (data.team1 != data.team2).all()

# Test to see if the number of gamedays is between 1 and 34
def test_number_of_gamedays():
    data = crawler.fetch_all_data()
    assert isinstance(data, pd.DataFrame)
    assert (data.gameday > 0 & data.gameday <= 34).all()

# Test to see if there are exactly 18 teams per season
def test_number_of_teams_per_season():
    data = crawler.fetch_all_data()
    assert isinstance(data, pd.DataFrame)
    assert data.team1 == 18

# Test to see if there are 34 gamedays
def test_team_names():
    data = crawler.fetch_all_data()
    assert isinstance(data, pd.DataFrame)
    assert data.gameday == 34

# Test to see if the year is realistic
def test_year():
    data = crawler.fetch_all_data()
    assert isinstance(data, pd.DataFrame)
    assert (data.year >= 2004 & data.year <= 2021).all()

crawler.fetch_all_data()
def test_fetch_all_data1():
    with open('Alldata.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_file:
            # Test to see if the Location is a String
            assert type(row['Location']) == str
            # Test to see if the amount of goals from team1 is an Integer
            assert type(row['GoalsTeam1']) == int
            # Test to see if the amount of goals from team2 is an Integer
            assert type(row['GoalsTeam2']) == int
            # Test to see if the number of goals is realistic
            assert (int(row['GoalsTeam1']) >= 0 & int(row['GoalsTeam1'] <= 15))
            assert (int(row['GoalsTeam2']) >= 0 & int(row['GoalsTeam2'] <= 15))

def fetch_all_data1():
    data = crawler.fetch_all_data()
    print(data)

fetch_all_data1()




