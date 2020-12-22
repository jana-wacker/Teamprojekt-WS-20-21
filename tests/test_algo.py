from unittest import TestCase
from teamproject.Algorithms.MinimalerVorhersageAlgo import data


class Test(TestCase):
    """function: try to test the machtNumber method in vorhersage_algo, to make sure that
                 the result of match is non-negative."""
    def test_match_number(self):
        from teamproject.Algorithms.MinimalerVorhersageAlgo import matchNumber
        assert (matchNumber(data) >= 0)

    """function: try to test the ProHomeWin method in vorhersage_algo, to make sure that
                 the result of procentage is non-negative."""
    def test_pro_home_win(self):
        from teamproject.Algorithms.MinimalerVorhersageAlgo import ProHomeWin
        assert (ProHomeWin(data) >= 0)

    """function: try to test the ProHomeLoss method in vorhersage_algo, to make sure that
                 the result of procentage is non-negative."""
    def test_pro_home_loss(self):
        from teamproject.Algorithms.MinimalerVorhersageAlgo import ProHomeLoss
        assert (ProHomeLoss(data) >= 0)

    """function: try to test the ProHomeTied method in vorhersage_algo, to make sure that
                 the result of procentage is non-negative."""
    def test_pro_home_tied(self):
        from teamproject.Algorithms.MinimalerVorhersageAlgo import ProHomeTied
        assert (ProHomeTied(data) >= 0)