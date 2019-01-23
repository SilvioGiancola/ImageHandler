#! /usr/bin/env bash
echo "Image Handler starter"
cd $( dirname "${BASH_SOURCE[0]}" )
conda --version
# source deactivate
# conda remove --name pyqt --all
conda create -n pyqt python lxml pylint pep8 flake8 yapf
source activate pyqt 
conda install -c menpo opencv
pip install PyQt5
echo "Run Image Handler"
python main.py
echo "Build Image Handler"
pip install pyinstaller
# conda env export > env_mac.yml
# rm -r dist
# rm -r build
# rm main.spec
pyinstaller -F main.py
./dist/main
