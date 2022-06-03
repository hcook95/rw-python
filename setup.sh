if [ $(dpkg-query -W -f='${Status}' python3-venv 2>/dev/null | grep -c "ok installed") -eq 0 ];
then
  sudo apt install python3-venv;
fi

if [ ! -d "venv" ]
then
    echo "Creating Python venv..."
    python3 -m venv venv

    echo "export RAPIDWRIGHT_PATH='../..'" >> venv/bin/activate
    echo "export CLASSPATH=\$RAPIDWRIGHT_PATH:$(echo \$RAPIDWRIGHT_PATH/jars/*.jar | tr ' ' ':')" >> venv/bin/activate


    echo "Python venv successfully created."
fi

source venv/bin/activate

if [ $(pip show JPype1 2>&1 >/dev/null | grep -c "WARNING: Package(s) not found:") -eq 1 ]
then
    pip install JPype1
fi

if [ $(pip show matplotlib 2>&1 >/dev/null | grep -c "WARNING: Package(s) not found:") -eq 1 ]
then
    pip install matplotlib
fi

if [ $(pip show pyqt5 2>&1 >/dev/null | grep -c "WARNING: Package(s) not found:") -eq 1 ]
then
    pip install pyqt5
fi

if [ ! -f rapidwright-2022.1.1-standalone-lin64.jar ]
then
    wget https://github.com/Xilinx/RapidWright/releases/download/v2022.1.1-beta/rapidwright-2022.1.1-standalone-lin64.jar
fi

# SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]:-$0}"; )" &> /dev/null && pwd 2> /dev/null; )";
# export RAPIDWRIGHT_PATH=$SCRIPT_DIR

# export CLASSPATH=$RAPIDWRIGHT_PATH:$(echo $RAPIDWRIGHT_PATH/jars/*.jar | tr ' ' ':')

# python -i rapidwright.py
