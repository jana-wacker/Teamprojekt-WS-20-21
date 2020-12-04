"""
Jana: Before anything works, the button "Activate Crawler" must be pressed. This button invokes the crawler (obviously)
and creates the .csv data needed. Otherwise, fetch_all_data would be called a few times which
extremely slows down the app. However, I have not figured out yet, how we can pass on the selected teams to the
algorithm. This is something I postponed since I do not know the newest version of the algorithm.
@Yupei As soon as you committed your version on GitHub, I (or someone else) can continue to integrate it into the GUI.
And please save your prediction-modules in the Algorithms-package. Makes it easier to retrieve the different algorithms.
"""
from tkinter import *
from PIL import Image, ImageTk
from teamproject.crawler import fetch_all_data
from teamproject.Algorithms.Vorhersage_Algo import algoPrediction
from tkcalendar import DateEntry
import csv
import pkgutil
import teamproject.Algorithms
import tkinter.font as font

root = Tk()


def getTeams():

    '''
    Gets Teams based on the data of the crawler
    '''

    with open('Alldata.csv', newline='') as all_data_raw:
        Teams = []
        all_data = csv.DictReader(all_data_raw, delimiter=',')
        for row in all_data:
            if row['Team1'] not in Teams:
                Teams.append(row['Team1'])
    return Teams


def main():
    """
    Creates and shows the main window with all the buttons and labels .
    """
    # Add code here to create and initialize window.

    # For demo purposes, this is how you could access methods from other
    # modules:
    #matchNumber = Vorhersage_Algo.matchNumber()
    #model = ExperienceAlwaysWins(data)
    #winner = model.predict_winner('Tübingen', 'Leverkusen')
    #print(winner)


    # Basics für das Window
    root.geometry("900x600")
    root.title("Bundesliga Vorhersagen")

    '''Trying to set the background picture '''
    image1 = Image.open("field.jpg")
    image1_resized = image1.resize((900, 600), Image.ANTIALIAS)
    pic_ready = ImageTk.PhotoImage(image1_resized)

    lable_background = Label(image=pic_ready)
    lable_background.image = pic_ready
    lable_background.place(x=0, y=0)

    lable_background.config(width=900, height=600)

    # Setting a lable style for all the descriptions
    myFont = font.Font(family="Helviva", size=14)

    # Lable for the header
    myLable = Label(root, text="Erstelle hier Vorhersagen zu anstehenden Bundesliga Spielen!")
    myLable.grid(row=0, column=1, columnspan=6, )
    myLable.config(font=("Times", 17))

    # Empty Lines - don't know how else to do it
    myEmptyLable = Label(root)
    myEmptyLable.grid(row=5, column=1, columnspan=6)
    myEmptyLable = Label(root)
    myEmptyLable.grid(row=1, column=1, columnspan=6)
    myEmptyLable = Label(root)
    myEmptyLable.grid(row=8, column=1, columnspan=6)
    myEmptyLable2 = Label(root)
    myEmptyLable2.grid(row=4, column=1, columnspan=3)
    myEmptyLable2 = Label(root)
    myEmptyLable2.grid(row=11, column=1, columnspan=6)

    # All of the labels
    settingsLable = Label(root, text="Activate the AI or Start the Crawler here:", bg="silver")
    settingsLable.grid(row=9, column=2, columnspan=6)
    settingsLable.config(font=("TKCaptionFont", 12))

    chooseDateLable = Label(root, text="Choose the day \n of the game")
    chooseDateLable.grid(row=5, column=5)
    chooseDateLable.config(font=("TKCaptionFont", 12))

    dropLable1 = Label(root, text="Choose the Home Team:", bg="mediumblue", fg="yellow")
    dropLable1.grid(row=5, column=1)
    dropLable1.config(font=("TKCaptionFont", 12))

    dropLable2 = Label(root, text="Choose the Guest Team:", bg="yellow", fg="mediumblue")
    dropLable2.grid(row=5, column=3)
    dropLable2.config(font=("TKCaptionFont", 12))

    chooseCrawlerLabel = Label(root, text="Choose an Algorithm for calculation:")
    chooseCrawlerLabel.grid(row=12, column=1)
    chooseCrawlerLabel.config(font=("TKCaptionFont", 12))

    # Bsp List for TeamHome
    teamsHome = getTeams()

    # Bsp List for TeamGuest
    teamsGuest = getTeams()

    '''Setup of the dropdown menus for the teams 
    clicked1 /2 : These is the Team the user selected, at the beginning it is set the FIRST team in the list 
    # Jana: We don't need this method anymore since the created lists do not have keys
    The method *teamsHome.keys() puts all of the keys, from the teamsHome List into the dropdown menu. 

    '''
    # Dropdowns für Mannschaften1
    firstTeamHome = list(teamsHome)[0]
    clicked1 = StringVar(root)
    clicked1.set(firstTeamHome)
    dropDown1 = OptionMenu(root, clicked1, *teamsHome)
    # This is for the Algo section, to know which team is selected
    homeTeam = clicked1.get()
    dropDown1.grid(row=6, column=1)

    # Dropdowns für Mannschaften2
    firstTeamGuest = list(teamsGuest)[0]
    clicked2 = StringVar(root)
    clicked2.set(firstTeamGuest)
    dropDown2 = OptionMenu(root, clicked2, *teamsGuest)
    # This is for the Algo section, to know which team is selected
    guestTeam = clicked2.get()
    dropDown2.grid(row=6, column=3)

    # The choice of an algorithm
    # Import from package "Algorithms"
    """Jana: Don't know why there's an error"""
    package = teamproject.Algorithms
    Algos = []
    for importer, modname, ispkg in pkgutil.walk_packages(path=package.__path__,
                                                          prefix=package.__name__ + '.',
                                                          onerror=lambda x: None):
        Algos.append(modname)

    firstAlgo = list(Algos)[0]
    clicked3 = StringVar()
    clicked3.set(firstAlgo)
    dropDownAlgo = OptionMenu(root, clicked3, *Algos)
    dropDownAlgo.grid(row=13, column=1)

    # Buttons to activate the search for the data
    buttonCrawler = Button(root, text="Activate Crawler", padx=10, pady=5, command = fetch_all_data)
    buttonCrawler.grid(row=15, column=3)

    # Button to activate the AI Process
    buttonAlgo = Button(root, text="Activate the AI", padx=10, pady=5)
    buttonAlgo.grid(row=15, column=4)

    # Button to calculate odds,call function to predict the winner from the Vorhersage_Algo script
    """Does not work yet"""
    # Button to calculate odds,call function to predict the winner from the other script
    buttonOdds = Button(root, text="Calculate Odds", padx=18, pady=15, font=myFont, bg="orange",
                        highlightthickness=2, highlightbackground="#111", command = algoPrediction)
    buttonOdds.grid(row=7, column=2)

    # Setting up a calender to choose the game day
    calendar = DateEntry(root, width=12, year=2020, month=11, day=26,
                         background="darkblue", foreground="white", borderwidth=2)
    calendar.grid(row=6, column=5)

    root.mainloop()

