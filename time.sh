#!bin/bash

# $1: number of samples

{ time python3 ./Kclause_Smarch/Smarch/smarch.py -o ~/git/t-wise/Data/Samples/Time ~/git/t-wise/Data/Financial_2018_05_09.dimacs $1 ; } 2>&1 | tee ./Data/Samples/Time/Financial_2018_05_09_$1.log
