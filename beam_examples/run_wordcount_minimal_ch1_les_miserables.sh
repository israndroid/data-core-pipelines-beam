#!/bin/bash
# This script runs the wordcount_minimal.py script with the DirectRunner on the input file ch1_les_miserables.txt and outputs the results to word_counts_ch1_les_miserables.txt.
# It assumes that the input file is located in the ./tests/input directory and the output file will be saved in the ./tests/output directory. 
python wordcount_minimal.py --runner DirectRunner --input ./tests/input/ch1_les_miserables.txt --output ./tests/output/word_counts_ch1_les_miserables.txt