#!/bin/sh

# check overlap (2.0 A) excluding next 20 atoms in file order from the check
python ../source/main.py -i solution.gro -t "overlap" -e 20 -th 2.0
