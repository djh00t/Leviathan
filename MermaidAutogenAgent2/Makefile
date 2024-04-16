# Target to install all dependencies

install:  # Correcting indentation to use tabs instead of spaces
	@echo "Installing dependencies..."
	@pip install -r requirements.txt

# Target to clean the project (remove build artifacts)

clean:
	@echo "Cleaning project..."
	@find . -type d -name "__pycache__" -exec rm -r {} +
	@rm -rf build *.egg-info

# Target to build the project (optional, not strictly necessary for Python projects)

build:  # Correcting indentation to use tabs instead of spaces
	@echo "Building project..."
	@mkdir -p build  # Create a build directory if it doesn't exist

# Target to run unit tests

test:  # Correcting indentation to use tabs instead of spaces
	@echo "Running unit tests..."
	@pytest tests/

# Target to run the application (assuming the main entry point is api/main.py)

run:  # Correcting indentation to use tabs instead of spaces
	@echo "Starting the application..."
	@uvicorn api.main:app --host 0.0.0.0 --port 8000  # Adjust host and port as needed

# Target to run tests with code coverage report

test-coverage:  # Correcting indentation to use tabs instead of spaces
	@echo "Running unit tests with coverage..."
	@pytest tests/ --cov=core --cov-report=html

# Target to lint the code (optional)

lint:  # Correcting indentation to use tabs instead of spaces
	@echo "Linting code..."
	@flake8 .

# Target to create Docker image (optional)

docker-build:  # Correcting indentation to use tabs instead of spaces
	@echo "Building Docker image..."
	@docker build -t mermaid-autogen-agent .

# Target to run the application inside a Docker container (optional)

docker-run:  # Correcting indentation to use tabs instead of spaces
	@echo "Running application in Docker container..."
	@docker run -p 8000:8000 mermaid-autogen-agent

# Help target to display available commands

help:  # Correcting indentation to use tabs instead of spaces
	@echo "Available commands:"
	@grep -E '^[^ ]+:.*?#?\{2\}' Makefile | sort

.PHONY: install clean build test run test-coverage lint docker-build docker-run
