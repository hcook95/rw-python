# RapidWright Python
This repository is used as a simple way to get started using RapidWright via Python3. 

RapidWright is written in Java, and as such is normally used in Java environments. 
However, setting up the RapidWright environment in Java can be cumbersome. 
Additionally many people (especially those first getting started with RapidWright) perfer Python to java, thus the makers of RapidWright have come out with a way to use the RapidWright API in a Python3 environment using JPype1.
The JPype1 Python library exposes Java APIs to Python as if they were native.

This repository packages the setup instrunctions found [here](https://www.rapidwright.io/docs/Install_RapidWright_as_a_Python_PIP_Package.html) into setup.py for convenience.
In addition, this repo contains a few tutorials written in Python to help new Python users get started.

## Getting Started

To setup the RapidWright environment, run `source setup.sh`.
The first time this script is ran, it will download, install, and setup everything needed for the RapidWright environment.
After the environment has been setup, one can enter the associated Python environment by running `source activate` in the top directory of the repository, however this is not reccomended.
Instead, it is recommended to recommended to run `source setup.sh` again, as this will also setup the necessary bash variables that are used by RapidWright's router.

As the [RapidWright for Python Instructions](https://www.rapidwright.io/docs/Install_RapidWright_as_a_Python_PIP_Package.html) state, you can run rapidwright.py in interactive mode by running `python -i rapidwright.py`.
This allows you to explore the various APIs. In addition, running this script in interactive mode will allow you to use tab-complete on the RapidWright Java Classes.

for example, after instatiating a AWS_F1 device with `device = Device.getDevice(Device.AWS_F1)`, one can tab complete `device.` to get the following:
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
Coming soon...
