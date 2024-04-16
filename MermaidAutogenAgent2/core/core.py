from agents.mermaid_diagram_agent import MermaidDiagramAgent
from mermaid import Mermaid

def generate_diagram(text_description, data=None):
  """
  Generates Mermaid diagram code based on user input using autogen.

  Args:
      text_description: Textual description of the diagram.
      data: Optional additional data for diagram generation (ignored here).

  Returns:
      The generated Mermaid diagram code as a string.
  """

  # Use the agent to process the text description
  agent = MermaidDiagramAgent()
  processed_data = agent.process(text_description, data)

  # Generate Mermaid code using the processed data
  mermaid = Mermaid()
  mermaid_code = "graph LR\n"
  # ... (add nodes, edges, styles based on processed_data)

  entities = processed_data["entities"]
  relationships = processed_data["relationships"]

  # Add nodes (assuming entities represent process steps/components)
  for entity in entities:
    mermaid_code += f'    {entity}[{entity}]\n'  # Node with label (entity name)

  # Add edges representing process flow
  for source, target, relation in relationships:
    style = ""  # Optional: Add styles based on relationship type (if applicable)
    mermaid_code += f'    {source} -->|{relation}| {target}\n'

  return mermaid_code
