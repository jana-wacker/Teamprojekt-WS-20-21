"""
Run the application.

This module is invoked when calling ``python -m teamproject``.
"""
from gui import main
from Prediction_Algo import predict_winner
from crawler import fetch_data

main()
predict_winner()
fetch_data()


