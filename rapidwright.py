import jpype
import jpype.imports
from jpype.types import *

jpype.startJVM(classpath=["rapidwright-2022.1.1-standalone-lin64.jar"])

from com.xilinx.rapidwright.device import *
from com.xilinx.rapidwright.design import *
from com.xilinx.rapidwright.rwroute import *