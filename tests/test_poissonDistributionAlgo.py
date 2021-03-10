from unittest import TestCase
import crawler
import os
import pandas as pd

class Test(TestCase):
    alldata = os.path.join(os.path.dirname(__file__), 'Crawler.csv')
    global data
    data = pd.read_csv(alldata)

    def test_check_match(self):
        """function: try to test the checkMatch method in poissonDistribution, to make sure that
                     the result of match is non-negative and the type of output is int64."""
        from teamproject.Algorithms.poissonDistribution import checkMatch
        self.assertTrue(checkMatch('FC Bayern München','Hertha BSC',data) >= 0)
        self.assertIsInstance(checkMatch('FC Bayern München','Hertha BSC',data), int)


    def test_home_team_win(self):
        """function: try to test the HomeTeamWin method in poissonDistribution, to make sure that
                     the result of percentage is non-negative."""
        from teamproject.Algorithms.poissonDistribution import HomeTeamWin
        self.assertTrue(HomeTeamWin('FC Bayern München','Hertha BSC',data) >= 0)


    def test_away_team_win(self):
        """function: try to test the AwayTeamWin method in poissonDistribution, to make sure that
                     the result of percentage is non-negative."""
        from teamproject.Algorithms.poissonDistribution import AwayTeamWin
        self.assertTrue(AwayTeamWin('FC Bayern München','Hertha BSC',data) >= 0)


    def test_predict_home_team_goal(self):
        """function: try to test the PredictHomeTeamGoal method in poissonDistribution, to make sure that
                     the result of percentage is non-negative."""
        from teamproject.Algorithms.poissonDistribution import PredictHomeTeamGoal
        self.assertTrue(PredictHomeTeamGoal('FC Bayern München','Hertha BSC',data) >= 0)


    def test_predict_tied(self):
        """function: try to test the PredictTied method in poissonDistribution, to make sure that
                     the result of percentage is non-negative."""
        from teamproject.Algorithms.poissonDistribution import PredictTied
        self.assertTrue(PredictTied('FC Bayern München','Hertha BSC',data) >= 0)

    def test_predict_away_team_goal(self):
        """function: try to test the PredictAwayTeamGoal method in poissonDistribution, to make sure that
                     the result of percentage is non-negative."""
        from teamproject.Algorithms.poissonDistribution import PredictAwayTeamGoal
        self.assertTrue(PredictAwayTeamGoal('FC Bayern München','Hertha BSC',data) >= 0)