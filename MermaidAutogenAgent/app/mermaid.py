# import necessary modules from mermaid-py
from mermaid.graph import Graph
import mermaid as md

def create_flowchart(description: str):
    """
    Creates a flowchart based on a given textual description.

    Args:
    description (str): Mermaid syntax description of the flowchart.

    Returns:
    An instance of a Mermaid object containing the flowchart.
    """
    # Create a Graph object
    graph = Graph('example-flowchart', description)

    # Convert the Graph to a Mermaid diagram object
    mermaid_diagram = md.Mermaid(graph)

    # For notebook use, just return the diagram object
    # For web output, convert to the desired format and return the file or URL
    return mermaid_diagram

# Example usage
flowchart_description = """
flowchart TD
    A[Start] --> B[Do Something]
    B --> C{Decision?}
    C -->|Yes| D[Do Another Thing]
    C -->|No| E[Stop]
"""
diagram = create_flowchart(flowchart_description)
print(diagram)