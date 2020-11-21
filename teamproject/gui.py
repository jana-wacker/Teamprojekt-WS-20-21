"""
Add your GUI code here.
"""
from tkinter import *
root = Tk()

from teamproject.crawler import fetch_data
from teamproject.models import ExperienceAlwaysWins


def main():
    """
    Creates and shows the main window.
    """
    # Add code here to create and initialize window.

    # For demo purposes, this is how you could access methods from other
    # modules:
    data = fetch_data()
    model = ExperienceAlwaysWins(data)
    winner = model.predict_winner('Tübingen', 'Leverkusen')
    print(winner)

    #My Code here

    # Basics für das Window
    root.geometry("800x500")
    root.title("Bundesliga Vorhersagen")

    myLable = Label(root, text="Erstelle hier Vorhersagen zu anstehenden Bundesliga Spielen!")
    myLable.grid(row=0, column=1, columnspan=3)
    myLable.config(font=("Courier", 10))

    # Empty Line - don't know how else to do it
    myEmptyLable = Label(root, text="           ")
    myEmptyLable.grid(row=5, column=1, columnspan=3)

    # Buttons für die Aufrufe der Funktionen
    buttonCrawler = Button(root, text="Activate Crawler", padx=10, pady=5)
    buttonCrawler.grid(row=2, column=1)

    # Button to activat the AI Process
    buttonAlgo = Button(root, text="Activate AI", padx=10, pady=5)
    buttonAlgo.grid(row=3, column=1)

    myEmptyLable2 = Label(root, text="           ")
    myEmptyLable2.grid(row=4, column=1, columnspan=3)

    # Button to calculate odds
    buttonOdds = Button(root, text="Calculate Odds", padx=30, pady=15)
    buttonOdds.grid(row=6, column=2)

    # Dropdowns für Mannschaften
    clicked1 = StringVar()
    clicked1.set("Bayern")
    dropDown1 = OptionMenu(root, clicked1, "Bayern", "Hamburg", "Stuttgart", "Bremen", "Madrid", "Barcelona",
                           "Bukarest")
    dropDown1.grid(row=6, column=1)

    # Lable für die Dropdowns
    dropLable1 = Label(root, text="Choose the first Team:")
    dropLable1.grid(row=5, column=1)

    clicked2 = StringVar()
    clicked2.set("Bayern")
    dropDown2 = OptionMenu(root, clicked2, "Bayern", "Hamburg", "Stuttgart", "Bremen", "Madrid", "Barcelona",
                           "Bukarest")
    dropDown2.grid(row=6, column=3)

    # Lable für die Dropdowns
    dropLable2 = Label(root, text="Choose the second Team:")
    dropLable2.grid(row=5, column=3)

    root.mainloop()
