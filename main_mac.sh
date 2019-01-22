#! /usr/bin/env bash
echo "Image Handler starter"
cd ~/git/ImageHandler
conda --version
conda create -n pyqt
source activate pyqt
conda install python pyqt pylint pep8 flake8 yapf
conda install -c menpo opencv
python main.py
