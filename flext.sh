#!/bin/bash

# flext launch script to bring in the venv with everything loaded

# make sure the libs are installed before launching

LIBS="PyQt6"

pip list |grep ${LIBS} > /dev/null

if [ $? -ne 0 ]; then
	echo "You need PyQt6 to run this. Should it be installed ?"
	read ans
	if [ $ans = "y" -o $ans = "Y" ]; then
		pip3 install PyQt6 2>/dev/null
		if [ $? -ne 0 ]; then
			echo "Sorry, pip3 failed to install ${LIBS}"
			exit 1
		fi
	else
		echo "Exiting."
		exit 0
	fi
fi

# flext has PyQt6, so continue
nohup python3 ${PWD}/flext.py >/dev/null 2>&1 &
