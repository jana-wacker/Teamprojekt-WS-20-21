from unittest import TestCase
from teamproject.vorhersage_algo import data

class Test(TestCase):
    """function: try to test the machtNumber method in vorhersage_algo, to make sure that
                 the result of match is non-negative."""
    def test_match_number(self):
        from teamproject.vorhersage_algo import matchNumber
        assert (matchNumber(data) >= 0)

    """function: try to test the ProHomeWin method in vorhersage_algo, to make sure that
                 the result of procentage is non-negative."""
    def test_pro_home_win(self):
        from teamproject.vorhersage_algo import ProHomeWin
        assert (ProHomeWin(data) >= 0)

    """function: try to test the ProHomeLoss method in vorhersage_algo, to make sure that
                 the result of procentage is non-negative."""
    def test_pro_home_loss(self):
        from teamproject.vorhersage_algo import ProHomeLoss
        assert (ProHomeLoss(data) >= 0)

    """function: try to test the ProHomeTied method in vorhersage_algo, to make sure that
                 the result of procentage is non-negative."""
    def test_pro_home_tied(self):
        from teamproject.vorhersage_algo import ProHomeTied
        assert (ProHomeTied(data) >= 0)