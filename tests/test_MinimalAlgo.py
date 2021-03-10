"""This module tests all functions of Minimal Prediction.py"""
import unittest
import os
import pandas as pd
import importlib

minimal_mod = importlib.import_module("teamproject.Algorithms.Minimal Prediction")


class Test(unittest.TestCase):
    alldata = os.path.join(os.path.dirname(__file__), '../teamproject/Crawler.csv')
    global data
    data = pd.read_csv(alldata)

    def test_match_number (self):
        """function: try to test the machtNumber method in Minimal, to make sure that
                     the result of match is non-negative and the type of output is int."""
        self.assertTrue(minimal_mod.matchNumber(data) >= 0)
        self.assertIsInstance(minimal_mod.matchNumber(data), int)

    def test_pro_home_win (self):
        """function: try to test the ProHomeWin method in Minimal, to make sure that
                     the result of percentage is non-negative."""
        self.assertTrue(minimal_mod.ProHomeWin(data) >= 0)

    def test_pro_home_loss (self):
        """function: try to test the ProHomeLoss method in Minimal, to make sure that
                     the result of percentage is non-negative."""
        self.assertTrue(minimal_mod.ProHomeLoss(data) >= 0)

    def test_pro_home_tied (self):
        """function: try to test the ProHomeTied method in Minimal, to make sure that
                     the result of percentage is non-negative."""
        self.assertTrue(minimal_mod.ProHomeTied(data) >= 0)


if __name__ == '__main__':
    unittest.main()
