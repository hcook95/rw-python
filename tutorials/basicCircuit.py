"""
This tutorial shows how to make a simple design in RapidWright. Note
that this tutorial outputs a .dcp file. To get a bitstream one must
open the resulting .dcp file in Vivado and use the 'write_bitstream'
command.

This tutorial is based on Lesson1 of the RapidWright tutorial found
here: https://github.com/Xilinx/RapidWright/blob/master/src/com/xilinx/rapidwright/examples/Lesson1.java
"""

import jpype
import jpype.imports
from jpype.types import *

import os

fileDir = os.path.dirname(os.path.realpath(__file__))
print(fileDir)
os.chdir(fileDir+"/..")

jpype.startJVM(classpath=["rapidwright-2022.1.1-standalone-lin64.jar"])

from com.xilinx.rapidwright.device import *
from com.xilinx.rapidwright.design import *
from com.xilinx.rapidwright.rwroute import *
from com.xilinx.rapidwright.router import Router

# Create new design for PYNQ-Z1 board
deviceName = Device.PYNQ_Z1
design = Design("basicCircuit", deviceName)

# Create and place a 2-input OR gate at the C6LUT in the slice at 50x50y.
or2 = design.createAndPlaceCell("or2", Unisim.OR2, "SLICE_X50Y50/C6LUT")

# Place the two button IO buffers
button0 = design.createAndPlaceIOB("button0", PinType.IN, "D19", "LVCMOS33")
button1 = design.createAndPlaceIOB("button1", PinType.IN, "D20", "LVCMOS33")


# Place the led IO buffer
led = design.createAndPlaceIOB("led", PinType.OUT, "R14", "LVCMOS33")

# Create a net to connect the button0 buffer to one of the OR gate inputs
button0Net = design.createNet("button0Net")
button0Net.connect(button0, "O")
button0Net.connect(or2, "I0")

# Create a net to connect the button1 buffer to the other OR gate input
button1Net = design.createNet("button1Net")
button1Net.connect(button1, "O")
button1Net.connect(or2, "I1")


# Create a net to connect the output of the OR gate to the led
ledNet = design.createNet("ledNet")
ledNet.connect(or2, "O")
ledNet.connect(led, "I")

# Route the connections internal to the sites
design.routeSites()

# Use the basic router to route the design
router = Router(design)
router.routeDesign()

# Write the design out to a checkpoint
design.writeCheckpoint("checkpoints/basicCircuit.dcp")