echo "Image Handler starter"
conda --version
activate base
conda create -n pyqt 
source activate pyqt
conda install python pyqt pylint pep8 flake8 yapf
python main.py
pause
