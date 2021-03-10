"""This module tests all functions of Poisson Distribution.py"""
import unittest
import os
import pandas as pd
import importlib

poisson_distribution_mod = importlib.import_module("teamproject.Algorithms.Poisson Distribution")


class Test(unittest.TestCase):
    alldata = os.path.join(os.path.dirname(__file__), '../teamproject/Crawler.csv')
    global data
    data = pd.read_csv(alldata)
    data = poisson_distribution_mod.encapsulation(data)

    def test_check_match (self):
        """function: try to test the checkMatch method in poissonDistribution, to make sure that
                     the result of match is non-negative and the type of output is int64."""
        self.assertTrue(poisson_distribution_mod.checkMatch('FC Bayern München', 'Hertha BSC', data) >= 0)
        self.assertIsInstance(poisson_distribution_mod.checkMatch('FC Bayern München', 'Hertha BSC', data), int)

    def test_home_team_win(self):
        """function: try to test the HomeTeamWin method in poissonDistribution, to make sure that
                     the result of percentage is non-negative."""
        self.assertTrue(poisson_distribution_mod.HomeTeamWin('FC Bayern München', 'Hertha BSC', data) >= 0)

    def test_away_team_win(self):
        """function: try to test the AwayTeamWin method in poissonDistribution, to make sure that
                     the result of percentage is non-negative."""
        self.assertTrue(poisson_distribution_mod.AwayTeamWin('FC Bayern München', 'Hertha BSC', data) >= 0)

    def test_predict_home_team_goal(self):
        """function: try to test the PredictHomeTeamGoal method in poissonDistribution, to make sure that
                     the result of percentage is non-negative."""
        self.assertTrue(poisson_distribution_mod.PredictHomeTeamGoal('FC Bayern München', 'Hertha BSC', data) >= 0)

    def test_predict_tied (self):
        """function: try to test the PredictTied method in poissonDistribution, to make sure that
                     the result of percentage is non-negative."""
        self.assertTrue(poisson_distribution_mod.PredictTied('FC Bayern München', 'Hertha BSC', data) >= 0)

    def test_predict_away_team_goal (self):
        """function: try to test the PredictAwayTeamGoal method in poissonDistribution, to make sure that
                     the result of percentage is non-negative."""
        self.assertTrue(poisson_distribution_mod.PredictAwayTeamGoal('FC Bayern München', 'Hertha BSC', data) >= 0)


if __name__ == '__main__':
    unittest.main()
