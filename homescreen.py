"""
file: homescreen.py

Author:   Kevin Viren
Date:     12/4/2023
modified: 12/11/2023
"""
from breezypythongui import EasyFrame
from tkinter import PhotoImage
from tkinter.font import Font
import gamescreen
import gamehistory


class HomeScreen(EasyFrame):
        
    def __init__(self, title = "Breezy Tic-Tac-Toe"): 
        EasyFrame.__init__(self)
        self.setSize(700, 700)

        #variables for game history
        self.xUser = ""
        self.oUser = ""

        #Welcome label
        FONT = Font(family = "Times New Roman", size=35, slant = "italic")  
        self.welcomeMsg = self.addLabel("Welcome to Breezy Tic-Tac-Toe!", row=0, column=0, columnspan=4, sticky="NSEW")
        self.welcomeMsg["font"] = FONT
        self.welcomeMsg["background"] = "#AA0000"
        self.welcomeMsg["foreground"] = "#FDFDFD"
        
        #X and O image icons
        self.xLabelImage = PhotoImage(file = "assets/x.png")
        self.oLabelImage = PhotoImage(file = "assets/o.png")
        self.xLabel = self.addLabel("", row=1, column=0, columnspan=2, sticky="NSEW")
        self.oLabel = self.addLabel("", row=1, column=2, columnspan=2, sticky="NSEW")
        self.xLabel["image"] = self.xLabelImage
        self.oLabel["image"] = self.oLabelImage

        #player name input text fields
        self.addLabel("Player X name:", row=2, column=0, sticky="NE")
        self.addLabel("Player O name:", row=2, column=2, sticky="NE")
        self.xInputField = self.addTextField(text = "", row=2, column=1, sticky="NW")
        self.oInputField = self.addTextField(text = "", row=2, column=3, sticky="NW")
        
        #menu buttons               -ADD COMMANDS!
        self.practiceButton = self.addButton(text="Practice", row=4, column=0, command = self.launchPractice)
        self.playGameButton = self.addButton(text="Play Game", row=4, column=1, command = self.launchGame)
        self.gameHistoryButton = self.addButton(text="Game History", row=4, column=3, command = self.launchGameHistory)

    
    def launchPractice(self):
        """Launches the game screen for a practice game""" #NEW CONCEPT - MULTI-SCREEN/MULTI-WINDOW GUI APPLICATIONS
        self.destroy() #Research source in /research/research.txt

        g = gamescreen.GameScreen()

    
    def launchGame(self):
        """Launches the game screen for a recorded game"""
        self.xUser = self.xInputField.getText()
        self.oUser = self.oInputField.getText()

        if(self.xUser=="" or self.oUser==""):
            self.messageBox(title = "ERROR", message = "Both player usernames must be entered for this game mode.")
        elif(len(self.xUser) > 20 or len(self.oUser) > 20):
            self.messageBox(title = "ERROR", message = "Usernames must be 20 characters or less.")
                
        else:
            self.destroy() #Research source in /research/research.txt

            g = gamescreen.GameScreen()

            #Writes usernames to gameHistory.txt
            fileName = "gameHistory.txt"
            file = open(fileName, 'a') #Research link on 'a' in /research/research.txt
            file.write(" "+self.xUser+18*" "+self.oUser+"\n")
            file.close()
            

    def launchGameHistory(self):
        """Launches the game history screen"""
        self.destroy() #Research source in /research/research.txt

        gh = gamehistory.GameHistory()



def main():
    HomeScreen().mainloop()


if __name__ == "__main__":
    main()
        
