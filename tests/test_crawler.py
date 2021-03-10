"""This module tests all functions of crawler.py"""
import teamproject.crawler as crawler
import pandas as pd
import csv
from datetime import datetime
import unittest


class test_crawler(unittest.TestCase):

    def test_fetch_matchday (self):
        """Test to see if Matchday is a string
            Test to see if Team1 is a string
            Test to see if Team2 is a string
            Test to see if Team1 is not the same as Team2
            Test to see if MatchNr is a string
        """
        try:
            crawler.fetch_matchday()
        except:
            raise Exception('Crawler could not fetch matchdays.')

        with open('../teamproject/Matchdays.csv', encoding='utf8', mode='r') as csv_file:
            data = csv.DictReader(csv_file, delimiter=',')
            for row in data:
                assert type(row['Matchday']) == str
                assert type(row['Team1']) == str
                assert type(row['Team2']) == str
                assert row['Team1'] != row['Team2']
                assert type(row['MatchNr']) == str

    def test_teamnames (self):
        """
        Test to check if team1 and team2 are different teams
        """
        try:
            crawler.fetch_data(2004, 1, 2005, 1)
        except:
            raise Exception('Crawler could not fetch selected data.')
        with open('../teamproject/Crawler.csv', encoding='utf8', mode='r') as csv_file:
            data = csv.DictReader(csv_file, delimiter=',')
            for row in data:
                assert row['Team1'] != row['Team2']

    def test_goals (self):
        """
        Test to check if the Goals are all equal or bigger than 0 and smaller than 12
        """
        try:
            crawler.fetch_data(2004, 1, 2005, 1)
        except:
            raise Exception('Crawler could not fetch selected data.')
        with open('../teamproject/Crawler.csv', encoding='utf8', mode='r') as csv_file:
            data = csv.DictReader(csv_file, delimiter=',')
            for row in data:
                assert str((row['GoalsTeam1']) >= str(0))
                assert str((row['GoalsTeam1']) <= str(12))
                assert str((row['GoalsTeam2']) >= str(0))
                assert str((row['GoalsTeam2']) <= str(12))

    def test_date (self):
        """
        Test to see if the year is realistic
        """
        try:
            crawler.fetch_data(2004, 1, 2005, 1)
        except:
            raise Exception('Crawler could not fetch selected data.')

        with open('../teamproject/Crawler.csv', encoding='utf8', mode='r') as csv_file:
            data = csv.DictReader(csv_file, delimiter=',')
            for row in data:
                assert str(row['Date']) <= str(datetime.now())
                assert str(row['Date']) >= str((datetime(2004, 8, 6)))

    def test_gamedays (self):
        """
        Test to see if the number of gamedays is between 1 and 34
        """
        crawler.fetch_data(2004, 1, 2005, 1)
        with open('../teamproject/Crawler.csv', encoding='utf8', mode='r') as csv_file:
            data = csv.DictReader(csv_file, delimiter=',')
            for row in data:
                assert str((row['Matchday']) > str(0))
                assert str((row['Matchday']) <= str(34))

    def test_fetch_all_data (self):
        """Test to check if the Locations are strings
        Test to check if the Dates are strings
        Test to check if the Teamnames are strings
        Test to check if the Goals are strings
        Test to check if the Matchdays are strings
        """
        try:
            crawler.fetch_all_data()
        except:
            raise Exception('Crawler could not fetch all data.')

        with open('../teamproject/Crawler.csv', encoding='utf8', mode='r') as csv_file:
            data = csv.DictReader(csv_file, delimiter=',')
            for row in data:
                assert type(row['Location']) == str
                assert type(row['Date']) == str
                assert type(row['Team1']) == str
                assert type(row['Team2']) == str
                assert type(row['GoalsTeam1']) == str
                assert type(row['GoalsTeam2']) == str
                assert type(row['Matchday']) == str

    def test_all_teamnames (self):
        """
        Test to check if team1 and team2 are different teams
        """
        try:
            crawler.fetch_all_data()
        except:
            raise Exception('Crawler could not fetch all data.')
        with open('../teamproject/Crawler.csv', encoding='utf8', mode='r') as csv_file:
            data = csv.DictReader(csv_file, delimiter=',')
            for row in data:
                assert str(row['Team1']) != str(row['Team2'])

    def test_all_goals (self):
        """
        Test to check if the Goals are all equal or bigger than 0 and smaller than 12
        """
        try:
            crawler.fetch_all_data()
        except:
            raise Exception('Crawler could not fetch all data.')
        with open('../teamproject/Crawler.csv', encoding='utf8', mode='r') as csv_file:
            data = csv.DictReader(csv_file, delimiter=',')
            for row in data:
                assert str((row['GoalsTeam1']) >= str(0))
                assert str((row['GoalsTeam1']) <= str(12))
                assert str((row['GoalsTeam2']) >= str(0))
                assert str((row['GoalsTeam2']) <= str(12))

    def test_all_date (self):
        """
        Test to see if the date is realistic
        """
        try:
            crawler.fetch_all_data()
        except:
            raise Exception('Crawler could not fetch all data.')
        with open('../teamproject/Crawler.csv', encoding='utf8', mode='r') as csv_file:
            data = csv.DictReader(csv_file, delimiter=',')
            for row in data:
                assert str(row['Date']) <= str(datetime.now())
                assert str(row['Date']) >= str(datetime(2004, 8, 6))

    def test_all_gamedays (self):
        """
        Test to see if the number of gamedays is between 1 and 34
        """
        try:
            crawler.fetch_all_data()
        except:
            raise Exception('Crawler could not fetch all data.')
        with open('../teamproject/Crawler.csv', encoding='utf8', mode='r') as csv_file:
            data = csv.DictReader(csv_file, delimiter=',')
            for row in data:
                assert str((row['Matchday']) > str(0))
                assert str((row['Matchday']) <= str(34))


if __name__ == '__main__':
    unittest.main()
