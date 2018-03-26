import os
from chip import *

clear = lambda: os.system('clear')

class Console:

    # Constructor, including the statemachine-loop for the menu
    def __init__(self):
        
        # Console variables
        self.menuState = 0
        self.loadedFile = ''
        self.loadedFlag = 0
        self.writtenFile = ''
        self.modified = 0
        self.chip = Chip()
        self.printMenu()

        # Statemachine für the menu
        while (self.menuState != 6):
            if (self.menuState == 0):
                self.printMenu()
                self.menuState = self.askMenu()
            elif (self.menuState == 1):
                self.printLoad()
                self.menuState = self.askLoad()
            elif (self.menuState == 2):
                self.printWrite()
                self.menuState = self.askWrite()
            elif (self.menuState == 3):
                self.printAllTiles()
                self.menuState = self.askAllTiles()
            elif (self.menuState == 4):
                self.printOneTile()
                self.menuState = self.askOneTile()
            elif (self.menuState == 5):
                self.printOneLut()
                self.menuState = self.askOneLut()

        # End the menu (menuState = 6)
        clear()
        print("Goodbye :)")

    def printMenu(self):
        clear()
        print ("H1K Bitstream Tile Manipulator")
        print ("------------------------------")
        print ("Loaded File:  " + self.loadedFile)
        if (self.modified == 0):
            print ("Modified:     No")
        else:
            print ("Modified:     Yes")
        print ("Written File: " + self.writtenFile)
        print ("------------------------------")
        print ("1 - Load .asc File")
        print ("2 - Write .asc File")
        print ("3 - Show all tiles")
        print ("4 - Show one tile")
        print ("5 - Show one LUT")
        print ("6 - Quit")
        print ("------------------------------")

    def askMenu(self):
        while True:
            key = input("Selection: ")
            if (not(key.isdigit())):
                self.printMenu()
                print ("Please enter a number (1-6)")
            elif (int(key) < 1 or int(key) > 6):
                self.printMenu()
                print ("Please enter a number (1-6)")
            else:
                return int(key)

    def printLoad(self):
        clear()
        print ("H1K Bitstream Tile Manipulator")
        print ("------------------------------")
        print ("Loading Menu") 
        print ("------------------------------")

    def askLoad(self):
        self.loadedFile = input("Filename to read (.asc): ")
        self.chip.readFile(self.loadedFile)
        self.loadedFlag = 1
        return 0

    def printWrite(self):
        clear()
        print ("H1K Bitstream Tile Manipulator")
        print ("------------------------------")
        print ("Writing Menu") 
        print ("------------------------------")

    def askWrite(self):
        self.writtenFile = input("Filename to write (.asc): ")
        self.chip.writeFile(self.writtenFile)
        return 0

    def printAllTiles(self):
        clear()
        print ("H1K Bitstream Tile Manipulator")
        print ("------------------------------")
        print ("All Tiles:") 
        print ("------------------------------")
        for x in range(14):
            print (' x  y mod?  ', end="")
        print("")

        for y in range(18):
            for x in range(14):
                modded = 0
                for l in range(8):
                    lutBits = int(self.chip.getLutBitsAll(x, y, l))
                    if (lutBits > 0):       
                        modded = 1
                print ('{0:2d} {1:2d} {2:2d}    '.format(x, y, modded), end="")
            print("")


    def askAllTiles(self):
        key = input("Press Enter: ")
        return 0

    def printOneTile(self):
        clear()
        print ("H1K Bitstream Tile Manipulator")
        print ("------------------------------")
        print ("One Tile Menu") 
        print ("------------------------------")

    def askOneTile(self):
        key = input("Selection: ")
        return 0

    def printOneLut(self):
        clear()
        print ("H1K Bitstream Tile Manipulator")
        print ("------------------------------")
        print ("One Lut Menu") 
        print ("------------------------------")

    def askOneLut(self):
        key = input("Selection: ")
        return 0

