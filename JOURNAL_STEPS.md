# data-core-pipelines-beam
A TDD core project to develop Apache Beam with Python SDK

# Current Steps to create this repo

1. Create Venv
```
# Create Venv
python -m venv /path/to/directory

# Activate venv
. /path/to/directory/bin/activate
```
2. Full list installs applied

```
# Install Apache Beam for local
pip install apache-beam

# Install Apache Beam for GCP
pip install wheel
pip install 'apache-beam[gcp]'
pip install --upgrade 'apache-beam[gcp]'
```

3. Created requirements.txt from current venv
```
# Create Requirements
pip freeze > requirements.txt
```

4. Install requirements.txt
```
# Install Requirements
pip install -r requirements.txt
```

5. Example: to Run wordcount_minimal.py with DirectRunner
From Examples:https://github.com/apache/beam/tree/master/sdks/python/apache_beam/examples
- Word count minimal: https://github.com/apache/beam/blob/master/sdks/python/apache_beam/examples/wordcount_minimal.py
- Word count minimal test: https://github.com/apache/beam/blob/master/sdks/python/apache_beam/examples/wordcount_minimal_test.py
```
# Run Direct Runner
python wordcount_minimal.py --runner DirectRunner --input ./test/input/ch1_les_miserables.txt --output ./test/output/word_counts_ch1_les_miserables.txt
```

6. Config base project (app, src, test ... setup.py, etc.).

    6.1 Local Flow: Will be able to run dataflow jobs. The base project will be can run Apache Beam pipelines in local with DirectRunner, and triggered by Airflow Dags in local env (or an Dockerized Dev Environment).

    6.2 The Cloud aproach (GCP): Using Airflow at Compute Engine, run Apache Beam Pipelines triggered by Airflow in a preemptible vm.

    Reference Doc for deploy in GCP:
    - Compute Engine:
    - Airflow in GCP: https://cloud.google.com/blog/products/data-analytics/different-ways-to-run-apache-airflow-on-google-cloud
    - Check terraform, for deploy scpecific free Tier for test at GCP. 
    




