#!/bin/bash
# Create subdirectories
mkdir data
mkdir data/training
mkdir data/training/spoken_descriptions
mkdir data/training/mermaid_code
mkdir data/test
mkdir data/test/spoken_descriptions
mkdir data/test/mermaid_code
mkdir src
mkdir tests

# Create empty files (optional)
touch src/__init__.py
touch ai.py
touch data_handler.py
touch dialog_manager.py  # Optional
touch mermaid_generator.py
touch nlu.py

# Create requirements file
touch requirements.txt

# Create script for clarity 
echo "# Edit this file to specify project dependencies" >> requirements.txt

echo "Project structure created"
