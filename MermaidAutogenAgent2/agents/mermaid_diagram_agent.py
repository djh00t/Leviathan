from autogen import Agent

class MermaidDiagramAgent(Agent):
  def __init__(self):
    super().__init__()

  def process(self, text_description, data=None):
    """
    Processes the text description to generate information for a process diagram.

    Args:
        text_description: Textual description of the diagram.
        data: Optional additional data for diagram generation (ignored here).

    Returns:
        A dictionary containing information for Mermaid diagram generation:
            - entities: List of steps and components involved in the process.
            - relationships: List of relationships between entities (showing flow).
    """

    # Extract entities from the text description (assuming basic parsing)
    entities = text_description.split(", ")

    # Define relationships representing the process flow
    relationships = [
      ("Application Startup", entities[0]),
      (entities[0], entities[1]),
      (entities[1], entities[2]),
      (entities[2], "Application Response"),
    ]

    return {
      "entities": entities,
      "relationships": relationships,
    }
