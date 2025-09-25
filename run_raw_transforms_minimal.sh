#!/bin/bash
python -m app.raw \
--runner DirectRunner \
--env DEV \
--input_bucket "./tests/data-core-project-landing-zone/data_lake_core_web_scrapper/raw/cl_real_state/2023-03-08 Precios Casas RM.csv" \
--output_bucket ./tests/data-core-project-landing-zone/data_lake_core_web_scrapper/standarized/cl_real_state/std_precios_casas_rm_20230308_v2.csv
