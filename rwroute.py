"""
This program is a simple wrapper over RWRouter. To use
simply run 'python rwroute <input.dcp> <output.dcp>'.
Note that RWRoute currently only works with UltraScale+
devices.
"""
from os import RWF_HIPRI
import sys
import jpype
import jpype.imports
from jpype.types import *

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