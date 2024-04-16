# Makefile for MermaidAutogenAgent

# Dynamically set the virtual environment name based on the directory name
VENV := $(notdir $(CURDIR))
CONDA_ACTIVATE := source $$(conda info --base)/etc/profile.d/conda.sh ; conda activate $(VENV)
PYTHON := $(CONDA_ACTIVATE) ; python
UVICORN := $(CONDA_ACTIVATE) ; uvicorn
APP := app.main:app

# Set the default target to help when just typing 'make'
.DEFAULT_GOAL := help

.PHONY: help
help:
	@echo "------------------------- HELP -------------------------"
	@echo "To use this Makefile, use one of the following commands:"
	@echo "make setup: Setup the Python virtual environment and install dependencies."
	@echo "make run: Run the FastAPI application."
	@echo "make test: Run tests using pytest."
	@echo "make clean: Remove all temporary files and the virtual environment."
	@echo "make s3Sync: Sync data directory to AWS S3."
	@echo "make downloadFromS3: Download data directory from AWS S3."
	@echo "make installCron: Install cron job for S3 data sync."
	@echo "-------------------------------------------------------"

.PHONY: setup
setup:
	@conda env list | grep $(VENV) > /dev/null || conda create -y -n $(VENV) python=3.11 pip pre-commit
	$(CONDA_ACTIVATE) ; pip install -r requirements.txt

.PHONY: run
run:
	@conda env list | grep $(VENV) > /dev/null || $(MAKE) setup
	$(UVICORN) $(APP) --reload --host 0.0.0.0 --port 8000

.PHONY: test
test:
	$(PYTHON) -m pytest

.PHONY: clean
clean:
	@conda env remove -n $(VENV)
	@find . -type f -name '*.pyc' -delete
	@find . -type d -name '__pycache__' -delete
	@echo "Cleaned up."

.PHONY: s3Sync
s3Sync:
	@$(PYTHON) scripts/upload_to_s3.py
	@echo "Data synced to S3."

.PHONY: downloadFromS3
downloadFromS3:
	@$(PYTHON) scripts/download_from_s3.py
	@echo "Data downloaded from S3."

.PHONY: installCron
installCron:
	@$(PYTHON) scripts/manage_cron.py
	@echo "Cron job installation script executed."
