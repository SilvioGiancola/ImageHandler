echo "Image Handler starter"
conda --version
activate base
conda create -n pyqt python pyqt
conda install opencv
python main.py
pause