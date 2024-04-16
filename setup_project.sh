#!/bin/bash

# Define project base path
BASE_PATH="./MermaidAutogenAgent"

# Create directories
echo "Creating project directories..."
mkdir -p $BASE_PATH/app
mkdir -p $BASE_PATH/config
mkdir -p $BASE_PATH/scripts
mkdir -p $BASE_PATH/data
mkdir -p $BASE_PATH/tests
mkdir -p $BASE_PATH/docs

# Create files in their respective directories
echo "Creating initial project files..."
touch $BASE_PATH/app/__init__.py
touch $BASE_PATH/app/main.py
touch $BASE_PATH/app/dependencies.py
touch $BASE_PATH/app/diagrams.py

touch $BASE_PATH/config/config.yaml

touch $BASE_PATH/scripts/upload_to_s3.py
touch $BASE_PATH/scripts/download_from_s3.py
touch $BASE_PATH/scripts/manage_cron.py

touch $BASE_PATH/data/.gitignore  # To ensure data isn't tracked by git

touch $BASE_PATH/tests/__init__.py
touch $BASE_PATH/tests/test_config.py
touch $BASE_PATH/tests/test_generation.py

touch $BASE_PATH/docs/index.md

touch $BASE_PATH/.env
touch $BASE_PATH/.gitignore
echo "/data/" > $BASE_PATH/.gitignore
echo "/venv/" >> $BASE_PATH/.gitignore
echo "*.pyc" >> $BASE_PATH/.gitignore
echo "__pycache__/" >> $BASE_PATH/.gitignore
echo ".aider*" >> $BASE_PATH/.gitignore

echo "/venv/" > .gitignore
echo "*.pyc" >> .gitignore
echo "__pycache__/" >> .gitignore
echo ".aider*" >> .gitignore

touch $BASE_PATH/README.md
touch $BASE_PATH/requirements.txt
touch $BASE_PATH/setup.py
touch $BASE_PATH/Makefile

echo "Project directory structure is set up."
