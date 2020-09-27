#!/bin/bash

# Run Script for spread sequence

# Aaron Regan
# 27.09.2020

while true
do
	echo "Running with 40%"

	sudo python runtext.py -t 40%

	sudo python spreading-block.py --protected 40

	echo "Running with 55%"

	sudo python runtext.py -t 55%

	sudo python spreading-block.py --protected 55

	echo "Running with 70%"

	sudo python runtext.py -t 70%

	sudo python spreading-block.py --protected 70

	echo "Sequence Restart"
done

