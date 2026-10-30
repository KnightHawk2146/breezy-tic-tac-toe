"""
file: gamescreen.py

Author:   Kevin Viren
Date:     12/4/2023
Modified: 12/7/2023
"""
from breezypythongui import EasyFrame
from tkinter import PhotoImage
from tkinter.font import Font
from random import randint
import datetime
import homescreen


class GameScreen(EasyFrame):

    def __init__(self, title = "Breezy Tic-Tac-Toe"):
        EasyFrame.__init__(self)
        self.setSize(700, 700)
        
        
        #variables
        MAINFONT = Font(family = "Times New Roman", size=30)
        STATUSFONT = Font(family = "Times New Roman", size=25)

        self.images = {"blankLabel":PhotoImage(file = "assets/blank.png"),
                       "xLabel":PhotoImage(file = "assets/x.png"),
                       "oLabel":PhotoImage(file = "assets/o.png")}
        self.winner = ''
        self.moveNum = 0
        self.dateTime = ""
        
        self.coinflip = randint(1,2)
        self.playerTurn = ""
        if self.coinflip == 1:
            self.playerTurn = "xLabel"
        else:
            self.playerTurn = "oLabel"
            
        
        #Game screen label
        self.mainLabel = self.addLabel("Game Screen", row=0, column=0, columnspan=7, sticky="NSEW")
        self.mainLabel["font"] = MAINFONT
        

        #Game grid setup  - button properties are named after their place in the grid
        self.zeroZero = self.addButton(text="", row=1, column=2, command = (lambda button="zeroZero", coord=(0,0): self.updateImage(button,coord)))
        self.oneZero = self.addButton(text="", row=1, column=3, command = (lambda button="oneZero", coord=(0,1): self.updateImage(button,coord)))
        self.twoZero = self.addButton(text="", row=1, column=4, command = (lambda button="twoZero", coord=(0,2): self.updateImage(button,coord)))

        self.zeroOne = self.addButton(text="", row=2, column=2, command = (lambda button="zeroOne", coord=(1,0): self.updateImage(button,coord)))
        self.oneOne = self.addButton(text="", row=2, column=3, command = (lambda button="oneOne", coord=(1,1): self.updateImage(button,coord)))
        self.twoOne = self.addButton(text="", row=2, column=4, command = (lambda button="twoOne", coord=(1,2): self.updateImage(button,coord)))
        
        self.zeroTwo = self.addButton(text="", row=3, column=2, command = (lambda button="zeroTwo", coord=(2,0): self.updateImage(button,coord)))
        self.oneTwo = self.addButton(text="", row=3, column=3, command = (lambda button="oneTwo", coord=(2,1): self.updateImage(button,coord)))
        self.twoTwo = self.addButton(text="", row=3, column=4, command = (lambda button="twoTwo", coord=(2,2): self.updateImage(button,coord)))


        #Game grid list
        self.gridButtons = [
                    [self.zeroZero, self.oneZero, self.twoZero],
                    [self.zeroOne, self.oneOne, self.twoOne],
                    [self.zeroTwo, self.oneTwo, self.twoTwo]
                ]

        self.grid = [
                ['','',''],
                ['','',''],
                ['','','']
            ]

        
        #Giving each button the blank image attribute
        for lyst in self.gridButtons:
            for button in lyst:
                button["image"] = self.images["blankLabel"]


        #Game status label
        self.statusMsg = self.addLabel("", row=4, column=0, columnspan=7, sticky="NSEW")
        self.statusMsg["font"] = STATUSFONT
        self.statusMsg["background"] = "#AA0000"
        self.statusMsg["foreground"] = "#FDFDFD"
        self.updateStatusMsg()
            
        
        #Bottom buttons
        self.homeButton = self.addButton(text="Home", row=5, column=0, command = self.home)
        self.RestartButton = self.addButton(text="Restart", row=5, column=6, command = self.restart)

        self.recordDateTime()
        
    
    #----METHODS----
    
    def updateImage(self, button, coord):    
        """Updates the image of a clicked grid button"""
        button = getattr(self, button) #Link to my research on this function in /research/research.txt
        button["image"] = self.images[self.playerTurn]
        button["state"] = 'disabled'

        x,y = coord

        
        if self.playerTurn == "xLabel":
            self.grid[x][y] = 'X'
            self.playerTurn = "oLabel"
        else:
            self.grid[x][y] = 'O'
            self.playerTurn = "xLabel"

        self.moveNum += 1

        self.checkGrid()
        
        
    def updateStatusMsg(self):
        """Updates the label below the game grid"""
        if(self.winner == 'X'):
            self.statusMsg["text"] = "X WINS!!!"
            self.disableButtons()
            self.recordStats(self.winner)
        
        elif(self.winner == 'O'):
            self.statusMsg["text"] = "O WINS!!!"
            self.disableButtons()
            self.recordStats(self.winner)
            

        elif(self.moveNum >= 9) and (self.winner != 'X' or self.winner != 'O'):
            self.statusMsg["text"] = "DRAW"
            self.disableButtons()
            self.recordStats(self.winner)
            
        else:
            if self.playerTurn == "oLabel":
                self.statusMsg["text"] = "O turn"
            else:
                self.statusMsg["text"] = "X turn"


    def disableButtons(self):
        """Disables the grid buttons when an end game state has been recognised in checkgrid()"""
        for lyst in self.gridButtons:
            for button in lyst:
                button["state"] = "disabled"


    def checkGrid(self):
        """Checks to see if a player has won or if a draw has occurred"""
                #Rows
        if(self.grid[0][0] == self.grid[0][1] and self.grid[0][1] == self.grid[0][2]):
            
            self.winner = self.grid[0][0]

            
            
        elif(self.grid[1][0] == self.grid[1][1] and self.grid[1][1] == self.grid[1][2]):

            self.winner = self.grid[1][0]

            
            
        elif(self.grid[2][0] == self.grid[2][1] and self.grid[2][1] == self.grid[2][2]):

            self.winner = self.grid[2][0]



                #Columns
        elif(self.grid[0][0] == self.grid[1][0] and self.grid[1][0] == self.grid[2][0]):

            self.winner = self.grid[0][0]

            
        elif(self.grid[0][1] == self.grid[1][1] and self.grid[1][1] == self.grid[2][1]):

            self.winner = self.grid[0][1]

            
        elif(self.grid[0][2] == self.grid[1][2] and self.grid[1][2] == self.grid[2][2]):

            self.winner = self.grid[0][2]

            
                #Diagonals
        elif(self.grid[0][0] == self.grid[1][1] and self.grid[1][1] == self.grid[2][2]):

            self.winner = self.grid[0][0]

            
        elif(self.grid[0][2] == self.grid[1][1] and self.grid[1][1] == self.grid[2][0]):

            self.winner = self.grid[0][2]
            
            
        self.updateStatusMsg()
        

    def home(self):
        """closes the game screen and launches the home screen"""
        self.destroy() #Link to my research on this method in /research/research.txt
        homescreen.HomeScreen()
        

    def restart(self):
        """Clears the grid and sets up a new game"""
        self.winner = ''
        self.moveNum = 0
        self.dateTime = ""

        self.coinflip = randint(1,2)
        self.playerTurn = ""
        if self.coinflip == 1:
            self.playerTurn = "xLabel"
        else:
            self.playerTurn = "oLabel"

        self.grid = [
                ['','',''],
                ['','',''],
                ['','','']
            ]
        
        #Gives each button the blank image attribute to clear the grid
        for lyst in self.gridButtons:
            for button in lyst:
                button["state"] = "active"
                button["image"] = self.images["blankLabel"]

        self.recordDateTime()
        self.updateStatusMsg()

        
    def recordStats(self, winner):
        """Writes win/loss and time/date stats to gameHistory.txt"""
        if(winner == 'X'):
            fileName = "gameHistory.txt"
            file = open(fileName, 'a')#Research link on 'a' in /research/research.txt
            file.write(' '+"WIN"+23*' '+"LOSS"+15*" "+self.dateTime+4*"\n ")
            file.close()
            
        elif(winner == 'O'):
            fileName = "gameHistory.txt"
            file = open(fileName, 'a')
            file.write(' '+"LOSS"+23*' '+"WIN"+15*" "+self.dateTime+4*"\n ")
            file.close()
            
        else:
            fileName = "gameHistory.txt"
            file = open(fileName, 'a')
            file.write(' '+"DRAW"+22*' '+"DRAW"+15*" "+self.dateTime+4*"\n ")
            file.close()


    def recordDateTime(self):
        """Collects the system time and date and puts them in a property"""
        t = datetime.datetime.now()
        date = t.strftime("%x")
        hour = t.strftime("%I")
        minutes = t.strftime("%M")
        ampm = t.strftime("%p")

        self.dateTime = date+" | "+hour+":"+minutes+ampm
     

def main():
    GameScreen().mainloop()

if __name__ == "__main__":
    main()
