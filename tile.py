class Tile:
        
    def __init__(self, tiletype, x, y):
        self.tiletype = tiletype
        self.x = x
        self.y = y
        self.bits = [0 for i in range(16)]            
        
    # returns the tiletype as string
    def getType(self):
        return self.tiletype
    
    # returns the x- and y-koordinates as tupel
    def getKoordinates(self):
        return (self.x, self.y)
    
    # returns the bits-array from this tile (16 rows)
    def getBits(self):
        return self.bits
    
    # sets the bits of bits[row] as a string. Row has to be 0..15
    def setBitsRow(self, row, bits):
        self.bits[row] = bits
