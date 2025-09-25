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
version: {{pipe_config.version}}
pipeline_name: {{pipe_config.pipeline_name}}
-----------------
{% for stage in stages %}
    {{stage}}
{% endfor %}

-----------------
"""