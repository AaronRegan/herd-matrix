#!/bin/bash

# Kill Script for spread sequence

# Aaron Regan
# 27.09.2020

sudo kill $(ps aux | grep spread_run | grep -v  grep | awk '{ print $2 }')

echo "Sequence Shutdown"