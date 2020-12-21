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
    Creates and shows the main window  .
    """
    # Add code here to create and initialize window.

    # For demo purposes, this is how you could access methods from other
    # modules:
    #matchNumber = Vorhersage_Algo.matchNumber()
    #model = ExperienceAlwaysWins(data)
    #winner = model.predict_winner('Tübingen', 'Leverkusen')
    #print(winner)

    # Basics für das Window
    root.geometry("1200x900")
    root.title("Bundesliga Vorhersagen")
    # Variables for the size of the picture
    x_Picture = 1200
    y_Picture = 900

    '''Trying to set the background picture '''
    image1 = Image.open("field.jpg")
    image1_resized = image1.resize((x_Picture, y_Picture), Image.ANTIALIAS)
    pic_ready = ImageTk.PhotoImage(image1_resized)

    lable_background = Label(image=pic_ready)
    lable_background.image = pic_ready
    lable_background.place(x=0, y=0)

    lable_background.config(x_Picture, y_Picture)

    # Lable for the header
    myLable = Label(root, text="Erstelle hier Vorhersagen zu anstehenden Bundesliga Spielen!", justify=CENTER,
                    bg="light green")
    myLable.pack(side="top", padx=10)
    myLable.config(font=("Times", 17))

    # Marking where the lables start, depending on the size of the main window
    begin_Labels = x_Picture / 4

    '''Setting up all the frames to insert the labels and the buttons into '''
    rahmenBelow = Frame(master=root, bg="purple")
    rahmenBelow.pack(side="bottom", padx=begin_Labels, pady=200)

    rahmenMiddle = Frame(master=root, bg="firebrick")
    rahmenMiddle.pack(side="left", padx=begin_Labels, pady=5)

    rahmenTeamHome = Frame(master=rahmenMiddle, bg="forest green")
    rahmenTeamHome.pack(side="left", padx=5, pady=5)

    rahmenTeamGuest = Frame(master=rahmenMiddle, bg="cornflower blue")
    rahmenTeamGuest.pack(side="right", padx=5, pady=5)

    rahmenCalender = Frame(master=rahmenMiddle, bg="cadet blue")
    rahmenCalender.pack(side="top", padx=15, pady=15)

    rahmenAlgo = Frame(master=rahmenBelow, bg="lightblue")
    rahmenAlgo.pack(side="left", padx=5, pady=5)

    rahmenCrawler = Frame(master=rahmenBelow, bg="lightgreen")
    rahmenCrawler.pack(side="left", padx=5, pady=5)

    # All of the labels
    settingsLable = Label(rahmenCrawler, text="Activate the AI or Start the Crawler here:", bg="silver")
    settingsLable.pack(side="top", padx=5)
    settingsLable.config(font=("TKCaptionFont", 12))

    dropLable1 = Label(master=rahmenTeamHome, text="Choose the Home Team:", bg="mediumblue", fg="yellow")
    dropLable1.pack(side="top", padx=5, pady=5)
    dropLable1.config(font=("TKCaptionFont", 12))

    # Button to calculate odds,call function to predict the winner from the other script
    '''Does not work yet 
    -the button is all the way up there because otherwise the frames are arranged weirdly... '''
    buttonOdds = Button(master=rahmenMiddle, text="Calculate Odds", font=myFont, bg="orange",
                        command= algoPrediction)
    buttonOdds.pack(side="left", padx=40, pady=40)

    dropLable2 = Label(master=rahmenTeamGuest, text="Choose the Guest Team:", bg="yellow", fg="mediumblue")
    dropLable2.pack(side="top", padx=5, pady=5)
    dropLable2.config(font=("TKCaptionFont", 12))

    chooseCrawlerLabel = Label(master=rahmenAlgo, text="Choose an Algorithm for calculation:")
    chooseCrawlerLabel.pack(side="top", padx=5, pady=5)
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
    dropDown1 = OptionMenu(rahmenTeamHome, clicked1, *teamsHome)
    # This is for the Algo section, to know which team is selected
    homeTeam = clicked1.get()
    dropDown1.pack(side="top", padx=5, pady=5)

    # Dropdowns für Mannschaften2
    firstTeamGuest = list(teamsGuest)[0]
    clicked2 = StringVar(root)
    clicked2.set(firstTeamGuest)
    dropDown2 = OptionMenu(rahmenTeamGuest, clicked2, *teamsGuest)
    # This is for the Algo section, to know which team is selected
    guestTeam = clicked2.get()
    dropDown2.pack(side="top", padx=5, pady=5)


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
    dropDownAlgo = OptionMenu(rahmenAlgo, clicked3, *Algos)
    dropDownAlgo.pack(side="top", padx=5)

    # Buttons to activate the search for the data
    buttonCrawler = Button(rahmenCrawler, text="Activate Crawler", padx=10, pady=5)
    buttonCrawler.pack(side="left", padx=5)

    # Button to activate the AI Process
    buttonAlgo = Button(rahmenCrawler, text="Activate the AI", padx=10, pady=5)
    buttonAlgo.pack(side="left", padx=5)

    # Setting up a calender to choose the game day

    chooseDateLable = Label(master=rahmenCalender, text="Choose the day \n of the game")
    chooseDateLable.pack(side="top", padx=5, pady=5)
    chooseDateLable.config(font=("TKCaptionFont", 12))

    calendar = DateEntry(rahmenCalender, width=12, year=2020, month=11, day=26,
                         background="darkblue", foreground="white", borderwidth=2)
    calendar.pack(side="top", padx=5, pady=5)

    root.mainloop()

