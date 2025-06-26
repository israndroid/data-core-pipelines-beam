#!/bin/bash
python -m app.raw \
--runner DirectRunner \
--env DEV \
--input ./tests/input/ch1_les_miserables.txt \
--output ./tests/output/std_word_counts_ch1_les_miserables.csv
