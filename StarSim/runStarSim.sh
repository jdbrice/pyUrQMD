#!/bin/bash


# just for testing
echo "INPUT: " $1
echo "OUTPUT: " $2
echo "N EVENTS: " $3
echo "GEOMETRY: " $4
starsim -w 0 -b StarSim.kumac $1 $2 $3 $4