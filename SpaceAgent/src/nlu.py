import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Replace with your chosen pre-trained model and labels
MODEL_NAME = "distilbert-base-uncased-finetuned-sst-2-english"
LABELS = ["flowchart", "uml_class_diagram"]  # Example labels for diagram types


def get_user_input():
    """
    Prompts the user for a written description of the desired diagram.

    Now accepts multi-line input. The user must type 'END' on a new line to finish input.

    Returns:
        str: The user-provided description.
    """

    print("Please enter a written description of the diagram you want to generate (e.g., flowchart, UML class diagram):")
    print("(Type 'END' on a new line when you are finished)")
    lines = []
    while True:
        line = input()
        if line == "END":
            break
        lines.append(line)
    description = "\n".join(lines)
    return description


def predict_diagram_type(description, model_name=MODEL_NAME, labels=LABELS):
    """
    Uses a pre-trained model to predict the type of diagram based on the description.

    Args:
        description: The user-provided description.
        model_name: Name of the pre-trained model (defaults to distilbert-base-uncased-finetuned-sst-2-english).
        labels: List of supported diagram types (defaults to flowchart and uml_class_diagram).

    Returns:
        str: The predicted diagram type (or None if prediction is uncertain).
    """
    import logging
    logging.basicConfig(level=logging.DEBUG)
    logging.debug("Entering predict_diagram_type function.")
    print(f"Predicting diagram type for description: {description[:60]}...")  # Show a snippet of the description for debugging
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(
        model_name, num_labels=len(labels)
    )
    logging.debug("Model and tokenizer loaded successfully.")
    print("Model and tokenizer loaded successfully.")
    encoded_input = tokenizer(description, return_tensors="pt", max_length=512, truncation=True)
    print(f"Input encoded. Length: {len(encoded_input['input_ids'][0])}")
    logging.debug(f"Input encoded. Length: {len(encoded_input['input_ids'][0])}")
    outputs = model(**encoded_input)
    predictions = torch.argmax(outputs.logits, dim=-1)
    predicted_label = labels[predictions.item()]
    logging.debug(f"Prediction completed. Label: {predicted_label}")
    print(f"Prediction completed. Label: {predicted_label}")
    print("Downloading or loading the tokenizer from:", model_name)
    print("Downloading or loading the model from:", model_name)
    print(f"Truncating input to max_length: {encoded_input['input_ids'].size()}")
    print(f"Predicted label index: {predictions.item()} - Predicted diagram type: {predicted_label}")
    return predicted_label


def generate_basic_mermaid_code(predicted_type):
    """
    Generates basic Mermaid code based on the predicted diagram type.

    Args:
        predicted_type: The predicted diagram type (e.g., flowchart, uml_class_diagram).

    Returns:
        str: The basic Mermaid code for the predicted diagram type (or None if type is unknown).
    """

    if predicted_type == "flowchart":
        mermaid_code = "graph LR\nA[Start] --> B(Process 1) --> C(Process 2) --> D(End)"
    elif predicted_type == "uml_class_diagram":
        mermaid_code = "classDiagram\nclass Customer {\n + name: String\n + email: String\n}\nclass Order {\n + id: int\n + customer: Customer\n + items: list\n}\nCustomer <|-- Order"
    else:
        mermaid_code = None
    return mermaid_code


if __name__ == "__main__":
    user_description = get_user_input()
    predicted_type = predict_diagram_type(user_description)
    if predicted_type:
        print(f"Predicted diagram type: {predicted_type}")
        mermaid_code = generate_basic_mermaid_code(predicted_type)
        if mermaid_code:
            print(f"\nBasic Mermaid code for {predicted_type}:\n{mermaid_code}")
        else:
            print("Generating Mermaid code for this type is not yet implemented.")
    else:
        print("Couldn't determine the diagram type based on your description.")
    print("Downloading or loading the tokenizer from:", model_name)
    print("Downloading or loading the model from:", model_name)
    print(f"Truncating input to max_length: {encoded_input['input_ids'].size()}")
    print(f"Predicted label index: {predictions.item()} - Predicted diagram type: {predicted_label}")
