"""This module tests all functions of Linear Regression.py"""
import unittest
import os
import pandas as pd
import importlib

linear_regression_mod = importlib.import_module("teamproject.Algorithms.Linear Regression")


class Test(unittest.TestCase):
    # import data
    alldata = os.path.join(os.path.dirname(__file__), '../teamproject/Crawler.csv')
    global data
    data = pd.read_csv(alldata)

    def test_match_count (self):
        """function: try to test the matchCount method in LinearRegression, to make sure that
                     the result of match is non-negative and the type is int64."""
        self.assertTrue(linear_regression_mod.matchCount('FC Bayern München', 'Hertha BSC', data) >= 0)
        self.assertIsInstance(linear_regression_mod.matchCount('FC Bayern München', 'Hertha BSC', data), int)

    def test_home_percentage(self):
        """function: try to test the homePercentage method in LinearRegression, to make sure that
                     the result is non-negative."""

        self.assertTrue(linear_regression_mod.homePercentage('FC Bayern München', 'Hertha BSC', data) >= 0)

    def test_away_percentage (self):
        """function: try to test the awayPercentage method in LinearRegression, to make sure that
                     the result is non-negative."""
        self.assertTrue(linear_regression_mod.awayPercentage('FC Bayern München', 'Hertha BSC', data) >= 0)

    def test_tied_precentage (self):
        """function: try to test the tiedPercentage method in LinearRegression, to make sure that
                     the result is non-negative."""
        self.assertTrue(linear_regression_mod.tiedPrecentage('FC Bayern München', 'Hertha BSC', data) >= 0)


if __name__ == '__main__':
    unittest.main()
