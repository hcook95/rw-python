if [ $(dpkg-query -W -f='${Status}' python3-venv 2>/dev/null | grep -c "ok installed") -eq 0 ];
then
  sudo apt install -y python3-venv;
fi

if [ ! -d "venv" ]
then
    echo "Creating Python venv..."
    python3 -m venv ../venv

    echo "export RAPIDWRIGHT_PATH='.'" >> ../venv/bin/activate #sets the rapidwright path to the current directory (used by RWRoute to find the timing file)
    echo "export CLASSPATH=\$RAPIDWRIGHT_PATH:$(echo \$RAPIDWRIGHT_PATH/jars/*.jar | tr ' ' ':')" >> ../venv/bin/activate

    echo "#!/bin/bash" >> ../activate
    echo "source ./venv/bin/activate" >> ../activate

    echo "Python venv successfully created."
fi

source ../venv/bin/activate

pip install -r requirements.txt

if [ ! -f ../rapidwright-2022.1.1-standalone-lin64.jar ]
then
    cd ..; wget https://github.com/Xilinx/RapidWright/releases/download/v2022.1.1-beta/rapidwright-2022.1.1-standalone-lin64.jar
fi