"""
Add your GUI code here.
"""
from tkinter import *
from PIL import Image, ImageTk
from crawler import fetch_data
from models import ExperienceAlwaysWins
import Vorhersage_Algo
root = Tk()


def main():
    """
    Creates and shows the main window.
    """
    # Add code here to create and initialize window.

    # For demo purposes, this is how you could access methods from other
    # modules:
    matchNumber = Vorhersage_Algo.matchNumber()
    data = fetch_data()
    model = ExperienceAlwaysWins(data)
    winner = model.predict_winner('Tübingen', 'Leverkusen')
    print(winner)


    # Basics für das Window
    root.geometry("900x800")
    root.title("Bundesliga Vorhersagen")

    '''Trying to set the background picture '''
    image1 = Image.open("D:\\Pictures\\GUI Teamprojekt\\Fußballfeld.jpg")
    image1_resized= image1.resize((800,600), Image.ANTIALIAS)
    pic_ready = ImageTk.PhotoImage(image1_resized)

    lable_background = Label(image = pic_ready)
    lable_background.image = pic_ready
    lable_background.place(x= 0, y= 0)

    lable_background.config(width=900, height = 700)

    #Lable for the header
    myLable = Label(root, text="Erstelle hier Vorhersagen zu anstehenden Bundesliga Spielen!")
    myLable.grid(row=0, column=1, columnspan=3)
    myLable.config(font=("Courier", 10))

    # Empty Line - don't know how else to do it
    myEmptyLable = Label(root, text="           ")
    myEmptyLable.grid(row=5, column=1, columnspan=3)

    # Dropdowns für Mannschaften1
    clicked1 = StringVar()
    clicked1.set("Bayern")
    dropDown1 = OptionMenu(root, clicked1, "Bayern", "Hamburg", "Stuttgart", "Bremen", "Madrid", "Barcelona",
                           "Bukarest")
    homeTeam = clicked1.get()
    dropDown1.grid(row=6, column=1)

    # Lable für die Dropdowns
    dropLable1 = Label(root, text="Choose the Home Team:")
    dropLable1.grid(row=5, column=1)

    #Dropdowns für Mannschaften2
    clicked2 = StringVar()
    clicked2.set("Bayern")
    dropDown2 = OptionMenu(root, clicked2, "Bayern", "Hamburg", "Stuttgart", "Bremen", "Madrid", "Barcelona",
                           "Bukarest")
    guestTeam = clicked2.get()
    dropDown2.grid(row=6, column=3)

    # Lable für die Dropdowns
    dropLable2 = Label(root, text="Choose the Guest Team:")
    dropLable2.grid(row=5, column=3)

    # Buttons für die Aufrufe der Funktionen
    buttonCrawler = Button(root, text="Activate Crawler to get the needed Data", padx=10, pady=5)
    buttonCrawler.grid(row=2, column=1)

    # Button to activat the AI Process
    buttonAlgo = Button(root, text="Activate the AI", padx=10, pady=5)
    buttonAlgo.grid(row=3, column=1)

    myEmptyLable2 = Label(root, text="           ")
    myEmptyLable2.grid(row=4, column=1, columnspan=3)

    # Button to calculate odds,call function to predict the winner from the other skript
    buttonOdds = Button(root, text="Calculate Odds", padx=30, pady=15,
                        command=matchNumber(clicked1, clicked2))
    # Not sure if this command-line up there is right, maybe Yupei knows better what to call?

    buttonOdds.grid(row=6, column=2)

    root.mainloop()
