# hx1k_manipulator
Python tools for manipulating the Lattice ICE40-HX1K Bitstream.
## 1. Description
The tools in this repository manipulate .asc files from the opensource-toolchain yosys, arachne-pnr and icestorm (by Clifford Wolf, [Link to project icestorm](http://www.clifford.at/icestorm). These .asc files are a direct representation of a FPGA-bitstream (.bin) after synthesising, placing and routing. 

h1xk-manipulator is work-in-progress and far from beeing stable. Be aware that you can easily destroy your FPGA with these tools. There are no build in checks for saving the FPGA. All the bit-manipulations work directly on the flashable bitstream.

## 2. Features
* Works with Lattice ICE40 HX1K FPGAs, tested on Lattice IceStick
* Load an .asc file from the asc/ directory
* Write an .asc file to the asc/ directory
* Display the status of LUTs in all Tiles
* Display the status of all LUTs in one chooseable Tile
* Display and modify one chooseable LUT in one chooseable Tile

## 3. Prerequisites
* Python 3

* Packages that should already be included in your python: 
  * os
  * io
  * subprocess

* Packages to be installed in python: 
  * click (pip install click)

* For working with the example on the Lattice IceStick: 
  * yosys
  * arachne-pnr
  * icestorm
 
## 4. Usage

## 5. Example

