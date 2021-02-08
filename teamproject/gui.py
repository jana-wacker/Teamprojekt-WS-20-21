"""This module imports the crawler and the algorithms and serves as an overall interface for the program."""
import tkinter as tk
from PIL import Image, ImageTk
import pandas as pd
from crawler import fetch_data, fetch_all_data, fetch_matchday
from Analysing import analysisoneclub
from tkcalendar import DateEntry, Calendar
from datetime import datetime
from tkinter.messagebox import showinfo
import csv
import pkgutil
import Algorithms
import tkinter.font as font
import os
# import io
import importlib


# import urllib.request

class gui:
    global framecolour
    global labelcolour
    global matchcolour
    global matchlabelcolour
    global menucolour
    global outputcolour
    global font
    global x_Picture
    global y_Picture
    global x_framesize
    global y_framesize

    def __init__(self, master):
        # fetch_all_data()
        # fetch_matchday()
        self.master = master

        # Basics for the window
        master.geometry("1120x600")
        master.title("Krake Paul: Bundesliga Predictions")
        self.font = "Bahnschrift"
        self.framecolour = "steel blue"
        self.lablecolour = "LightBlue1"
        self.matchcolour = self.framecolour  # "yellow green"
        self.matchlabelcolour = self.lablecolour  # "OliveDrab1"
        self.menucolour = "light blue"
        self.outputcolour = self.lablecolour
        self.x_framesize = 350
        self.y_framesize = 400

        # Variables for the size of the picture
        self.x_Picture = 1200

        # Setting background
        self.background = os.path.join(os.path.dirname(__file__), 'field.jpg')
        image1 = Image.open(self.background)
        image1_resized = image1.resize((1800, 1600), Image.ANTIALIAS)
        pic_ready = ImageTk.PhotoImage(image1_resized)

        self.lable_background = tk.Label(self.master, image=pic_ready)
        self.lable_background.image = pic_ready
        self.lable_background.place(x=0, y=0, relwidth=1, relheight=1)

        # import paul.png for calculate odds button
        self.paul_raw = os.path.join(os.path.dirname(__file__), 'paul.png')
        self.paul_open = Image.open(self.paul_raw)
        self.paul_resized = self.paul_open.resize((100, 80), Image.ANTIALIAS)
        self.paul = ImageTk.PhotoImage(self.paul_resized)

        # Label for the header
        self.header = tk.Label(self.master, text="Predict upcoming Bundesliga matches!",
                               justify=tk.CENTER,
                               bg=self.lablecolour)
        self.header.pack(side="top", padx=5)
        self.header.config(font=(self.font, 18))

        # Marking where the labels start, depending on the size of the main window
        self.begin_Labels = self.x_Picture / 100

        # Setting up all  frames to insert the labels and the buttons into

        self.frameMiddle = tk.Frame(master=self.master, bg=self.framecolour)
        self.frameMiddle.pack(side="top", padx=self.begin_Labels, pady=5)

        self.frameLeft = tk.Frame(master=self.master,
                                  width=self.x_framesize, height=self.y_framesize,
                                  bg=self.matchcolour)
        self.frameLeft.pack(side='left', expand='YES', padx=self.begin_Labels, pady=5)
        self.frameLeft.pack_propagate(0)

        self.frameOutput = tk.Frame(master=self.master,
                                    width=self.x_framesize, height=self.y_framesize,
                                    bg=self.outputcolour)
        self.frameOutput.pack(side='left', expand='YES', padx=self.begin_Labels, pady=5)
        self.frameOutput.pack_propagate(0)

        self.frameBelow = tk.Frame(master=self.master,
                                   width=self.x_framesize, height=self.y_framesize,
                                   bg=self.framecolour)
        self.frameBelow.pack(side='left', expand='YES', padx=self.begin_Labels, pady=5)
        self.frameBelow.pack_propagate(0)

        self.frameTeamHome = tk.Frame(master=self.frameMiddle, bg=self.framecolour)
        self.frameTeamHome.pack(side="left", padx=5, pady=5)

        self.frameTeamGuest = tk.Frame(master=self.frameMiddle, bg=self.framecolour)
        self.frameTeamGuest.pack(side="right", padx=5, pady=5)

        self.frameCalendar = tk.Frame(master=self.frameMiddle, bg=self.framecolour)
        self.frameCalendar.pack(side="top", padx=10, pady=0)

        self.frameAlgo = tk.Frame(master=self.frameBelow, bg=self.framecolour)
        self.frameAlgo.pack(side="top", padx=5, pady=5)

        self.frameCrawler = tk.Frame(master=self.frameBelow, bg=self.framecolour)
        self.frameCrawler.pack(side="top", padx=5, pady=5)

        # All labels
        self.settingsLable = tk.Label(self.frameCrawler, text="Activate the Crawler:",
                                      bg=self.lablecolour)
        self.settingsLable.pack(side="top", padx=5, pady=2)
        self.settingsLable.config(font=(self.font, 12))

        self.dropLable1 = tk.Label(master=self.frameTeamHome, text="Choose the Home Team:", bg=self.framecolour,
                                   fg="lightcyan1")
        self.dropLable1.pack(side="top", padx=5, pady=5)
        self.dropLable1.config(font=(self.font, 12))

        self.dropLable2 = tk.Label(master=self.frameTeamGuest, text="Choose the Away Team:", bg=self.framecolour,
                                   fg="lightcyan1")
        self.dropLable2.pack(side="top", padx=5, pady=5)
        self.dropLable2.config(font=(self.font, 12))

        self.oddsLable = tk.Label(master=self.frameMiddle, text="Predict!", bg=self.framecolour, font=self.font)
        self.oddsLable.pack(side="bottom", padx=1, pady=1)

        self.chooseCrawlerLabel = tk.Label(master=self.frameAlgo, text="Choose an Algorithm for calculation:",
                                           bg=self.lablecolour)
        self.chooseCrawlerLabel.pack(side="top", padx=5, pady=2)
        self.chooseCrawlerLabel.config(font=(self.font, 12))

        # Jana: May be renamed when it has a function
        self.chooseDateLable = tk.Label(master=self.frameCalendar, text="Today's day",
                                        bg=self.lablecolour)
        self.chooseDateLable.pack(side="top", padx=5, pady=5)
        self.chooseDateLable.config(font=(self.font, 12))

        self.matchdaysLabel = tk.Label(master=self.frameLeft, text="Next Match Days:",
                                       bg=self.matchlabelcolour)
        self.matchdaysLabel.pack(side="top", padx=5, pady=5)
        self.matchdaysLabel.config(font=(self.font, 12))

        self.outputLabel = tk.Label(master=self.frameOutput,
                                    text="Prediction results appear here",
                                    bg=self.outputcolour)
        self.outputLabel.pack(side="top", padx=5, pady=5)
        self.outputLabel.config(font=(self.font, 12))

        # List for Teams
        teams = self.getTeams()

        # Dropdowns Home Team
        self.clicked1 = tk.StringVar()
        self.clicked1.set(teams[0])
        self.dropDown1 = tk.OptionMenu(self.frameTeamHome, self.clicked1, *teams)
        self.dropDown1.config(bg=self.menucolour, font=(self.font, 8))
        self.dropDown1["menu"].config(bg=self.menucolour)
        self.dropDown1.pack(side="top", padx=5, pady=5)

        # Dropdowns Away Team
        self.clicked2 = tk.StringVar(self.frameTeamGuest)
        self.clicked2.set(teams[0])
        self.dropDown2 = tk.OptionMenu(self.frameTeamGuest, self.clicked2, *teams)
        self.dropDown2.config(bg=self.menucolour, font=(self.font, 8))
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
        self.dropDownAlgo = tk.OptionMenu(self.frameAlgo, self.clicked3, *Algos)
        self.dropDownAlgo.config(bg=self.menucolour, font=(self.font, 8))
        self.dropDownAlgo["menu"].config(bg=self.menucolour)
        self.dropDownAlgo.pack(side="top", padx=5, pady=2)
        self.clicked3.set(self.selectedAlgo)

        # Button to calculate odds,call function to predict the winner from the other script
        # When clicked, prediction of the chosen model is triggered
        self.buttonOdds = tk.Button(master=self.frameMiddle, image=self.paul,
                                    borderwidth=2, bg=self.framecolour,
                                    command=lambda: self.wrapAlgo())
        # command=lambda: self.syncAlgo().predict(
        #    self.clicked1.get(), self.clicked2.get(), self.data))
        self.buttonOdds.pack(side="bottom", padx=5, pady=5)

        # Buttons to activate the search for the data
        self.buttonCrawler = tk.Button(master= self.frameCrawler, text="Activate Crawler (all data since 2004)",
                                       padx=10, pady=5, bg=self.menucolour, font=(self.font, 8),
                                       command=lambda:
                                       self.outputLabel.config(text=self.wrapCrawler()))
        self.buttonCrawler.pack(side="top", padx=5, pady=1)

        # Button to activate the other Crawler function (date-selected)
        self.buttonCrawler2 = tk.Button(master=self.frameCrawler, text="Activate Crawler (selected data)",
                                        padx=30, pady=5, bg=self.menucolour, font=(self.font, 8),
                                        command=lambda:
                                        self.outputLabel.config(text=self.check_fetch(int(self.startYear.get()),
                                                                                      int(self.startDay.get()),
                                                                                      int(self.endYear.get()),
                                                                                      int(self.endDay.get()))))
        self.buttonCrawler2.pack(side="top", padx=5, pady=2)

        # Buttons for statistics about the teams
        self.buttonInfo1 = tk.Button(master=self.frameTeamHome, bitmap="info",
                                     padx=0, pady=0, bg=self.lablecolour,
                                     command=lambda: analysisoneclub(self.clicked1.get()))
        self.buttonInfo1.pack(side="bottom")

        self.buttonInfo1 = tk.Button(master=self.frameTeamGuest, bitmap="info",
                                     padx=0, pady=0, bg=self.lablecolour,
                                     command=lambda: analysisoneclub(self.clicked2.get()))
        self.buttonInfo1.pack(side="bottom")

        # Boxes to choose Dates from
        self.chooseStartDay = tk.Label(master=self.frameCrawler, text="Choose first Gameday of Year:",
                                       bg=self.lablecolour, font=(self.font, 8))
        self.chooseStartDay.pack(side="top", padx=5, pady=2)
        self.chooseStartDay.config(font=(self.font, 12))

        self.startDay = tk.Spinbox(self.frameCrawler, from_=1, to=34)
        self.startDay.pack(side="top", padx=5, pady=2)
        self.startYear = tk.Spinbox(self.frameCrawler, from_=2004, to=datetime.now().year)
        self.startYear.pack(side="top", padx=5, pady=2)

        self.chooseEndDay = tk.Label(master=self.frameCrawler, text="Choose last Gameday of Year:",
                                     bg=self.lablecolour, font=(self.font, 8))
        self.chooseEndDay.pack(side="top", padx=5, pady=2)
        self.chooseEndDay.config(font=(self.font, 12))
        self.endDay = tk.Spinbox(self.frameCrawler, from_=1, to=34)
        self.endDay.pack(side="top", padx=5, pady=2)
        self.endYear = tk.Spinbox(self.frameCrawler, from_=2004, to=datetime.now().year)
        self.endYear.pack(side="top", padx=5, pady=2)

        # Setting up a calendar
        self.currentYear = datetime.now().year
        self.currentDate = datetime.now().date()

        self.calendar = DateEntry(self.frameCalendar, width=12, year=self.currentYear, month=datetime.now().month,
                                  day=datetime.now().day, background=self.menucolour,
                                  foreground="white", borderwidth=2, font=(self.font, 8))
        self.calendar.pack(side="top", padx=5, pady=5)

        self.displayMatchdays()
        self.nextLabel = tk.Label(master=self.frameLeft, text=(str(self.next)), bg=self.matchlabelcolour)
        self.nextLabel.pack(side="bottom", padx=5, pady=5)
        self.nextLabel.config(font=(self.font, 12))


    def check_fetch(self, startYear, startDay, endYear, endDay):
        """Checks whether input was correct and if so, fetch chosen data"""
        if startYear > endYear or startDay > endDay:
            showinfo("Activate Crawler", "Incorrect Input: The first Gameday must be before the last Gameday.")
        else:
            fetch_data(startYear, startDay, endYear, endDay)
            self.refreshTeams()
            return "Selected data fetched."

    def displayMatchdays(self):
        """Displays all matchdays of a season"""
        self.divisionLabel = tk.Label(master=self.frameLeft,
                                      text=('Date and Time       Home Team       Away Team'),
                                      bg=self.matchcolour, fg="lightcyan1", font=(self.font, 8))
        self.divisionLabel.pack(side="top", padx=2, pady=2)
        Days = self.getMatchDays()
        for date in Days:
            self.dateLabel = tk.Label(master=self.frameLeft, text=(str(date)), bg=self.matchcolour)
            self.dateLabel.pack(side="top", padx=5, pady=5)
            self.dateLabel.config(font=(self.font, 8))

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
                self.match_name = ((str(row['Matchday'].replace("T", " at "))) +
                                   ': ' + (str(row['Team1'])) +
                                   ' vs. ' + (str(row['Team2'])))
                self.matches.append(self.match_name)
                break

            # 'next' is upcoming match day
            global next
            self.next = self.gameday[0]

            for row in game_dates:
                if (row['MatchNr'] == self.next):
                    self.match_name = ((str(row['Matchday'].replace("T", " at "))) +
                                       ': ' + (str(row['Team1'])) +
                                       ' vs. ' + (str(row['Team2'])))
                    self.matches.append(self.match_name)
        return self.matches

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

    def refreshTeams(self):
        """Refreshes Teams with getTeams()"""
        self.dropDown1['menu'].delete(0, 'end')
        self.dropDown2['menu'].delete(0, 'end')
        teams = self.getTeams()
        for team in teams:
            self.dropDown1['menu'].add_command(label=team, command=tk._setit(self.clicked1, team))
            self.dropDown2['menu'].add_command(label=team, command=tk._setit(self.clicked2, team))

    def syncAlgo(self):
        """Imports chosen module for prediction"""
        global data
        alldata = os.path.join(os.path.dirname(__file__), 'Crawler.csv')
        self.data = pd.read_csv(alldata)
        module = importlib.import_module(self.clicked3.get())
        return module

    def wrapAlgo(self):
        """Wraps choice of algorithm."""
        output = self.syncAlgo().predict(self.clicked1.get(), self.clicked2.get(), self.data)
        self.outputLabel.config(text=output)

    def wrapCrawler(self):
        """Wraps Crawler for all data."""
        fetch_all_data()
        self.refreshTeams()
        return 'All data fetched.'


def main():
    """Creates main window."""
    root = tk.Tk()
    gui(root)
    root.mainloop()


if __name__ == '__main__':
    main()

###################################################################################################
# Jana: I might need that for another idea :)
# url = "https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/VfB_Stuttgart_1893_Logo.svg/921px-VfB_Stuttgart_1893_Logo.svg.png"
# image_bytes = urllib.request.urlopen(url).read()
# data_stream = io.BytesIO(image_bytes)
# pil_image = Image.open(data_stream)
# pil_image = pil_image.resize((100, 108), Image.ANTIALIAS)
# self.tk_image = ImageTk.PhotoImage(pil_image)
