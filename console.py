import os
import subprocess
import click
from chip import *

clear = lambda: os.system('clear')

class Console:

    # Constructor, including the statemachine-loop for the menu
    def __init__(self):
        
        # Console variables
        self.menuState = 0
        self.loadedFile = ''
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
                self.menuState = self.loadFile()

            elif (self.menuState == 2):
                self.menuState = self.writeFile()

            elif (self.menuState == 3):
                self.menuState = self.printAllTiles()

            elif (self.menuState == 4):
                self.menuState = self.printOneTile()

            elif (self.menuState == 5):
                self.menuState = self.printOneLut()

        # End the menu (menuState = 6)
        clear()
        print("Goodbye :)")

    # MENU --------------
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
        print ("5 - Show and modify one LUT")
        print ("6 - Quit")
        print ("--------------------------------------------------------------------------")

    def askMenu(self):
        return self.askValue(1, 6, "Selection: ")        

    # LOAD FILE ---------
    # menuState == 1
    def loadFile(self):
        clear()
        print ("HX1K Bitstream Tile Manipulator")
        print ("--------------------------------------------------------------------------")
        print ("Loading .asc File") 
        print ("--------------------------------------------------------------------------")
        print ("Content of folder asc/:")
        print ("")
        subprocess.check_call(['ls', '-l'], cwd="asc/")
        print ("")
        self.loadedFile = input("Filename to read (.asc): asc/")
        self.loadedFile = "asc/" + self.loadedFile
        self.chip.readFile(self.loadedFile)
        self.loadedFlag = 1
        return 0

    # WRITE FILE --------
    # menuState == 2
    def writeFile(self):
        clear()
        print ("HX1K Bitstream Tile Manipulator")
        print ("--------------------------------------------------------------------------")
        print ("Writing .asc File") 
        print ("--------------------------------------------------------------------------")
        print ("")
        subprocess.check_call(['ls', '-l'], cwd="asc/")
        print ("")
        if (self.loadedFile == ''):
            print ('No File loaded!')
            print ('Press any key')
            click.getchar()
            return 0
        self.writtenFile = input("Filename to write (.asc): asc/")
        self.writtenFile = "asc/" + self.writtenFile
        self.chip.writeFile(self.writtenFile)
        return 0

    # ALL TILES ---------
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

        if (self.loadedFile == ''):
            print ('No File loaded!')
            print ('Press any key')
            click.getchar()
            return 0

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
                        lutBits = int(self.chip.getLutBits(x, y, l))
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
        
        print ("Press any key")
        click.getchar()
        return 0

    # ONE TILE ----------
    # menuState == 4
    def printOneTile(self):
        
        one_tile_state = 0
        one_tile_luts = []

        if (self.loadedFile == ''):
            clear()
            print ("HX1K Bitstream Tile Manipulator")
            print ("--------------------------------------------------------------------------")
            print ("One Tile Menu") 
            print ("--------------------------------------------------------------------------")
            print ('No File loaded!')
            print ('Press any key')
            click.getchar()
            return 0

        while (one_tile_state != 2):
              
            if (one_tile_state == 0):
                clear()
                print ("HX1K Bitstream Tile Manipulator")
                print ("--------------------------------------------------------------------------")
                print ("One Tile Menu") 
                print ("--------------------------------------------------------------------------")
                lut_x = self.askValue(0, 13, "Enter x of the tile (0-13): ") 
                lut_y = self.askValue(0, 17, "Enter y of the tile (0-17): ")
                if (self.chip.tiles[lut_y][lut_x].getType() != '.logic_tile'):
                    print ("This is not a logic tile!")
                    print ("Press any key")
                    click.getchar()
                    return 0
                for i in range(8):
                    one_tile_luts.append(self.chip.getLutTable(lut_x, lut_y, i))
                one_tile_state = 1

            if (one_tile_state == 1):
                clear()
                print ("HX1K Bitstream Tile Manipulator")
                print ("--------------------------------------------------------------------------")
                print ("One Tile Menu") 
                print ("--------------------------------------------------------------------------")
                print ("Tile x: {0:0>2}, y: {1:0>2}".format(lut_x, lut_y))
                print ("--------------------------------------------------------------------------")
                print ("LUT In    LUT 0   LUT 1   LUT 2   LUT 3   LUT 4   LUT 5   LUT 6   LUT 7")
                for x in range(16):
                    print (" {0:0>4}     ".format((bin(x))[2:]), end ="")
                    for y in range(8):
                        print ("   {0:1}    ".format(one_tile_luts[y][x]), end="")
                    print ("")

                print ("")
                print ("Press any key")
                click.getchar()
                one_tile_state = 2

        return 0


    # ONE LUT -----------
    # menuState == 5
    def printOneLut(self):

        one_lut_state = 0
        lut_table = ''
        lut_out = ''
        lut_x = 0
        lut_y = 0
        lut_n = 0
        cursor = 0

        if (self.loadedFile == ''):
            clear()
            print ("HX1K Bitstream Tile Manipulator")
            print ("--------------------------------------------------------------------------")
            print ("Show and modify one LUT") 
            print ("--------------------------------------------------------------------------")
            print ('No File loaded!')
            print ('Press any key')
            click.getchar()
            return 0

        while (one_lut_state != 2):

            if (one_lut_state == 0):
                clear()
                print ("HX1K Bitstream Tile Manipulator")
                print ("--------------------------------------------------------------------------")
                print ("Show and modify one LUT") 
                print ("--------------------------------------------------------------------------")
                lut_x = self.askValue(0, 13, "Enter x of the tile (0-13): ") 
                lut_y = self.askValue(0, 17, "Enter y of the tile (0-17): ")
                lut_n = self.askValue(0, 7,  "Enter nr of the lut (0-7): ")
                if (self.chip.tiles[lut_y][lut_x].getType() != '.logic_tile'):
                    print ("This is not a logic tile!")
                    print ("Press any key")
                    click.getchar()
                    return 0
                lut_table = (self.chip.getLutTable(lut_x, lut_y, lut_n))
                one_lut_state = 1

            elif (one_lut_state == 1):
                clear()
                print ("HX1K Bitstream Tile Manipulator")
                print ("--------------------------------------------------------------------------")
                print ("Show and modify one LUT") 
                print ("--------------------------------------------------------------------------")
                print ("Tile x: {0:0>2}, y: {1:0>2} LUT-Nr.: {2:1}".format(lut_x, lut_y, lut_n))
                print ("--------------------------------------------------------------------------")
                print ("Usage: UP = w, DOWN = s, TOGGLE = t, CONFIRM ALL = c, ESCAPE = e")
                print ("--------------------------------------------------------------------------")
                print ("LUT In    LUT Out")
                for i in range(16):
                    print (" {0:0>4}        {1:1}".format((bin(i))[2:], lut_table[i]), end="")
                    if (cursor == i):
                        print ("   *")
                    else:
                        print("")

                print ("")                
                print ("Navigate with w, s, t, e, c")    

                key = click.getchar()
                if (key == 'w' and cursor > 0):
                    cursor -= 1
                elif (key == 's' and cursor < 15):
                    cursor += 1
                elif (key == 't'):
                    if (lut_table[cursor] == '1'):
                        lut_table[cursor] = '0'
                    else:
                        lut_table[cursor] = '1'
                elif (key == 'e'):
                    return 0
                elif (key == 'c'):
                    for i in range(16):
                        lut_out = lut_out + lut_table[i]
                    self.chip.setLutTableBits(lut_x, lut_y, lut_n, lut_out)
                    self.modified = 1
                    one_lut_state = 2
        return 0


    # ------------------------------------
    # Helper functions -------------------
    # ------------------------------------
    
    # Ask in console for a int-value
    # parameters: not_below, not_above, question_text
    def askValue(self, not_below, not_above, question_text):
        while True:
            key = input(question_text)
            if (not(key.isdigit())):
                print ("Please enter a number in range {0:2d} {1:2d}.".format(not_below, not_above))
            elif (int(key) < not_below or int(key) > not_above):
                print ("Please enter a number in range {0:2d} {1:2d}.".format(not_below, not_above))
            else:
                return int(key)

