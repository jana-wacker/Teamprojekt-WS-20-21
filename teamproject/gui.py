"""This module imports the crawler and the algorithms and serves as an overall interface for the program."""
import tkinter as tk
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


class gui:
    global framecolour
    global labelcolour
    global matchcolour
    global matchlabelcolour
    global menucolour
    global font
    global x_Picture
    global y_Picture

    def __init__(self, master):
        fetch_all_data()
        fetch_matchday()
        self.master = master

        # Basics for the window
        master.geometry("1200x600")
        master.title("Krake Paul: Bundesliga Predictions")
        self.font = "TKCaptionFont"
        self.framecolour = "steel blue"
        self.lablecolour = "LightBlue1"
        self.matchcolour = "yellow green"
        self.matchlabelcolour = "OliveDrab1"
        self.menucolour = "light blue"

        # Variables for the size of the picture
        self.x_Picture = 1200
        self.y_Picture = 600

        # Setting the background
        self.background = os.path.join(os.path.dirname(__file__), 'field.jpg')
        image1 = Image.open(self.background)
        image1_resized = image1.resize((1800, 1600), Image.ANTIALIAS)
        pic_ready = ImageTk.PhotoImage(image1_resized)

        self.lable_background = tk.Label(self.master, image=pic_ready)
        self.lable_background.image = pic_ready
        self.lable_background.place(x=0, y=0, relwidth=1, relheight=1)

        # import paul.png for calculate odds button
        self.paul_raw = os.path.join(os.path.dirname(__file__), 'paul.png')
        self.paul1 = Image.open(self.paul_raw)
        self.paul2 = self.paul1.resize((100, 80), Image.ANTIALIAS)
        self.paul = ImageTk.PhotoImage(self.paul2)

        # Lable for the header
        self.header = tk.Label(self.master, text="Predict upcoming Bundesliga matches!",
                               justify=tk.CENTER,
                               bg=self.lablecolour)
        self.header.pack(side="top", padx=5)
        self.header.config(font=(self.font, 20))

        # Marking where the lables start, depending on the size of the main window
        self.begin_Labels = self.x_Picture / 100
        self.end_Labels = self.y_Picture / 10

        # Setting up all the frames to insert the labels and the buttons into
        self.frameLeft = tk.Frame(master=self.master, bg=self.matchcolour)
        self.frameLeft.pack(side="left", padx=self.begin_Labels, pady=5)

        self.rahmenMiddle = tk.Frame(master=self.master, bg=self.framecolour)
        self.rahmenMiddle.pack(side="top", padx=self.begin_Labels, pady=10)

        self.rahmenBelow = tk.Frame(master=self.master, bg=self.framecolour)
        self.rahmenBelow.pack(side="bottom", padx=self.begin_Labels, pady=10)

        self.rahmenTeamHome = tk.Frame(master=self.rahmenMiddle, bg=self.framecolour)
        self.rahmenTeamHome.pack(side="left", padx=5, pady=5)

        self.rahmenTeamGuest = tk.Frame(master=self.rahmenMiddle, bg=self.framecolour)
        self.rahmenTeamGuest.pack(side="right", padx=5, pady=5)

        self.rahmenCalendar = tk.Frame(master=self.rahmenMiddle, bg=self.framecolour)
        self.rahmenCalendar.pack(side="top", padx=10, pady=0)

        self.rahmenAlgo = tk.Frame(master=self.rahmenBelow, bg=self.framecolour)
        self.rahmenAlgo.pack(side="left", padx=5, pady=5)

        self.rahmenCrawler = tk.Frame(master=self.rahmenBelow, bg=self.framecolour)
        self.rahmenCrawler.pack(side="left", padx=5, pady=5)

        # Jana: Maybe I need that later for the output
        #self.frameOutput = tk.Frame(master=self.master, bg="red")
        #self.frameOutput.pack(side="top", padx=5, pady=5)

        # All of the labels
        self.settingsLable = tk.Label(self.rahmenCrawler, text="Activate the AI or Start the Crawler here:",
                                      bg=self.lablecolour)
        self.settingsLable.pack(side="top", padx=5)
        self.settingsLable.config(font=(self.font, 12))

        self.dropLable1 = tk.Label(master=self.rahmenTeamHome, text="Choose the Home Team:", bg=self.framecolour,
                                   fg="lightcyan1")
        self.dropLable1.pack(side="top", padx=5, pady=5)
        self.dropLable1.config(font=(self.font, 12))

        self.dropLable2 = tk.Label(master=self.rahmenTeamGuest, text="Choose the Away Team:", bg=self.framecolour,
                                   fg="lightcyan1")
        self.dropLable2.pack(side="top", padx=5, pady=5)
        self.dropLable2.config(font=(self.font, 12))

        self.oddsLable = tk.Label(master=self.rahmenMiddle, text="Calculate Odds!", bg=self.framecolour, font=self.font)
        self.oddsLable.pack(side="bottom", padx=1, pady=1)

        self.chooseCrawlerLabel = tk.Label(master=self.rahmenAlgo, text="Choose an Algorithm for calculation:",
                                           bg=self.lablecolour)
        self.chooseCrawlerLabel.pack(side="top", padx=5, pady=5)
        self.chooseCrawlerLabel.config(font=(self.font, 12))

        # Jana: May be renamed when it has a function
        self.chooseDateLable = tk.Label(master=self.rahmenCalendar, text="Today's day",
                                        bg=self.lablecolour)
        self.chooseDateLable.pack(side="top", padx=5, pady=5)
        self.chooseDateLable.config(font=(self.font, 12))

        self.matchdaysLabel = tk.Label(master=self.frameLeft, text="Next Match Days:", bg=self.matchlabelcolour)
        self.matchdaysLabel.pack(side="top", padx=5, pady=5)
        self.matchdaysLabel.config(font=(self.font, 12))

        # Jana: Maybe I need that later for the output
        #self.outputLabel = tk.Label(master=self.frameOutput, text="", font=self.font)
        #self.outputLabel.pack(side="top", padx=5, pady=5)

        # List for Teams
        teams = self.getTeams()

        # Dropdowns Home Team
        self.clicked1 = tk.StringVar()
        self.clicked1.set(teams[0])
        self.dropDown1 = tk.OptionMenu(self.rahmenTeamHome, self.clicked1, *teams)
        self.dropDown1.config(bg=self.menucolour)
        self.dropDown1["menu"].config(bg=self.menucolour)
        self.dropDown1.pack(side="top", padx=5, pady=5)

        # Dropdowns Away Team
        self.clicked2 = tk.StringVar(self.rahmenTeamGuest)
        self.clicked2.set(teams[0])
        self.dropDown2 = tk.OptionMenu(self.rahmenTeamGuest, self.clicked2, *teams)
        self.dropDown2.config(bg=self.menucolour)
        self.dropDown2["menu"].config(bg=self.menucolour)
        self.dropDown2.pack(side="top", padx=5, pady=5)

        # Algorithm choice, import from package "Algorithms"
        package = Algorithms
        Algos = []
        for importer, modname, ispkg in pkgutil.walk_packages(path=package.__path__,
                                                              prefix=package.__name__ + '.',
                                                              onerror=lambda x: None):
            Algos.append(modname)

        self.selectedAlgo = list(Algos)[0]
        self.clicked3 = tk.StringVar()
        self.dropDownAlgo = tk.OptionMenu(self.rahmenAlgo, self.clicked3, *Algos)
        self.dropDownAlgo.config(bg=self.menucolour)
        self.dropDownAlgo["menu"].config(bg=self.menucolour)
        self.dropDownAlgo.pack(side="top", padx=5)
        self.clicked3.set(self.selectedAlgo)

        # Button to calculate odds,call function to predict the winner from the other script
        # When clicked, prediction of the chosen model is triggered
        self.buttonOdds = tk.Button(master=self.rahmenMiddle, image=self.paul,
                          borderwidth=0, bg=self.framecolour,
                                    command=lambda: self.syncAlgo().predict(
                                        self.clicked1.get(), self.clicked2.get(), self.data))
        self.buttonOdds.pack(side="bottom", padx=5, pady=5)

        # Buttons to activate the search for the data
        self.buttonCrawler = tk.Button(self.rahmenCrawler, text="Activate Crawler (all data since 2004)", padx=10,
                                       pady=5, bg=self.menucolour,
                                       command=fetch_all_data)
        self.buttonCrawler.pack(side="top", padx=5)

        # Button to activate the other Crawler function (date-selected)
        self.buttonCrawler2 = tk.Button(self.rahmenCrawler, text="Activate Crawler (selected data)", padx=30, pady=5,
                                        bg=self.menucolour,
                                        command=lambda:
                                        self.check_fetch(int(self.startYear.get()), int(self.startDay.get()),
                                                         int(self.endYear.get()), int(self.endDay.get())))
        self.buttonCrawler2.pack(side="top", padx=5)

        # Boxes to choose Dates from
        self.chooseStartDay = tk.Label(master=self.rahmenCrawler, text="Choose first Gameday of Year:",
                                       bg=self.lablecolour)
        self.chooseStartDay.pack(side="top", padx=5, pady=5)
        self.chooseStartDay.config(font=(self.font, 12))

        self.startDay = tk.Spinbox(self.rahmenCrawler, from_=1, to=34)
        self.startDay.pack(side="top", padx=5, pady=5)
        self.startYear = tk.Spinbox(self.rahmenCrawler, from_=2004, to=datetime.now().year)
        self.startYear.pack(side="top", padx=5, pady=5)

        self.chooseEndDay = tk.Label(master=self.rahmenCrawler, text="Choose last Gameday of Year:",
                                     bg=self.lablecolour)
        self.chooseEndDay.pack(side="top", padx=5, pady=5)
        self.chooseEndDay.config(font=(self.font, 12))
        self.endDay = tk.Spinbox(self.rahmenCrawler, from_=1, to=34)
        self.endDay.pack(side="top", padx=5, pady=5)
        self.endYear = tk.Spinbox(self.rahmenCrawler, from_=2004, to=datetime.now().year)
        self.endYear.pack(side="top", padx=5, pady=5)

        # Setting up a calendar to choose the game day
        self.currentYear = datetime.now().year
        self.currentDate = datetime.now().date()

        self.calendar = DateEntry(self.rahmenCalendar, width=12, year=self.currentYear, month=datetime.now().month,
                                  day=datetime.now().day, background=self.menucolour, foreground="white", borderwidth=2)
        self.calendar.pack(side="top", padx=5, pady=5)

        self.displayMatchdays()
        self.nextLabel = tk.Label(master=self.frameLeft, text=(str(self.next)), bg=self.matchlabelcolour)
        self.nextLabel.pack(side="bottom", padx=5, pady=5)
        self.nextLabel.config(font=(self.font, 12))

    def syncAlgo(self):
        """Wrapper: Imports chosen module for prediction"""
        global data
        alldata = os.path.join(os.path.dirname(__file__), 'Crawler.csv')
        self.data = pd.read_csv(alldata)
        module = importlib.import_module(self.clicked3.get())
        return module

    def check_fetch(self, startYear, startDay, endYear, endDay):
        """Checks whether input was correct and if so, fetch chosen data"""
        if startYear > endYear or startDay > endDay:
            showinfo("Activate Crawler", "Incorrect Input: The first Gameday must be before the last Gameday.")
        else:
            fetch_data(startYear, startDay, endYear, endDay)

    def displayMatchdays(self):
        """Displays all matchdays of a season"""
        Days = self.getMatchDays()
        for date in Days:
            self.dateLabel = tk.Label(master=self.frameLeft, text=(str(date)), bg=self.matchcolour)
            self.dateLabel.pack(side="top", padx=5, pady=5)
            self.dateLabel.config(font=(self.font, 8))

    def getTeams(self):
        """
        Creates a dictionary with all teams, using the Crawler.csv as data basis
        :returns: all team-names(dictionary)
        """
        alldata = os.path.join(os.path.dirname(__file__), 'Crawler.csv')
        with open(alldata, newline='', encoding="utf8") as all_data_raw:
            Teams = []
            all_data = csv.DictReader(all_data_raw, delimiter=',')
            for row in all_data:
                if row['Team1'] not in Teams:
                    Teams.append(row['Team1'])
        Teams.sort()
        return Teams

    def getMatchDays(self):
        """
        Creates a dictionary with upcoming match day, using the Matchdays.csv as data basis
        :returns: upcoming match days (dictionary)
        """
        gamedates = os.path.join(os.path.dirname(__file__), 'Matchdays.csv')
        with open(gamedates, newline='', encoding="utf8") as dates_raw:
            game_dates = csv.DictReader(dates_raw, delimiter=',')
            self.matches = []
            self.gameday = []

            # getting the next match day and adding it to 'matches'
            for row in game_dates:
                self.gameday.append(row['MatchNr'])
                self.match_name = ((str(row['Matchday'])) +
                                   ': ' + (str(row['Team1'])) +
                                   ' vs. ' + (str(row['Team2'])))
                self.matches.append(self.match_name)
                break

            # 'next' is upcoming match day
            global next
            self.next = self.gameday[0]

            for row in game_dates:
                if (row['MatchNr'] == self.next):
                    self.match_name = ((str(row['Matchday'])) +
                                       ': ' + (str(row['Team1'])) +
                                       ' vs. ' + (str(row['Team2'])))
                    self.matches.append(self.match_name)
        return self.matches


def main():
    """Creates main window."""
    root = tk.Tk()
    gui(root)
    root.mainloop()

if __name__ == '__main__':
    main()