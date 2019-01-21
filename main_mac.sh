#! /usr/bin/env bash
cd ~/git/ImageHandler
conda env create --file env_mac.yml
source activate pyqt
python main.py