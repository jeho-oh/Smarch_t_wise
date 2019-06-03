# Smarch_t_wise

This is the repository for SPLC 2019 challenge solution paper: "t-wise Coverage by Uniform Sampling"

Abstract:

A gigantic configuration space has over a trillion (10^12) configurations. Efficiently testing gigantic configuration spaces of Software Product Lines(SPLs) requires a sampling algorithm that is both scalable and provides good t-wise coverage. The 2019 SPLC Sampling Challenge provides real-world gigantic feature models and asks for a t-wise sampling algorithm that can work for those models. 

We evaluate t-wise coverage with one of the provided gigantic feature models using the Smarch algorithm, that uniformly samples SPL configurations.  While uniform sampling alone is not enough to produce 100% 1-wise and 2-wise coverage, we use standard probabilistic analysis to explain our experimental results and to conjecture how uniform sampling may enhance the scalability of existing t-wise sampling algorithms.

## Repository structure

This repository has following structure.

* Financial_2018_05_09: Data and results for FinancialServices01 product line, version 2018_05_09
* Kclause_Smarch: Repository for the Smarch sampling tool
* src: Source code used for evaluation

Further details are in the README.md file of each directory.
