"""
This tutorial shows how to use RapidWright to extract some basic
information of a device. While this example can be easily replicated
in Vivado using a couple tcl commands, it is often desirable to use 
RapidWright to get device information for the performance advantage
and ease of post processing in languages such as Java or Python.
"""

import jpype
import jpype.imports
from jpype.types import *

jpype.startJVM(classpath=["rapidwright-2022.1.1-standalone-lin64.jar"])

from com.xilinx.rapidwright.device import *
from com.xilinx.rapidwright.design import *

deviceName = "xc7z020iclg400-1L" # 7 Series Zynq chip
device = Device.getDevice(deviceName)


# gets all sites SLICEM sites
slices = device.getAllSitesOfType(SiteTypeEnum.SLICEM)

# put all BELs in all slices that are LUTs and check the length
numOfLUTs = len([bel for site in slices for bel in site.getBELs() if bel.isLUT()])
print(numOfLUTs)