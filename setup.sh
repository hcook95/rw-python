if [ $(dpkg-query -W -f='${Status}' python3-venv 2>/dev/null | grep -c "ok installed") -eq 0 ];
then
  sudo apt install python3-venv;
fi

if [ ! -d "venv" ]
then
    python3 -m venv venv
fi

source venv/bin/activate
pip install JPype1

if [ ! -f rapidwright-2022.1.1-standalone-lin64.jar ]
then
    wget https://github.com/Xilinx/RapidWright/releases/download/v2022.1.1-beta/rapidwright-2022.1.1-standalone-lin64.jar
fi

python -i rapidwright.py
