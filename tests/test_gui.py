"""This module tests gui.py using mockist testing."""

import teamproject.gui as g
import teamproject.crawler as c
import teamproject.Algorithms
import tkinter as tk
import unittest
from unittest import mock


class test_gui(unittest.TestCase):
    def test_buttonOdds(self):
        """Tests if buttonOdds can be pressed and if it calls the correct function (syncAlgo)."""
        root = tk.Toplevel()
        window = g.gui(root)
        try:
            window.buttonOdds.invoke()
        except:
            raise Exception("buttonOdds could not be pressed.")
        syncAlgo_mock = mock.Mock(side_effect=window.syncAlgo)
        syncAlgo_mock()
        assert syncAlgo_mock.called
        assert syncAlgo_mock.call_count > 0

    def test_buttonCrawler(self):
        """Tests if buttonCrawler can be pressed and if calls the correct function (fetch_all_data)."""
        root = tk.Toplevel()
        window = g.gui(root)

        try:
            window.buttonCrawler.invoke()
        except:
            raise Exception('buttonCrawler could not be pressed.')
        fetch_all_data_mock = mock.Mock(side_effect=c.fetch_all_data)
        fetch_all_data_mock()
        assert fetch_all_data_mock.called
        assert fetch_all_data_mock.call_count > 0


    def test_buttonCrawler2(self):
        """Tests if buttonCrawler2 can be pressed and if calls the correct function (check_fetch)."""
        root = tk.Toplevel()
        window = g.gui(root)
        try:
            window.buttonCrawler2.invoke()
        except:
            raise Exception("buttonCrawler2 could not be pressed.")
        check_fetch_mock = mock.Mock(side_effect=window.check_fetch)
        check_fetch_mock(2004, 1, 2004, 2)
        assert check_fetch_mock.called
        assert check_fetch_mock.call_count > 0

if __name__ == '__main__':
    unittest.main()
