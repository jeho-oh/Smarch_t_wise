#!bin/bash

# $1: number of samples

cd ..
{ time python3 ./Kclause_Smarch/Smarch/smarch.py -o ~/git/t-wise/Financial_2018_05_09/Samples/Time ~/git/t-wise/Financial_2018_05_09/Financial_2018_05_09.dimacs $1 ; } 2>&1 | tee ./Financial_2018_05_09/Samples/Time/Financial_2018_05_09_$1.log
