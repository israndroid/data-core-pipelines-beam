import os
from jinja2 import Environment, FileSystemLoader


max_score = 100
test_name = "Python Challenge"
students = [
    {"name": "Sandrine",  "score": 100},
    {"name": "Gergeley", "score": 87},
    {"name": "Frieda", "score": 92}
]

pipeline_config_template = {
    "version": "0.0.0-dev",
    "pipeline_type": "beam",
    "pipeline_id": "pipe_raw_to_std_real_state",
    "pipeline_name": "pipe_raw_to_std_real_state",
    "description": "Pipeline to transform raw real estate data into example standardized ingest format",
    "stages": [
        {
            "order": 1,
            "stage_id": "step-01-read_raw_real_state",
            "stage_name": "read_raw_real_state",
            "stage_type": "source",
            "module": "src.modules.io_transforms",
            "source_class": "ReadCSVSource",
            "input_pcollection": None,
            "output_pcollection": "raw_real_state_data",
            "params": {
                "file_path": "/data/raw/real_state_data.csv",
                "delimiter": ",",
                "header": True
            }
        },
        {
            "order": 2,
            "stage_id": "step-02-raw_to_std_real_state",
            "stage_name": "raw_to_std_real_state",
            "stage_type": "transform",
            "module": "src.modules.raw_transforms",
            "transform_class": "StandarizeCSV",
            "params": {
                "field_mapping": {
                    "address": "property_address",
                    "price": "listing_price",
                    "bedrooms": "num_bedrooms",
                    "bathrooms": "num_bathrooms",
                    "area": "property_area",
                    "listing_date": "date_listed"
                }
            }
        },
        {
            "order": 3,
            "stage_id": "step-03-raw_to_std_real_state",
            "stage_name": "raw_to_std_real_state",
            "stage_type": "transform",
            "module": "src.modules.raw_transforms",
            "transform_class": "StandarizeCSV",
            "params": {
                "field_mapping": {
                    "address": "property_address",
                    "price": "listing_price",
                    "bedrooms": "num_bedrooms",
                    "bathrooms": "num_bathrooms",
                    "area": "property_area",
                    "listing_date": "date_listed"
                }
            }
        }
    ]
} 

environment = Environment(loader=FileSystemLoader("app/pipelines_templates/"))
template = environment.get_template("raw_template.py")
pipeline_builder_output_path = "builded_pipelines/"
os.makedirs(pipeline_builder_output_path, exist_ok=True)

filename = f"raw_pipe_real_state.py"
stages = pipeline_config_template.get('stages', []) 
if stages != []:
    content = template.render(
        pipe_config=pipeline_config_template,
        stages=stages
    )
else:
    print("stage is None, skipping...")
with open(f'{pipeline_builder_output_path}{filename}', mode="w", encoding="utf-8") as message:
    message.write(content)
    print(f"... wrote {filename}")