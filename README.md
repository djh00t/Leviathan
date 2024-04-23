# Project Leviathan: Automated Diagram Generation

This project aims to develop a system that automatically generates diagrams based on user-provided descriptions.

## Project Goals

* Support for Multiple Diagrams: The system will initially focus on flowcharts and pie charts, with the potential to expand to other types in the future.
* Natural Language Processing (NLP) Integration: We will leverage spaCy to parse user descriptions and identify key components for diagram creation.
* Mermaid Visualization: Diagrams will be generated using Mermaid's visual language.

## Code Structure

* **nlp_parser.py:** This module will house the NLP processing logic. It will use spaCy to extract relevant information from user descriptions and translate them into a structured format suitable for visualization.
* **mermaid_visualizer.py:**  This module will take the output from the NLP parser and convert it into the corresponding Mermaid code for different diagram types.
* **main.py:** This main script will serve as the entry point. It will handle user interaction, determine the diagram type, call the NLP parser and visualizer functions, and finally render or display the generated diagram.

## Corpus

We will maintain a dedicated corpus of user requests and corresponding example diagrams. This corpus serves several purposes:

* **Training Data Source:** The NLP parser will be trained on this corpus to learn how to identify key elements from user descriptions.
* **Reference Guide:** The corpus will act as a reference point during development to ensure the system can handle various phrasing styles and diagram types.

## Documentation

The project will be well-documented with comments within the codebase and a central markdown file (likely named README.md) that will cover:

* Project Goals
* Supported Diagram Types
* High-Level Architecture Overview
* Instructions on running the project (to be added as development progresses)

## Getting Started

This project utilizes Python libraries like spaCy and Mermaid.

* **Prerequisites:** Ensure you have these libraries installed:
    ```bash
    pip install spacy mermaid
    ```

* **Data Preparation:**  Populate the corpus with user requests and corresponding example diagrams in formats like Mermaid code or image files.
* **Code Walkthrough:** Refer to the code within each module (`nlp_parser.py`, `mermaid_visualizer.py`, and `main.py`) for detailed comments on the functionalities.

## Future Enhancements

* Integration with a web framework to create a user-friendly interface.
* Support for additional diagram types (e.g., bar charts, sequence diagrams).
* Refinement of the NLP parsing to handle more complex user descriptions.
