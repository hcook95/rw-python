"""
RWRoute is a new open-source, timing-based router written
in RapidWright. It provides a substantial speedup to routing 
when compared to Vivado's router, with a sacrifice in the 
critical path delay. This may be useful for applications such 
as quick design iterations.

This program not as much of a tutorial as much as it 
is a simple wrapper over the RWRouter main function. To use
simply run 'python rwroute <input.dcp> <output.dcp>'.
Note that RWRoute currently only works with UltraScale+
devices.

This file also contains the code of RWRoute.main() converted 
from Java into Python. This code is commented out, and can be 
used to understand and manipulate the main function of RWRoute.
"""
from os import RWF_HIPRI
import sys
import jpype
import jpype.imports
from jpype.types import *

import os

fileDir = os.path.dirname(os.path.realpath(__file__))
os.chdir(fileDir+"/..")

jpype.startJVM(classpath=["rapidwright-2022.1.1-standalone-lin64.jar"])

from com.xilinx.rapidwright.rwroute import *

RWRoute.main(sys.argv[1:])


###############################################################
# The following commented code is RWRoute.main converted into #
# python. This may be useful if one wants to play around with #
# the code.                                                   #
###############################################################

# from com.xilinx.rapidwright.tests import CodePerfTracker
# from com.xilinx.rapidwright.design import Design

# if (len(sys.argv) < 3):
#     print("USAGE: <input.dcp> <output.dcp> [options]")
#     exit(-1)

# t = CodePerfTracker("rwroute", True)

# #Reads in a design checkpoint
# unroutedDesign = Design.readCheckpoint(sys.argv[1])
# #Routes design checkpoint
# routedDesign = RWRoute.routeDesignWithUserDefinedArguments(unroutedDesign, sys.argv)

# routedDesign.writeCheckpoint(sys.argv[2], t)
# print("\nINFO: Write routed design\n " + sys.argv[2] + "\n")