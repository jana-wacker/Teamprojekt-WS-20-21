from unittest import TestCase
from teamproject.Algorithms.Minimal import data


class Test(TestCase):
    """function: try to test the machtNumber method in Minimal, to make sure that
                 the result of match is non-negative and the type of output is int64."""
    def test_match_number(self):
        from teamproject.Algorithms.Minimal import matchNumber
        assert (matchNumber(data) >= 0)
        assert (matchNumber(data).dtype == 'int64')

    def test_pro_home_win(self):
        """function: try to test the ProHomeWin method in Minimal, to make sure that
                     the result of percentage is non-negative and the output type is float64."""
        from teamproject.Algorithms.Minimal import ProHomeWin
        assert (ProHomeWin(data) >= 0)
        assert (ProHomeWin(data).dtype == 'float64')

    def test_pro_home_loss(self):
        """function: try to test the ProHomeLoss method in Minimal, to make sure that
                     the result of percentage is non-negative and the output type is float64."""
        from teamproject.Algorithms.Minimal import ProHomeLoss
        assert (ProHomeLoss(data) >= 0)
        assert (ProHomeLoss(data).dtype == 'float64')

    def test_pro_home_tied(self):
        """function: try to test the ProHomeTied method in Minimal, to make sure that
                     the result of percentage is non-negative and the output type is float64."""
        from teamproject.Algorithms.Minimal import ProHomeTied
        assert (ProHomeTied(data) >= 0)
        assert (ProHomeTied(data).dtype == 'float64')