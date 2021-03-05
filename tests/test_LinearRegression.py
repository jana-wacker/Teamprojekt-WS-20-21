"""This module tests all functions of Linear Regression.py"""

import unittest


class Test(unittest.TestCase):

    def test_match_count(self):
        """function: try to test the matchCount method in LinearRegression, to make sure that
                     the result of match is non-negative and the type is int64."""
        from teamproject.Algorithms.LinearRegression import matchCount
        assert (matchCount(data) >= 0)
        assert (matchCount(data).dtype == 'int64')

    def test_score_intercept(self):
        """function: try to test the scoreIntercept method in LinearRegression, to make sure that
                     the type of it is float64."""
        from teamproject.Algorithms.LinearRegression import scoreIntercept
        assert (scoreIntercept(data).dtype == 'float64')

    def test_score_coefhomeoraway(self):
        """function: try to test the scoreCoefhomeoraway method in LinearRegression, to make sure that
                     the type of it is float64."""
        from teamproject.Algorithms.LinearRegression import scoreCoefhomeoraway
        assert (scoreCoefhomeoraway(data).dtype == 'float64')

    def test_score_coefavg(self):
        """function: try to test the scoreCoefavg method in LinearRegression, to make sure that
                     the type of it is float64."""
        from teamproject.Algorithms.LinearRegression import scoreCoefavg
        assert (scoreCoefavg(data).dtype == 'float64')

    def test_home_score(self):
        """function: try to test the homeScore method in LinearRegression, to make sure that
                     the result of match is non-negative and the type is float64."""
        from teamproject.Algorithms.LinearRegression import homeScore
        assert (homeScore(data) >= 0)
        assert (homeScore(data).dtype == 'float64')

    def test_away_score(self):
        """function: try to test the awayScore method in LinearRegression, to make sure that
                     the result of match is non-negative and the type is float64."""
        from teamproject.Algorithms.LinearRegression import awayScore
        assert (awayScore(data) >= 0)
        assert (awayScore(data).dtype == 'float64')

    def test_percentage_intercept(self):
        """function: try to test the percentageIntercept method in LinearRegression, to make sure that
                     the result type is float64."""
        from teamproject.Algorithms.LinearRegression import percentageIntercept
        assert (percentageIntercept(data).dtype == 'float')

    def test_percentage_coefhomeoraway(self):
        """function: try to test the percentageCoefhomeoraway method in LinearRegression, to make sure that
                     the result type is float64."""
        from teamproject.Algorithms.LinearRegression import percentageCoefhomeoraway
        assert (percentageCoefhomeoraway(data).dtype == 'float64')

    def test_percentage_coefavg(self):
        """function: try to test the percentageCoefavg method in LinearRegression, to make sure that
                     the result type is float64."""
        from teamproject.Algorithms.LinearRegression import percentageCoefavg
        assert (percentageCoefavg(data).dtype == 'float64')

    def test_home_percentage(self):
        """function: try to test the homePercentage method in LinearRegression, to make sure that
                     the result is non-negative and the type is float64."""
        from teamproject.Algorithms.LinearRegression import homePercentage
        assert (homePercentage(data).dtype == 'float64')
        assert (homePercentage(data) >= 0)

    def test_away_percentage(self):
        """function: try to test the awayPercentage method in LinearRegression, to make sure that
                     the result is non-negative and the type is float64."""
        from teamproject.Algorithms.LinearRegression import awayPercentage
        assert (awayPercentage(data).dtype == 'float64')
        assert (awayPercentage(data) >= 0)

    def test_tied_precentage(self):
        """function: try to test the tiedPercentage method in LinearRegression, to make sure that
                     the result is non-negative and the type is float64."""
        from teamproject.Algorithms.LinearRegression import tiedPrecentage
        assert (tiedPrecentage(data).dtype == 'float64')
        assert (tiedPrecentage(data) >= 0)

    def test_sumof_percentage(self):
        """function: try to test the sumofPercentage method in LinearRegression, to make sure that
                     the result is non-negative."""
        from teamproject.Algorithms.LinearRegression import sumofPercentage
        assert (sumofPercentage(data) >= 0)


if __name__ == '__main__':
    unittest.main()
