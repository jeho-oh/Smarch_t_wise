These directory lists the scripts used for data collection and analysis.

For the data collection, we used an existing tool Smarch, 
and provided bash scripts (time.sh, meomory.sh) so that 
anyone can run the tool for the given feature model and 
get configurations, sample time, and memory usage.

We also provided python scripts for each analysis, where:
  - combination.py: get all valid t-wise combinations;
  - coverage.py: get t-wise coverage of the samples;
  - ratio.py: derive config. ratio for each combination; and
  - estimation.py: estimate the t-wise coverage.
Simply running each script in this order allows getting all 
the data that are represented in the paper.

While our paper is targeted for a given feature model, 
users can try different models by simply modifying the 
input dimacs file path in the scripts.

