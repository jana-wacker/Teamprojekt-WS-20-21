from tkinter import *
from PIL import Image, ImageTk
import pandas as pd
from crawler import fetch_data, fetch_all_data
from tkcalendar import DateEntry, Calendar
from datetime import datetime
import csv
import pkgutil
import Algorithms
import tkinter.font as font
import os
import importlib

# Jana: This is not fixed yet, we need to fetch the data first when the csv is emtpy.
# Otherwise the program won't open.
#fetch_all_data()

# Needed by the Vorhersage_Algo
alldata = os.path.join(os.path.dirname(__file__), 'Crawler.csv')
data = pd.read_csv(alldata)


def getTeams():
    with open(alldata, newline='', encoding="utf8") as all_data_raw:
        Teams = []
        all_data = csv.DictReader(all_data_raw, delimiter=',')
        for row in all_data:
            if row['Team1'] not in Teams:
                Teams.append(row['Team1'])
    Teams.sort()
    return Teams



def main():
    root = Tk()
    """
    Creates and shows the main window  .
    """
    # Add code here to create and initialize window.

    # For demo purposes, this is how you could access methods from other
    # modules:
    # matchNumber = Vorhersage_Algo.matchNumber()
    # model = ExperienceAlwaysWins(data)
    # winner = model.predict_winner('T�bingen', 'Leverkusen')
    # print(winner)

    # Basics für das Window
    root.geometry("800x600")
    root.title("Bundesliga Vorhersagen")

    # Variables for the size of the picture
    x_Picture = 800
    y_Picture = 600

    '''Trying to set the background picture '''
    background = os.path.join(os.path.dirname(__file__), 'field.jpg')
    image1 = Image.open(background)
    image1_resized = image1.resize((x_Picture, y_Picture), Image.ANTIALIAS)
    pic_ready = ImageTk.PhotoImage(image1_resized)

    lable_background = Label(root, image=pic_ready)
    lable_background.image = pic_ready
    lable_background.place(x=0, y=0, relwidth=1, relheight=1)

    #lable_background.config(x_Picture, y_Picture)

    # Lable for the header
    myLable = Label(root, text="Erstelle hier Vorhersagen zu anstehenden Bundesliga Spielen!", justify=CENTER,
                    bg="light green")
    myLable.pack(side="top", padx=10)
    myLable.config(font=("Times", 20))

    # Marking where the lables start, depending on the size of the main window
    begin_Labels = x_Picture / 10

    '''Setting up all the frames to insert the labels and the buttons into '''
    rahmenBelow = Frame(master=root, bg="lightblue1")
    rahmenBelow.pack(side="bottom", padx=begin_Labels, pady=10)

    rahmenMiddle = Frame(master=root, bg="cadetblue1")
    rahmenMiddle.pack(side="left", padx=begin_Labels, pady=5)

    rahmenTeamHome = Frame(master=rahmenMiddle, bg="cadetblue3")
    rahmenTeamHome.pack(side="left", padx=5, pady=5)

    rahmenTeamGuest = Frame(master=rahmenMiddle, bg="cadetblue3")
    rahmenTeamGuest.pack(side="right", padx=5, pady=5)

    rahmenCalendar = Frame(master=rahmenMiddle, bg="cadetblue4")
    rahmenCalendar.pack(side="top", padx=15, pady=15)

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

    dropLable2 = Label(master=rahmenTeamGuest, text="Choose the Guest Team:", bg="lightcyan1", fg="royalblue1")
    dropLable2.pack(side="top", padx=5, pady=5)
    dropLable2.config(font=("TKCaptionFont", 12))

    chooseCrawlerLabel = Label(master=rahmenAlgo, text="Choose an Algorithm for calculation:")
    chooseCrawlerLabel.pack(side="top", padx=5, pady=5)
    chooseCrawlerLabel.config(font=("TKCaptionFont", 12))

    # List for TeamHome
    teamsHome = getTeams()

    # List for TeamGuest
    teamsGuest = getTeams()

    '''Setup of the dropdown menus for the teams'''
    # Dropdowns f�r Mannschaften1
    firstTeamHome = teamsHome[0]
    clicked1 = StringVar(root)
    clicked1.set(firstTeamHome)
    dropDown1 = OptionMenu(rahmenTeamHome, clicked1, *teamsHome)
    dropDown1.pack(side="top", padx=5, pady=5)

    # Dropdowns f�r Mannschaften2
    firstTeamGuest = teamsGuest[0]
    clicked2 = StringVar(root)
    clicked2.set(firstTeamGuest)
    dropDown2 = OptionMenu(rahmenTeamGuest, clicked2, *teamsGuest)
    dropDown2.pack(side="top", padx=5, pady=5)


    # syncs clicks [ZWISCHENLÖSUNG]
    def sync1():
        return clicked1.get()

    def sync2():
        return clicked2.get()

    # [ZWISCHENLÖSUNG]
    # The choice of an algorithm
    # Import from package "Algorithms"
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

    # Imports chosen module for prediction
    def syncAlgo():
        module = importlib.import_module(clicked3.get())
        return module

    # Button to calculate odds,call function to predict the winner from the other script
    '''The button is all the way up there because otherwise the frames are arranged weirdly... '''
    # When clicked, prediction of the chosen model is triggered
    buttonOdds = Button(master=rahmenMiddle, text="Calculate Odds", font=("Times", 17), bg="orange",
                        command=lambda: syncAlgo().predict(sync1(), sync2(), data))
    buttonOdds.pack(side="left", padx=40, pady=40)

    # Buttons to activate the search for the data
    buttonCrawler = Button(rahmenCrawler, text="Activate Crawler (all data since 2004)", padx=10, pady=5,
                           command=fetch_all_data)
    buttonCrawler.pack(side="top", padx=5)

    """Jana: Do we need a button for the AI? I mean, the algorithm is started via the
    Calculate-Odds-Button. So I replaced that by a button for the data selection of the crawler.
    But it looks ugly, so I leave that to Hanni :)."""
    # Button to activate the other Crawler function (date-selected)
    buttonCrawler2 = Button(rahmenCrawler, text="Activate Crawler (selected data)", padx=30, pady=5,
                            command=lambda:
                            fetch_data(int(startYear.get()), int(startDay.get()),
                                       int(endYear.get()), int(endDay.get())))
    buttonCrawler2.pack(side="top", padx=5)

    # Boxes to choose Dates from
    chooseStartDay = Label(master=rahmenCrawler, text="Choose first Gameday of Year:", bg="lightyellow1")
    chooseStartDay.pack(side="top", padx=5, pady=5)
    chooseStartDay.config(font=("TKCaptionFont", 12))

    startDay = Spinbox(rahmenCrawler, from_=1, to=34)
    startDay.pack(side="top", padx=5, pady=5)
    startYear = Spinbox(rahmenCrawler, from_=2004, to= datetime.now().year)
    startYear.pack(side="top", padx=5, pady=5)

    chooseEndDay = Label(master=rahmenCrawler, text="Choose last Gameday of Year:", bg="lightyellow1")
    chooseEndDay.pack(side="top", padx=5, pady=5)
    chooseEndDay.config(font=("TKCaptionFont", 12))
    endDay = Spinbox(rahmenCrawler, from_=1, to=34)
    endDay.pack(side="top", padx=5, pady=5)
    endYear = Spinbox(rahmenCrawler, from_=2004, to= datetime.now().year)
    endYear.pack(side="top", padx=5, pady=5)

    # Setting up a calendar to choose the game day

    chooseDateLable = Label(master=rahmenCalendar, text="Choose the day \n of the game")
    chooseDateLable.pack(side="top", padx=5, pady=5)
    chooseDateLable.config(font=("TKCaptionFont", 12))

    calendar = DateEntry(rahmenCalendar, width=12, year=2020, month=11, day=26,
                         background="darkblue", foreground="white", borderwidth=2)
    calendar.pack(side="top", padx=5, pady=5)

    # Display of Matchdays
    currentYear = datetime.now().year
    currentDate = datetime.now().date()



    root.mainloop()

if __name__ == '__main__':
    main()
