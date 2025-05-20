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
# Create Requirement
pip freeze
```

