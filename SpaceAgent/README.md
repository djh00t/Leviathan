# Building an AI for Generating Diagrams from Descriptions

This project aims to create a Python AI tool that can generate Mermaid code based on spoken or written descriptions of processes, diagrams, or projects.

## Core Functionality

- User Input: Accepts spoken English descriptions (optional) or written text descriptions.
- Natural Language Understanding (NLU):
    - Identifies the type of diagram the user wants (e.g., flowchart, UML class diagram).
    - Extracts crucial details from the description like steps in a process or system components.
- Mermaid Code Generation: Builds Mermaid code using the extracted information.
- User Interaction (Optional):
    - Asks clarifying questions if the information seems insufficient.
    - Presents the generated Mermaid code for user feedback.
    - Refines the model based on user feedback (future implementation).

## Tools and Technologies

- **Python:** Programming Language
- **Hugging Face Transformers:** Pre-trained models for NLU tasks (e.g., DistilBERT, T5)
- **SpeechRecognition (Optional):** Converts spoken English to text.
- **Mermaid library:** Interacts with the Mermaid diagramming language.
- **Prompt Toolkit (Optional):** Handles user interaction and prompts for clarification.

## Getting Started
1. **Install Requirements:** Refer to requirements.txt for the list of dependencies and install them using pip install -r requirements.txt.
2. **Data Preparation:** Create a dataset of spoken English descriptions paired with corresponding Mermaid code in the data/ folder. Organize the data into subfolders for training and testing sets.
3. **Run the Script:** Execute the setup.sh script to create the initial project structure.

## Project Structure

```
diagrams_from_description/
├── data/
│   ├── training/
│   │   ├── spoken_descriptions/
│   │   │   ├── flowchart.txt
│   │   │   └── ... (other diagram types)
│   │   └── mermaid_code/
│   │       ├── flowchart.mmd
│   │       └── ... (other diagram types)
│   └── test/
│       ├── spoken_descriptions/
│       │   ├── flowchart.txt
│       │   └── ... (other diagram types)
│       └── mermaid_code/
│           ├── flowchart.mmd
│           └── ... (other diagram types)
├── requirements.txt
├── src/
│   ├── __init__.py  # Optional empty file to mark it as a package
│   ├── ai.py
│   ├── data_handler.py
│   ├── dialog_manager.py  # Optional for speech recognition and clarification prompts
│   ├── mermaid_generator.py
│   └── nlu.py
├── tests/
│   └── test_*.py  # Unit tests for your code
└── README.md
└── setup.sh  # Script to create initial project structure
```

## Next Steps
- Implement core functionalities like user input handling, NLU, and Mermaid code generation.
- (Optional) Integrate speech recognition and user interaction for clarification.
- Train your model using the prepared dataset.
- Continuously improve the model's accuracy through user feedback and data augmentation.

## Contributing
This project welcomes contributions! Feel free to fork the repository and submit pull requests with improvements or additional features.

## License
This project is licensed under the MIT License.