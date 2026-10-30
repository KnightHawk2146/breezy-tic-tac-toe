"""
file: gamehistory.py

Author:   Kevin Viren
Date:     12/4/2023
Modified: 12/11/2023
"""
from breezypythongui import EasyFrame
from tkinter.font import Font
import homescreen


class GameHistory(EasyFrame):

    def __init__(self, title = "Breezy Tic-Tac-Toe"):
        EasyFrame.__init__(self)
        self.setSize(700, 700)

        LABELFONT = Font(family = "Times New Roman", size=25)

        self.gameHistoryLabel = self.addLabel("Game History", row=0, column=0, columnspan=2, sticky="NSEW")
        self.gameHistoryLabel["font"] = LABELFONT
        self.gameHistoryLabel["background"] = "#AA0000"
        self.gameHistoryLabel["foreground"] = "#FDFDFD"

        self.homeButton = self.addButton(text="Home", row=0, column=2, command = self.home)

        self.outputArea = self.addTextArea("", row=1, column=0, columnspan=3, height=35)

        self.openFile()


    def home(self):
        """closes the game screen and launches the home screen"""
        self.destroy() #Link to my research on this method in /research/research.txt
        h = homescreen.HomeScreen()

        
    def openFile(self):
        try:
            fileName = "gameHistory.txt"
            file = open(fileName, 'r')
            text = file.read()
            file.close()
            self.outputArea.setText(text)
            self.outputArea["state"] = "disabled"
        except:
            self.messageBox(title = "ERROR", message = "Unable to read 'gameHistory.txt'. Make sure the file exists in 'Breezy Tic-Tac-Toe' folder.")


def main():
    GameHistory().mainloop()

if __name__ == "__main__":
    main()
