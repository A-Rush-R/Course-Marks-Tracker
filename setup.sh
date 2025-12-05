#!/bin/bash

python3 -m venv .venv

source .venv/bin/activate

pip install --upgrade pip
pip install xlsxwriter
pip install openpyxl

echo "------------------------------------------------"
echo "Environment created and dependencies installed."
echo "To use it, run: source venv/bin/activate"
echo "------------------------------------------------"

