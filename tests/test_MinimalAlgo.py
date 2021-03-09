from unittest import TestCase
import crawler


class Test(TestCase):
    """function: try to test the machtNumber method in Minimal, to make sure that
                 the result of match is non-negative and the type of output is int64."""
    def test_match_number(self):
        from teamproject.Algorithms.Minimal import matchNumber
        data = crawler.fetch_data()
        assert (matchNumber(data) >= 0)
        assert (matchNumber(data).dtype == 'int64')


    def test_pro_home_win(self):
        """function: try to test the ProHomeWin method in Minimal, to make sure that
                     the result of percentage is non-negative and the output type is float64."""
        from teamproject.Algorithms.Minimal import ProHomeWin
        data = crawler.fetch_data()
        assert (ProHomeWin(data) >= 0)
        assert (ProHomeWin(data).dtype == 'float64')

    def test_pro_home_loss(self):
        """function: try to test the ProHomeLoss method in Minimal, to make sure that
                     the result of percentage is non-negative and the output type is float64."""
        from teamproject.Algorithms.Minimal import ProHomeLoss
        data = crawler.fetch_data()
        assert (ProHomeLoss(data) >= 0)
        assert (ProHomeLoss(data).dtype == 'float64')

    def test_pro_home_tied(self):
        """function: try to test the ProHomeTied method in Minimal, to make sure that
                     the result of percentage is non-negative and the output type is float64."""
        from teamproject.Algorithms.Minimal import ProHomeTied
        data = crawler.fetch_data()
        assert (ProHomeTied(data) >= 0)
        assert (ProHomeTied(data).dtype == 'float64')