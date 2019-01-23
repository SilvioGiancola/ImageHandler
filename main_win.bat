echo "Image Handler starter"
call conda --version
REM call deactivate
REM call conda remove --name pyqt --all
call conda create -n pyqt python lxml pylint pep8 flake8 yapf opencv
call activate pyqt
pip install PyQt5
python main.py
REM PAUSE
pip install pyinstaller
REM call conda env export > env_win.yml
REM rm -r dist
REM rm -r build
REM rm main.spec
pyinstaller -F main.py
start dist/main
PAUSE