from unittest import TestCase
import crawler
import os
import pandas as pd


class Test(TestCase):
    alldata = os.path.join(os.path.dirname(__file__), 'Crawler.csv')
    global data
    data = pd.read_csv(alldata)

    global homeName
    homeName='Bayer Leverkusen'
    global guestName
    guestName='Hannover 96'

    def test_match_number(self):
        """function: try to test the machtNumber method in Minimal, to make sure that
                     the result of match is non-negative and the type of output is int."""
        from teamproject.Algorithms.Minimal import matchNumber
        self.assertTrue(matchNumber(data) >= 0)
        self.assertIsInstance(matchNumber(data), int)


    def test_pro_home_win(self):
        """function: try to test the ProHomeWin method in Minimal, to make sure that
                     the result of percentage is non-negative."""
        from teamproject.Algorithms.Minimal import ProHomeWin
        self.assertTrue(ProHomeWin(data) >= 0)

    def test_pro_home_loss(self):
        """function: try to test the ProHomeLoss method in Minimal, to make sure that
                     the result of percentage is non-negative."""
        from teamproject.Algorithms.Minimal import ProHomeLoss
        self.assertTrue(ProHomeLoss(data) >= 0)

    def test_pro_home_tied(self):
        """function: try to test the ProHomeTied method in Minimal, to make sure that
                     the result of percentage is non-negative."""
        from teamproject.Algorithms.Minimal import ProHomeTied
        self.assertTrue(ProHomeTied(data) >= 0)

