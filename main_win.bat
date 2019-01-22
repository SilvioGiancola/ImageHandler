echo "Image Handler starter"
call conda --version
call conda create -n pyqt 
call activate pyqt
call conda install python pyqt pylint pep8 flake8 yapf lxml opencv
python main.py
PAUSE
