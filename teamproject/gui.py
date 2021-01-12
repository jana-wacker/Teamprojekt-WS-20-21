from tkinter import *
from PIL import Image, ImageTk
import pandas as pd
from crawler import fetch_data, fetch_all_data, fetch_matchday
from tkcalendar import DateEntry, Calendar
from datetime import datetime
from tkinter.messagebox import showinfo
import csv
import pkgutil
import Algorithms
import tkinter.font as font
import os
import importlib

# Open .csv-files
alldata = os.path.join(os.path.dirname(__file__), 'Crawler.csv')
data = pd.read_csv(alldata)

gamedates = os.path.join(os.path.dirname(__file__), 'Matchdays.csv')
dates = pd.read_csv(gamedates)

def getTeams():
    """
    Creates a dictionary with all teams, using the Crawler.csv as data basis
    :returns: all team-names(dictionary
    """
    with open(alldata, newline='', encoding="utf8") as all_data_raw:
        Teams = []
        all_data = csv.DictReader(all_data_raw, delimiter=',')
        for row in all_data:
            if row['Team1'] not in Teams:
                Teams.append(row['Team1'])
    Teams.sort()
    return Teams

def getMatchDays():
    """
    Creates a dictionary with upcoming match day, using the Matchdays.csv as data basis
    :returns: upcoming match days (dictionary)
    """
    with open(gamedates, newline='', encoding="utf8") as dates_raw:
        game_dates = csv.DictReader(dates_raw, delimiter=',')
        matches = []
        gameday = []

        # getting the next match day and adding it to 'matches'
        for row in game_dates:
            gameday.append(row['MatchNr'])
            match_name = ((str(row['Matchday'])) +
                          ': ' + (str(row['Team1'])) +
                          ' vs. ' + (str(row['Team2'])))
            matches.append(match_name)
            break

        # 'next' is upcoming match day
        global next
        next = gameday[0]

        for row in game_dates:
            if (row['MatchNr'] == next):
                match_name = ((str(row['Matchday'])) +
                              ': ' + (str(row['Team1'])) +
                              ' vs. ' + (str(row['Team2'])))
                matches.append(match_name)
    return matches

