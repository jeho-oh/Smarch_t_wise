#!bin/bash

# $1: number of samples

{ time python3 ./Kclause_Smarch/Smarch/smarch_mp.py -o ~/git/t-wise/Data/Samples -p 7 ~/git/t-wise/Data/Financial_2018_05_09.dimacs $1 ; } 2>&1 | tee ./Data/Samples/Financial_2018_05_09_$1.log
