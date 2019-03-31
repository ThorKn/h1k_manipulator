class iceconfig:

    # Konstruktor, leer
    def __init__(self):

    # Clear the whole chip
    def clear(self):

    # Setup an empty HX1K chip
    # Init:
    # self.ramb_tiles[(x, y)]    (dictionary)
    # self.ramt_tiles[(x, y)]    (dictionary)
    # self.logic_tiles[(x, y)]   (dictionary)
    # self.io_tiles[(x, y)]      (dictionary)
    # Set all Bits in all tiles to "0"
    def setup_empty_1k(self):

    # Same Setup for HX8K chip
    def setup_empty_8k(self):

    # ???
    def lookup_extra_bit(self, bit):

    # Lookup for x-y-tile
    # Returns the full self.(io, logic, ramb, ramt)_tile     (dictionary)
    def tile(self, x, y):

    # Returns an array of all IO-Pins
    # [(pin_nr, tile_x, tile_y, pin_tile_nr), (...), ...] 
    def pinloc_db(self):

    # ???
    def gbufin_db(self):

    # ???
    def iolatch_db(self):

    # ???
    def padin_pio_db(self):

    # ???
    def extra_bits_db(self):

    # ???
    def ieren_db(self):

    # ???
    def pll_list(self):

    # ???
    def colbuf_db(self):

    # ???
    def tile_db(self, x, y):








