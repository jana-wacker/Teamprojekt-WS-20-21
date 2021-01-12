Soccer Predictions 
---------------


What does it do? 
=====

Soccer is the national sport of many countries, e.g. in Germany, society holds its breath every time the german team plays. 
This implies that a majority of people are wrecking their brains before a game wondering who will win. 

For that, we have a fast, easy-to-use solution! 
Our software gives you a fast prediciton using **three algorithms** on how your favorite team is going to hold up in the next game. 
All you need to do is select some details and you are ready to shine at the next beting event! 


How to use it? 
===========

This software is super simple to use, and here is how step by step: 

0. Make sure a Python version >3 is installed on your device. 
1. Select the two teams you want a prediction for 
2. Select one of the algorithms you want to use for this prediction 
3. Select the time frame for the data, the calculation is based on 

All done! 


Pictures
============

INSERT PICTURES 


Necessary packages for Python
=====

The following packages are necessary to have the software run smooth: 
-tkinter 
-pillow
-
-


The process of development
===================


Structure of the git repository 
===================
The following is a short overview of how our project is structured here on git::

    .
    ├── README.rst                      project front page
    ├── setup.py                        packaging script
    ├── setup.cfg                       package metadata and tool config
    ├── MANIFEST.in                     lists data files to be included
    ├── .gitignore                      lists files to be ignored by git
    │
    ├── teamproject
    │   ├── __init__.py                 toplevel package variables
    │   ├── __main__.py                 invoked on `python -m teamproject`
    │   ├── crawler.py                  web-crawler / queries
    │   ├── gui.py                      defines the gui code
    │   └── models.py                   ML code for predictions
    │
    └── tests
        ├── test_crawler.py             tests grouped by functionality
        ├── ....
        └── test_models.py


Contact to the creators 
===================
If any issues may occur while using our software or you would like to help us further improve out application, feel free to reach out to us: 

Jana Wacker - 
Hanni Hille - 
Nora Siegel - 
Yupei Yang - 
