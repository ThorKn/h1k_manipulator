import io
from tile import *

class Chip:
    
    lut_bit_order = (4, 14, 15, 5, 6, 16, 17, 7, 3, 13, 12, 2, 1, 11, 10, 0)
    
    def __init__(self):
        self.comment = ''
        self.device = ''
        self.tiles = [[0 for j in range(14)] for i in range(18)]
        
    def readFile(self, filename):
        
        # Read the file from filename
        with open(filename) as f:
            buf = f.read()
        
        # shorten the lines in buf (delete string terminationsymbol)
        # and write the lines to data
        buf_2 = io.StringIO(buf)
        data = [line[:-1] for line in buf_2]

#        self.comment = data[0]
        self.device = data[0]
        i = 1
        line = data[i]
        
        # parse the lines in data and fill the tiles-array    
        while True:            
                                  
            # IO Tile
            if (line[0:8] == '.io_tile'):
                x = int(line[9:].split()[0])
                y = int(line[9:].split()[1])
                self.tiles[y][x] = Tile('.io_tile', x, y)
                for j in range(16):
                    i += 1
                    self.tiles[y][x].setBitsRow(j, data[i])
           
            # LOGIC Tile
            if (line[0:11] == '.logic_tile'):
                x = int(line[12:].split()[0])
                y = int(line[12:].split()[1])
                self.tiles[y][x] = Tile('.logic_tile', x, y)
                for j in range(16):
                    i += 1
                    self.tiles[y][x].setBitsRow(j, data[i])
            
            # RAMB Tile
            if (line[0:10] == '.ramb_tile'):
                x = int(line[11:].split()[0])
                y = int(line[11:].split()[1])
                self.tiles[y][x] = Tile('.ramb_tile', x, y)
                for j in range(16):
                    i += 1
                    self.tiles[y][x].setBitsRow(j, data[i])

            # RAMT Tile    
            if (line[0:10] == '.ramt_tile'):
                x = int(line[11:].split()[0])
                y = int(line[11:].split()[1])
                self.tiles[y][x] = Tile('.ramt_tile', x, y)
                for j in range(16):
                    i += 1
                    self.tiles[y][x].setBitsRow(j, data[i])
                
            i += 1
            if (i >= len(data)): break
            
            line = data[i]
            
        # Corner Tiles (No tiles)
        self.tiles[0][0] = Tile('NO', 0, 0)
        self.tiles[0][13] = Tile('NO', 13, 0)
        self.tiles[17][0] = Tile('NO', 0, 17)
        self.tiles[17][13] = Tile('NO', 13, 17)
        
    def writeFile(self, filename):

        with open(filename, "w") as f:
            
            f.write(str(self.comment) + "\n")
            f.write(str(self.device) + "\n")
            for rows in self.tiles:
                for tile in rows:
                    if (tile.getType() != 'NO'):
                        f.write (str(tile.getType()) + " " + str(tile.getKoordinates()[0]) + " " + str(tile.getKoordinates()[1]) + "\n")
                        bits = tile.getBits()
                        for line in bits:
                            f.write(str(line) + "\n")
                        
    def printTiles(self):
        # print out all tiles
        print (str(self.comment))
        print (str(self.device))
        for rows in self.tiles:
            for tile in rows:
                if (tile.getType() != 'NO'):
                    print (str(tile.getType()) + " " + str(tile.getKoordinates()[0]) + " " + str(tile.getKoordinates()[1]))
                    bits = tile.getBits()
                    for line in bits:
                        print(str(line))

    def getLutBitsAll(self, tile_x, tile_y, lut_nr):
        if (self.tiles[tile_y][tile_x].getType() != '.logic_tile'):
            return -1
        tile_bits = self.tiles[tile_y][tile_x].getBits()
        lut = (tile_bits[lut_nr * 2])[36:46] + (tile_bits[(lut_nr * 2) + 1])[36:46]
        return lut
    
    def printLutTable(self, tile_x, tile_y, lut_nr):
        lut = self.getLutBitsAll(tile_x, tile_y, lut_nr)
        lut_in_order = []
        for i in range(16):
#            lut_in_order.append(lut[self.lut_bit_order[i]])
 
#        print (lut_in_order)
            print ("%04s" % ((bin(i))[2:]) + " " + lut[self.lut_bit_order[i]])
        

    

