"""
version: 0.0.0-dev
pipeline_name: pipe_raw_to_std_real_state
-----------------

    {'order': 1, 'stage_id': 'step-01-read_raw_real_state', 'stage_name': 'read_raw_real_state', 'stage_type': 'source', 'module': 'src.modules.io_transforms', 'source_class': 'ReadCSVSource', 'input_pcollection': None, 'output_pcollection': 'raw_real_state_data', 'params': {'file_path': '/data/raw/real_state_data.csv', 'delimiter': ',', 'header': True}}

    {'order': 2, 'stage_id': 'step-02-raw_to_std_real_state', 'stage_name': 'raw_to_std_real_state', 'stage_type': 'transform', 'module': 'src.modules.raw_transforms', 'transform_class': 'StandarizeCSV', 'params': {'field_mapping': {'address': 'property_address', 'price': 'listing_price', 'bedrooms': 'num_bedrooms', 'bathrooms': 'num_bathrooms', 'area': 'property_area', 'listing_date': 'date_listed'}}}

    {'order': 3, 'stage_id': 'step-03-raw_to_std_real_state', 'stage_name': 'raw_to_std_real_state', 'stage_type': 'transform', 'module': 'src.modules.raw_transforms', 'transform_class': 'StandarizeCSV', 'params': {'field_mapping': {'address': 'property_address', 'price': 'listing_price', 'bedrooms': 'num_bedrooms', 'bathrooms': 'num_bathrooms', 'area': 'property_area', 'listing_date': 'date_listed'}}}


-----------------
"""


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

def setup_options(argv=None, save_main_session=True):
    parser = argparse.ArgumentParser()
    parser.add_argument('--runner', dest='runner', default='DirectRunner', choices=['DirectRunner', 'DataflowRunner'], help='Runner to use for the pipeline')
    parser.add_argument('--env', dest='environment', default='DEV',choices=GC.ENV_OPTIONS, help=f'Environment to run the pipeline ({GC.ENV_DEV}: Local, {GC.ENV_PROD}: pre-prod environment (Example: test at DataFlowRunner), {GC.ENV_PROD}: Production environment)')
    parser.add_argument('--input_bucket', dest='input_bucket', required=True, help='Path to read RAW file')
    parser.add_argument('--output_bucket', dest='output_bucket', required=True, help='Path to write STANDARIZED file') 
    parser.add_argument('--transforms', dest='transforms', default=['IOReadFromText', 'StandarizeHeader', 'IOWriteToText'], help='Raw transform to apply on the input data')
    parser.add_argument('--date_calc', dest='date_calc', default=datetime.now().strftime('%Y-%m-%d'), help='Date to calculate the data (default: yesterday)')

    know_args, pipeline_args = parser.parse_known_args()
    pipeline_options = PipelineOptions(pipeline_args)
    pipeline_options.view_as(SetupOptions).save_main_session = save_main_session
    return know_args, pipeline_options

def main(pipeline_options, args, date_calc):
    if args.environment == GC.ENV_DEV:
        logging.info(f'Running in {GC.ENV_DEV} environment')
    elif args.environment == GC.ENV_UAT:    
        logging.info(f'Running in {GC.ENV_UAT} environment')
    elif args.environment == GC.ENV_PROD:
        logging.info(f'Running in {GC.ENV_PROD} environment')
    
    logging.info(f'Pipeline options parsed: {pipeline_options}')
    logging.info(f'Args parsed: {args}')

    with beam.Pipeline(options=pipeline_options) as p:
        logging.info(f'Transforms to apply: {args.transforms}')
        #pcol_transform_applied = [p]
        """ for transform in args.transforms:
            logging.info(f'Applying transform: {transform}')
            pcol_transform_applied.append(
                pcol_transform_applied[i] | transform(
            ) """
        prefix_step = 'Step 01 - Read, Transform and Write to Text'
        header = raw_transforms.read_first_line_from_file(args.input_bucket)
        std_header = raw_transforms.sanitize_header(header, to_lower_case=True)
        pcol_transform_applied = (p
            | f'{prefix_step} - IOReadFromText' >> io_transforms.IOReadFromText(input_bucket=args.input_bucket)
            | f'{prefix_step} - SplitRawLineToDict' >> raw_transforms.SplitRawLineToDict(
                header=std_header,
                delimiter=',',
                to_sanitize_header=False,  # We already sanitized the header
                to_lower_case=True,
                tag='SplitRawLineToDict'
            )
            | f'{prefix_step} - dict_to_row_concat' >> beam.Map(lambda row: raw_transforms.dict_to_row_concat(row, delimiter=','))
            #| 'SelectRenamedCreateIfNotExists' >> SelectRenamedCreateIfNotExists() #TODO: Implement this transform
            | f'{prefix_step} - IOWriteToText' >> io_transforms.IOWriteToText(output_bucket=args.output_bucket, header=std_header, file_name_suffix='.txt')
        )

    

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    know_args, pipeline_options = setup_options(argv=None, save_main_session=True)

    start_time = time.time()
    print(f'[start_time: {start_time}] Starting the pipeline... raw.py -> main()')
    
    main(pipeline_options=pipeline_options, args=know_args, date_calc=know_args.date_calc)
    end_time = time.time()

    print(f'[end_time: {end_time}] Ending the pipeline... raw.py -> main()')