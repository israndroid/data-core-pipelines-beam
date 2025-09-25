import argparse
from datetime import datetime, timedelta
import logging
import time
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import SetupOptions
from src.modules import raw_transforms
from src.modules import io_transforms
from config import global_config as GC

"""
version: 0.0.0-dev
pipeline_name: pipe_raw_to_std_real_state
-----------------

    {'order': 1, 'stage_id': 'step-01-read_raw_real_state', 'stage_name': 'read_raw_real_state', 'stage_type': 'source', 'module': 'src.modules.io_transforms', 'source_class': 'ReadCSVSource', 'input_pcollection': None, 'output_pcollection': 'raw_real_state_data', 'params': {'file_path': '/data/raw/real_state_data.csv', 'delimiter': ',', 'header': True}}

    {'order': 2, 'stage_id': 'step-02-raw_to_std_real_state', 'stage_name': 'raw_to_std_real_state', 'stage_type': 'transform', 'module': 'src.modules.raw_transforms', 'transform_class': 'StandarizeCSV', 'params': {'field_mapping': {'address': 'property_address', 'price': 'listing_price', 'bedrooms': 'num_bedrooms', 'bathrooms': 'num_bathrooms', 'area': 'property_area', 'listing_date': 'date_listed'}}}

    {'order': 3, 'stage_id': 'step-03-raw_to_std_real_state', 'stage_name': 'raw_to_std_real_state', 'stage_type': 'transform', 'module': 'src.modules.raw_transforms', 'transform_class': 'StandarizeCSV', 'params': {'field_mapping': {'address': 'property_address', 'price': 'listing_price', 'bedrooms': 'num_bedrooms', 'bathrooms': 'num_bathrooms', 'area': 'property_area', 'listing_date': 'date_listed'}}}


-----------------
"""