# MermaidAutogenAgent

This project, MermaidAutogenAgent, is designed to generate and manage Mermaid
diagrams using a pyautogen agent. It integrates with FastAPI for the API layer,
utilizes a FAISS database for storing feedback and experiences, and employs AWS
S3 for storage of diagrams and data synchronization.

The plugin takes in a description of a diagram and automatically generates the
diagram using the mermaid-py library. It also incorporates user feedback into
the generation process, learning from past experiences to improve the quality
of the generated diagrams. 

## Features

- **Diagram Generation**: Automatically generate diagrams from descriptions using the mermaid-py library.
- **Learning from Feedback**: Incorporates user feedback into the generation process using a FAISS vector database.
- **S3 Integration**: Stores diagrams and synchronizes the data directory with AWS S3.
- **Cron Job Automation**: Automates S3 synchronization through configurable cron jobs.

## Getting Started

### Prerequisites

- Python 3.8+
- Docker (optional for containerization)
- AWS account (for S3 storage)

### Installation

1. Clone the repository:
git clone https://github.com/djh00t/Leviathan.git
cd MermaidAutogenAgent

2. Install dependencies:
make setup

3. Configure your environment variables:
cp .env.example .env

Edit .env to fit your environment setup

### Usage

- Start the application:
make run

- Access the application at `http://localhost:8000`.

- Use the `/docs` endpoint to view the API documentation and interact with the API.

## Deployment

- **Local Deployment**:
- Use the `make run` command to run the application locally.

- **Production Deployment**:
- Detailed instructions on deploying to a production environment, including considerations for load balancing and security.

## Project Structure

This section outlines the directory and file structure for the project, detailing the purpose of each component.

MermaidAutogenAgent/
├── app/ # Main application directory
│ ├── init.py # Makes app a Python package
│ ├── main.py # Entry point for the FastAPI app
│ └── dependencies.py # Dependency management for FastAPI
│
├── tests/ # Test directory
│ ├── init.py # Makes tests a Python package
│ ├── test_config.py # Tests for configuration settings
│ └── test_generation.py # Tests for the diagram generation functionalities
│
├── docs/ # Documentation files (future use)
│ └── index.md # Starting point for the documentation
│
├── diagrams/ # Directory for storing generated diagrams (if not using a DB)
│
├── data/ # Data directory for any additional project data
│ └── training_data/ # Example data that could be used for machine learning models
│
├── .env # Environment variables (not tracked by Git)
├── .gitignore # Specifies intentionally untracked files to ignore
├── README.md # Project overview and setup instructions
├── requirements.txt # The list of requirements for the project
├── setup.py # Setup script for the project's package distribution
└── Makefile # Contains commands to facilitate common setup and development tasks

### Explanation of Directory Structure:

- **`/app`**: Contains all the source code for the FastAPI application, including initializers and route definitions.
- **`/tests`**: Includes all pytest test cases for the project. This is where you would add tests for new functionalities.
- **`/docs`**: Intended for project documentation. Currently empty but can be set up to use tools like Sphinx.
- **`/diagrams`**: Optional directory for storing generated diagrams locally, useful for debugging and quick checks.
- **`/data`**: For storing any relevant project data, which might include datasets for training or examples.
- **Root Files**:
  - **`.env`**: For local environment variables needed for development.
  - **`.gitignore`**: Lists files and directories that should be ignored by version control.
  - **`README.md`**: Provides an overview of the project, setup instructions, and other essential information.
  - **`requirements.txt`**: Lists all Python libraries the project depends on.
  - **`setup.py`**: Used for packaging the project, making it easier to distribute and install.
  - **`Makefile`**: Simplifies common administrative tasks like setting up the environment, testing, and cleaning up artifacts.

This enhanced `README.md` includes a comprehensive guide to the project's layout, making it easier for others to navigate and understand the project's structure and contributing as needed.

## Contributing

Contributions are welcome! Please read the CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.