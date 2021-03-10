from unittest import TestCase
import crawler
import os
import pandas as pd


class Test(TestCase):
    alldata = os.path.join(os.path.dirname(__file__), 'Crawler.csv')
    global data
    data = pd.read_csv(alldata)


    def test_match_count(self):
        """function: try to test the matchCount method in LinearRegression, to make sure that
                     the result of match is non-negative and the type is int64."""
        from teamproject.Algorithms.LinearRegression import matchCount
        self.assertTrue(matchCount('FC Bayern München','Hertha BSC',data) >= 0)
        self.assertIsInstance(matchCount('FC Bayern München','Hertha BSC',data), int)

    def test_home_percentage(self):
        """function: try to test the homePercentage method in LinearRegression, to make sure that
                     the result is non-negative."""
        from teamproject.Algorithms.LinearRegression import homePercentage
        self.assertTrue(homePercentage('FC Bayern München','Hertha BSC',data) >= 0)

    def test_away_percentage(self):
        """function: try to test the awayPercentage method in LinearRegression, to make sure that
                     the result is non-negative."""
        from teamproject.Algorithms.LinearRegression import awayPercentage
        self.assertTrue(awayPercentage('FC Bayern München','Hertha BSC',data) >= 0)

    def test_tied_precentage(self):
        """function: try to test the tiedPercentage method in LinearRegression, to make sure that
                     the result is non-negative."""
        from teamproject.Algorithms.LinearRegression import tiedPrecentage
        self.assertTrue(tiedPrecentage('FC Bayern München','Hertha BSC',data) >= 0)
