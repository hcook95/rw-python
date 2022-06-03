# RapidWright Python
This repository provides a simple way to get started using RapidWright via Python3. 

RapidWright is written in Java, and as such is normally used in Java environments. 
However, setting up the RapidWright environment in Java can be cumbersome. 
Additionally many people (especially those first getting started with RapidWright) prefer Python to java, thus the makers of RapidWright have come out with a way to use the RapidWright API in a Python3 environment using JPype1.
The JPype1 Python library exposes Java APIs to Python as if they were native.

This repository packages the setup instructions found [here](https://www.rapidwright.io/docs/Install_RapidWright_as_a_Python_PIP_Package.html) into a setup.sh script for convenience.
In addition, this repository contains a few tutorials written in Python3 to help new users get started.

## Getting Started

Before getting started with this 

To setup the RapidWright environment, run `source setup.sh`, which will download, install, and setup everything needed for the RapidWright environment.
After the environment has been setup, one can enter the associated Python environment by running `source venv/bin/activate`.

As the [RapidWright for Python Instructions](https://www.rapidwright.io/docs/Install_RapidWright_as_a_Python_PIP_Package.html) state, you can run rapidwright.py in interactive mode by running `python -i rapidwright.py`.
This allows you to explore the various APIs. In addition, running this script in interactive mode will allow you to use tab-complete on the RapidWright Java Classes.

for example, after instantiating a AWS_F1 device with `device = Device.getDevice(Device.AWS_F1)`, one can tab complete `device.` to get the following:
```
>>> device.
device.AWS_F1                         device.getClass(                      device.getSLRByConfigOrderIndex(
device.DEVICE_FILE_VERSION            device.getClockRegion(                device.getSLRs(
device.FRAMEWORK_NAME                 device.getClockRegionFromTile(        device.getSeries(
device.FRAMEWORK_NAME_AND_VERSION     device.getClockRegions(               device.getSite(
device.KCU105                         device.getColumns(                    device.getSiteFromPackagePin(
device.PYNQ_Z1                        device.getDevice(                     device.getSitePin(
device.QUIET_MESSAGE                  device.getDeviceName(                 device.getSiteTypeCount(
device.RAPIDWRIGHT_MINOR_VERSION      device.getDeviceVersion(              device.getTile(
device.RAPIDWRIGHT_QUARTER_VERSION    device.getFamilyType(                 device.getTileTypeCount(
device.RAPIDWRIGHT_VERSION            device.getMasterSLR(                  device.getTiles(
device.RAPIDWRIGHT_YEAR_VERSION       device.getName(                       device.getWire(
device.RW_QUIET_MESSAGE               device.getNode(                       device.hashCode(
device.a(                             device.getNumOfClockRegionRows(       device.notify(
device.equals(                        device.getNumOfClockRegionsColumns(   device.notifyAll(
device.getActivePackage(              device.getNumOfSLRs(                  device.quietReflectiveAccessWarning(
device.getAllCompatibleSites(         device.getPIP(                        device.releaseDeviceReferences(
device.getAllSitesOfType(             device.getPackage(                    device.setActivePackage(
device.getAllTiles(                   device.getPackages(                   device.toString(
device.getArchitecture(               device.getRows(                       device.wait(
device.getAvailableDevices(           device.getSLR(
>>> device.
```

## Tutorials

### numOfMemLUTs
This tutorial shows how to use RapidWright to extract some basic
information of a device. While this example can be easily replicated
in Vivado using a couple tcl commands, it is often desirable to use 
RapidWright to get device information for the performance advantage
and ease of post processing in languages such as Java or Python.

### netSizes
This tutorial shows how to use RapidWright to extract some basic
information of a design. It also does some post-processing (plotting
the info in matplotlib) to show some of the advantages of using
RapidWright with Python.

### basicCircuit
This tutorial shows how to make a simple design in RapidWright. Note
that this tutorial outputs a .dcp file. To get a bitstream one must
open the resulting .dcp file in Vivado and use the 'write_bitstream'
command.

This tutorial is based on Lesson1 of the RapidWright tutorial found
here: https://github.com/Xilinx/RapidWright/blob/master/src/com/xilinx/rapidwright/examples/Lesson1.java

### rwroute
RWRoute is a new open-source router written in RapidWright.
It provides a substantial speedup to routing when
compared to Vivado's router, with the sacrifice of timing.
This may be useful for applications such as quick design iterations.

This program not as much of a tutorial as much as it is a simple wrapper over RWRouter. To use
simply run 'python rwroute <input.dcp> <output.dcp>'.
Note that RWRoute currently only works with UltraScale+
devices.
