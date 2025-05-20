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