def main():
    """
    Creates and shows the main window
    """
    root = Tk()
    '''Needs to be activated before initial start of the program'''
    #fetch_all_data()
    #fetch_matchday()

    # Basics for the window
    root.geometry("1000x600")
    root.title("Bundesliga Vorhersagen")

    # Variables for the size of the picture
    x_Picture = 800
    y_Picture = 600

    # Setting the background
    background = os.path.join(os.path.dirname(__file__), 'field.jpg')
    image1 = Image.open(background)
    image1_resized = image1.resize((1800, 1600), Image.ANTIALIAS)
    pic_ready = ImageTk.PhotoImage(image1_resized)

    lable_background = Label(root, image=pic_ready)
    lable_background.image = pic_ready
    lable_background.place(x=0, y=0, relwidth=1, relheight=1)

    # Lable for the header
    myLable = Label(root, text="Erstelle hier Vorhersagen zu anstehenden Bundesliga Spielen!", justify=CENTER,
                    bg="light green")
    myLable.pack(side="top", padx=10)
    myLable.config(font=("Times", 20))

    # Marking where the lables start, depending on the size of the main window
    begin_Labels = x_Picture / 100
    end_Labels = y_Picture / 10

    # Setting up all the frames to insert the labels and the buttons into
    frameLeft = Frame(master=root, bg="red")
    frameLeft.pack(side="left", padx=begin_Labels, pady=10)

    rahmenMiddle = Frame(master=root, bg="cadetblue1")
    rahmenMiddle.pack(side="top", padx=begin_Labels, pady=20)

    rahmenBelow = Frame(master=root, bg="lightblue1")
    rahmenBelow.pack(side="bottom", padx=begin_Labels, pady=20)

    rahmenTeamHome = Frame(master=rahmenMiddle, bg="cadetblue3")
    rahmenTeamHome.pack(side="left", padx=5, pady=5)

    rahmenTeamGuest = Frame(master=rahmenMiddle, bg="cadetblue3")
    rahmenTeamGuest.pack(side="right", padx=5, pady=5)

    rahmenCalendar = Frame(master=rahmenMiddle, bg="cadetblue4")
    rahmenCalendar.pack(side="top", padx=15, pady=5)

    rahmenAlgo = Frame(master=rahmenBelow, bg="lightsteelblue2")
    rahmenAlgo.pack(side="left", padx=5, pady=5)

    rahmenCrawler = Frame(master=rahmenBelow, bg="lightsteelblue3")
    rahmenCrawler.pack(side="left", padx=5, pady=5)

    # All of the labels
    settingsLable = Label(rahmenCrawler, text="Activate the AI or Start the Crawler here:", bg="lightyellow2")
    settingsLable.pack(side="top", padx=5)
    settingsLable.config(font=("TKCaptionFont", 12))

    dropLable1 = Label(master=rahmenTeamHome, text="Choose the Home Team:", bg="royalblue1", fg="lightcyan1")
    dropLable1.pack(side="top", padx=5, pady=5)
    dropLable1.config(font=("TKCaptionFont", 12))

    dropLable2 = Label(master=rahmenTeamGuest, text="Choose the Away Team:", bg="lightcyan1", fg="royalblue1")
    dropLable2.pack(side="top", padx=5, pady=5)
    dropLable2.config(font=("TKCaptionFont", 12))

    chooseCrawlerLabel = Label(master=rahmenAlgo, text="Choose an Algorithm for calculation:")
    chooseCrawlerLabel.pack(side="top", padx=5, pady=5)
    chooseCrawlerLabel.config(font=("TKCaptionFont", 12))

    chooseDateLable = Label(master=rahmenCalendar, text="Choose the day \n of the game")
    chooseDateLable.pack(side="top", padx=5, pady=5)
    chooseDateLable.config(font=("TKCaptionFont", 12))

    matchdaysLabel = Label(master=frameLeft, text="Next Match Days:", bg="IndianRed1")
    matchdaysLabel.pack(side="top", padx=5, pady=5)
    matchdaysLabel.config(font=("TKCaptionFont", 12))

    # List for TeamHome
    teamsHome = getTeams()

    # List for TeamGuest
    teamsGuest = getTeams()

    '''Setup of the dropdown menus for the teams'''
    # Dropdowns Home Team
    firstTeamHome = teamsHome[0]
    clicked1 = StringVar(root)
    clicked1.set(firstTeamHome)
    dropDown1 = OptionMenu(rahmenTeamHome, clicked1, *teamsHome)
    dropDown1.pack(side="top", padx=5, pady=5)

    # Dropdowns Away Team
    firstTeamGuest = teamsGuest[0]
    clicked2 = StringVar(root)
    clicked2.set(firstTeamGuest)
    dropDown2 = OptionMenu(rahmenTeamGuest, clicked2, *teamsGuest)
    dropDown2.pack(side="top", padx=5, pady=5)


    # syncs clicks [ZWISCHENLÖSUNG]
    def sync1():
        """syncs clicks of clicked1"""
        return clicked1.get()

    def sync2():
        """syncs clicks of clicked2"""
        return clicked2.get()

    # Algorithm choice, import from package "Algorithms"
    package = Algorithms
    Algos = []
    for importer, modname, ispkg in pkgutil.walk_packages(path=package.__path__,
                                                          prefix=package.__name__ + '.',
                                                          onerror=lambda x: None):
        Algos.append(modname)

    selectedAlgo = list(Algos)[0]
    clicked3 = StringVar()
    clicked3.set(selectedAlgo)
    dropDownAlgo = OptionMenu(rahmenAlgo, clicked3, *Algos)
    dropDownAlgo.pack(side="top", padx=5)
    clicked3.set(selectedAlgo)

    def syncAlgo():
        """Imports chosen module for prediction"""
        module = importlib.import_module(clicked3.get())
        return module

    # Button to calculate odds,call function to predict the winner from the other script
    # When clicked, prediction of the chosen model is triggered
    buttonOdds = Button(master=rahmenMiddle, text="Calculate Odds", font=("Times", 17), bg="orange",
                        command=lambda: syncAlgo().predict(sync1(), sync2(), data))
    buttonOdds.pack(side="left", padx=20, pady=20)

    # Buttons to activate the search for the data
    buttonCrawler = Button(rahmenCrawler, text="Activate Crawler (all data since 2004)", padx=10, pady=5,
                           command=fetch_all_data)
    buttonCrawler.pack(side="top", padx=5)

    # Button to activate the other Crawler function (date-selected)
    buttonCrawler2 = Button(rahmenCrawler, text="Activate Crawler (selected data)", padx=30, pady=5,
                            command=lambda:
                            check_fetch(int(startYear.get()), int(startDay.get()),
                                       int(endYear.get()), int(endDay.get())))
    buttonCrawler2.pack(side="top", padx=5)

    # Boxes to choose Dates from
    chooseStartDay = Label(master=rahmenCrawler, text="Choose first Gameday of Year:", bg="lightyellow1")
    chooseStartDay.pack(side="top", padx=5, pady=5)
    chooseStartDay.config(font=("TKCaptionFont", 12))

    startDay = Spinbox(rahmenCrawler, from_=1, to=34)
    startDay.pack(side="top", padx=5, pady=5)
    startYear = Spinbox(rahmenCrawler, from_=2004, to=datetime.now().year)
    startYear.pack(side="top", padx=5, pady=5)

    def check_fetch(startYear,startDay,endYear,endDay):
        if startYear > endYear:
            showinfo("Activate Crawler", "Incorrect Input: The first Gameday must be before the last Gameday.")
        else:
            fetch_data(startYear, startDay, endYear, endDay)

    chooseEndDay = Label(master=rahmenCrawler, text="Choose last Gameday of Year:", bg="lightyellow1")
    chooseEndDay.pack(side="top", padx=5, pady=5)
    chooseEndDay.config(font=("TKCaptionFont", 12))
    endDay = Spinbox(rahmenCrawler, from_=1, to=34)
    endDay.pack(side="top", padx=5, pady=5)
    endYear = Spinbox(rahmenCrawler, from_=2004, to= datetime.now().year)
    endYear.pack(side="top", padx=5, pady=5)

    # Setting up a calendar to choose the game day


    currentYear = datetime.now().year
    currentDate = datetime.now().date()

    calendar = DateEntry(rahmenCalendar, width=12, year=currentYear, month=datetime.now().month,
                         day=datetime.now().day, background="darkblue", foreground="white", borderwidth=2)
    calendar.pack(side="top", padx=5, pady=5)

    # Display of Matchdays
    def displayMatchdays():
        """Displays all Matchdays of a Season"""
        Days = getMatchDays()
        for date in Days:
            dateLabel = Label(master=frameLeft, text=(str(date)), bg="red")
            dateLabel.pack(side="top", padx=5, pady=5)
            dateLabel.config(font=("TKCaptionFont", 8))

    displayMatchdays()
    nextLabel = Label(master=frameLeft, text=(str(next)), bg="IndianRed1")
    nextLabel.pack(side="bottom", padx=5, pady=5)
    nextLabel.config(font=("TKCaptionFont", 12))


    root.mainloop()

if __name__ == '__main__':
    main()
