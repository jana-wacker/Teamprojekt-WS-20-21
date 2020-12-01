"""
Add your GUI code here.
"""
from tkinter import *
from PIL import Image, ImageTk
from crawler import fetch_data
from models import ExperienceAlwaysWins
from Vorhersage_Algo import algoPrediction
from tkcalendar import DateEntry
root = Tk()


def main():
    """
    Creates and shows the main window.
    """
    # Add code here to create and initialize window.

    # For demo purposes, this is how you could access methods from other
    # modules:
    #matchNumber = Vorhersage_Algo.matchNumber()
    data = fetch_data()
    model = ExperienceAlwaysWins(data)
    winner = model.predict_winner('Tübingen', 'Leverkusen')
    print(winner)


    # Basics für das Window
    root.geometry("700x400")
    root.title("Bundesliga Vorhersagen")

    '''Trying to set the background picture '''
    image1 = Image.open("D:\\Pictures\\GUI Teamprojekt\\Fußballfeld.jpg")
    image1_resized = image1.resize((700, 400), Image.ANTIALIAS)
    pic_ready = ImageTk.PhotoImage(image1_resized)

    lable_background = Label(image=pic_ready)
    lable_background.image = pic_ready
    lable_background.place(x=0, y=0)

    lable_background.config(width=700, height=400)

    # Lable for the header
    myLable = Label(root, text="Erstelle hier Vorhersagen zu anstehenden Bundesliga Spielen!")
    myLable.grid(row=0, column=1, columnspan=6, )
    myLable.config(font=("TkCaptionFont", 14))

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
    settingsLable = Label(root, text="Activate the AI or Start the Crawler here:")
    settingsLable.grid(row=9, column=2, columnspan=6)

    chooseDateLable = Label(root, text="Choose the day \n of the game")
    chooseDateLable.grid(row=5, column=5)

    dropLable1 = Label(root, text="Choose the Home Team:")
    dropLable1.grid(row=5, column=1)

    dropLable2 = Label(root, text="Choose the Guest Team:")
    dropLable2.grid(row=5, column=3)

    chooseCrawlerLabel = Label(root, text="Choose an Algorithm for calculation:")
    chooseCrawlerLabel.grid(row=12, column=1)

    # Bsp List for TeamHome
    teamsHome = {"Tübingen": 1, "München": 2, "Madrid": 3, "Hamburg": 4, "Bukarest": 5}

    # Bsp List for TeamGuest
    teamsGuest = {"Bayern": 1, "München": 2, "Madrid": 3, "Hamburg": 4, "Bukarest": 5}

    '''Setup of the dropdown menus for the teams 
    clicked1 /2 : These is the Team the user selected, at the beginning it is set the FIRST team in the list 

    The method *teamsHome.keys() puts all of the keys, from the teamsHome List into the dropdown menu. 

    '''
    # Dropdowns für Mannschaften1
    firstTeamHome = list(teamsHome.keys())[0]
    clicked1 = StringVar(root)
    clicked1.set(firstTeamHome)
    dropDown1 = OptionMenu(root, clicked1, *teamsHome.keys())
    # This is for the Algo section, to know which team is selected
    homeTeam = clicked1.get()
    dropDown1.grid(row=6, column=1)

    # Dropdowns für Mannschaften2
    firstTeamGuest = list(teamsGuest.keys())[0]
    clicked2 = StringVar(root)
    clicked2.set(firstTeamGuest)
    dropDown2 = OptionMenu(root, clicked2, *teamsGuest.keys())
    # This is for the Algo section, to know which team is selected
    guestTeam = clicked2.get()
    dropDown2.grid(row=6, column=3)

    # The choice of an algorithm
    optionsAlgo = {"Algo1": 1, "Algo2": 2, "Algo3": 3}
    firstAlgo = list(optionsAlgo.keys())[0]
    clicked3 = StringVar()
    clicked3.set(firstAlgo)
    dropDownAlgo = OptionMenu(root, clicked3, *optionsAlgo.keys())
    dropDownAlgo.grid(row=13, column=1)

    # Buttons to activate the search for the data
    buttonCrawler = Button(root, text="Activate Crawler", padx=10, pady=5)
    buttonCrawler.grid(row=10, column=3)

    # Button to activate the AI Process
    buttonAlgo = Button(root, text="Activate the AI", padx=10, pady=5)
    buttonAlgo.grid(row=10, column=4)

    # Button to calculate odds,call function to predict the winner from the Vorhersage_Algo script
    buttonOdds = Button(root, text="Calculate Odds", padx=18, pady=15, command=algoPrediction(homeTeam, guestTeam) )
    buttonOdds.grid(row=7, column=2)

    # Setting up a calender to choose the game day
    calendar = DateEntry(root, width=12, year=2020, month=11, day=26,
                         background="darkblue", foreground="white", borderwidth=2)
    calendar.grid(row=6, column=5)

    root.mainloop()

