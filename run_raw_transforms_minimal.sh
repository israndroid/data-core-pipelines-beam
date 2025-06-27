#!/bin/bash
python -m app.raw \
--runner DirectRunner \
--env DEV \
--input_bucket ./tests/input/ch1_les_miserables.txt \
--output_bucket ./tests/output/std_ch1_les_miserables.txt
