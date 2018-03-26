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

    # menuState == 0
    def printMenu(self):
        clear()
        print ("HX1K Bitstream Tile Manipulator")
        print ("--------------------------------------------------------------------------")
        print ("Loaded File:  " + self.loadedFile)
        if (self.modified == 0):
            print ("Modified:     No")
        else:
            print ("Modified:     Yes")
        print ("Written File: " + self.writtenFile)
        print ("--------------------------------------------------------------------------")
        print ("1 - Load .asc File")
        print ("2 - Write .asc File")
        print ("3 - Show all tiles")
        print ("4 - Show one tile")
        print ("5 - Show one LUT")
        print ("6 - Quit")
        print ("--------------------------------------------------------------------------")

    # menuState == 0, input
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

    # menuState == 1
    def printLoad(self):
        clear()
        print ("HX1K Bitstream Tile Manipulator")
        print ("--------------------------------------------------------------------------")
        print ("Loading .asc File") 
        print ("--------------------------------------------------------------------------")

    # menuState == 1, input
    def askLoad(self):
        self.loadedFile = input("Filename to read (.asc): asc/")
        self.loadedFile = "asc/" + self.loadedFile
        self.chip.readFile(self.loadedFile)
        self.loadedFlag = 1
        return 0

    # menuState == 2
    def printWrite(self):
        clear()
        print ("HX1K Bitstream Tile Manipulator")
        print ("--------------------------------------------------------------------------")
        print ("Writing .asc File") 
        print ("--------------------------------------------------------------------------")

    # menuState == 2, input
    def askWrite(self):
        self.writtenFile = input("Filename to write (.asc): asc/")
        self.writtenFile = "asc/" + self.writtenFile
        self.chip.writeFile(self.writtenFile)
        return 0

    # menuState == 3
    def printAllTiles(self):
        clear()
        print ("HX1K Bitstream Tile Manipulator")
        print ("--------------------------------------------------------------------------")
        print ("All Tiles:") 
        print ("--------------------------------------------------------------------------")
        print ("n.a. = not available, io = io_tile, ram_b = ram_b_tile, ram_t = ram_t_tile")
        print ("0 = logic_tile no data in LUT")
        print ("1 = logic_tile with data in LUT")
        print ("--------------------------------------------------------------------------")

        print('   x', end="")
        for x in range(14):
            print ('  {0:2d}   '.format(x), end="")
        print("")
        print(" y")

        for y in range(18):
            print('{0:2d}  '.format(y), end="")
            for x in range(14):
                modded = 0
                type = self.chip.tiles[y][x].getType()
                if (type == '.logic_tile'):
                    for l in range(8):
                        lutBits = int(self.chip.getLutBitsAll(x, y, l))
                        if (lutBits > 0):       
                            modded = 1
                    print ('  {0:2d}   '.format(modded), end="")
                elif (type == '.io_tile'):
                    print ('   io  ', end="")
                elif (type == '.ramb_tile'):
                    print (' ram_b ', end="")
                elif (type == '.ramt_tile'):
                    print (' ram_t ', end="")
                else:
                    print ('  n.a. ', end="")
            print("")
        print("")


    # menuState == 3, input
    def askAllTiles(self):
        key = input("Press Enter: ")
        return 0

    # menuState == 4
    def printOneTile(self):
        clear()
        print ("HX1K Bitstream Tile Manipulator")
        print ("--------------------------------------------------------------------------")
        print ("One Tile Menu") 
        print ("--------------------------------------------------------------------------")

    # menuState == 4, input
    def askOneTile(self):
        key = input("Selection: ")
        return 0

    # menuState == 5
    def printOneLut(self):
        clear()
        print ("HX1K Bitstream Tile Manipulator")
        print ("--------------------------------------------------------------------------")
        print ("One Lut Menu") 
        print ("--------------------------------------------------------------------------")
        self.chip.printLutTable(9,1,0)

    # menuState == 5, input
    def askOneLut(self):
        key = input("Selection: ")
        return 0

