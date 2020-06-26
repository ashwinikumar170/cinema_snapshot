#!/bin/bash
ls $1 &> files.txt
python cleaner.py
python API_call.py
rm -f files.txt
rm -f clean.txt
