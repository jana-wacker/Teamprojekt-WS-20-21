from unittest import TestCase


class Test(TestCase):
    """function: try to test the checkMatch method in poissonDistribution, to make sure that
                     the result of match is non-negative and the type of output is int64."""
    def test_check_match(self):
        from teamproject.Algorithms.poissonDistribution import checkMatch
        assert (checkMatch(data) >= 0)
        assert (checkMatch(data).dtype == 'int64')

    def test_home_team_win(self):
        """function: try to test the HomeTeamWin method in poissonDistribution, to make sure that
                     the result of percentage is non-negative and the output type is float64."""
        from teamproject.Algorithms.poissonDistribution import HomeTeamWin
        assert (HomeTeamWin(data) >= 0)
        assert (HomeTeamWin(data).dtype == 'float64')

    def test_away_team_win(self):
        """function: try to test the AwayTeamWin method in poissonDistribution, to make sure that
                     the result of percentage is non-negative and the output type is float64."""
        from teamproject.Algorithms.poissonDistribution import AwayTeamWin
        assert (AwayTeamWin(data) >= 0)
        assert (AwayTeamWin(data).dtype == 'float64')

    def test_predict_home_team_goal(self):
        """function: try to test the PredictHomeTeamGoal method in poissonDistribution, to make sure that
                     the result of percentage is non-negative and the output type is float64."""
        from teamproject.Algorithms.poissonDistribution import PredictHomeTeamGoal
        assert (PredictHomeTeamGoal(data) >= 0)
        assert (PredictHomeTeamGoal(data).dtype == 'float64')

    def test_predict_tied(self):
        """function: try to test the PredictTied method in poissonDistribution, to make sure that
                     the result of percentage is non-negative and the output type is float64."""
        from teamproject.Algorithms.poissonDistribution import PredictTied
        assert (PredictTied(data) >= 0)
        assert (PredictTied(data).dtype == 'float64')

    def test_predict_away_team_goal(self):
        """function: try to test the PredictAwayTeamGoal method in poissonDistribution, to make sure that
                     the result of percentage is non-negative and the output type is float64."""
        from teamproject.Algorithms.poissonDistribution import PredictAwayTeamGoal
        assert (PredictAwayTeamGoal(data) >= 0)
        assert (PredictAwayTeamGoal(data).dtype == 'float64')
