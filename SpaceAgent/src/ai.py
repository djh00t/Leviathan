from nlu import get_user_input, predict_diagram_type
import mermaid_generator
import logging

logging.basicConfig(level=logging.DEBUG)
def generate_diagram(description):
  """
  Coordinates functionalities to generate Mermaid code based on user description.

  Args:
      description: The user-provided description of the desired diagram.
  logging.debug("generate_diagram called with description: {}".format(description))

  Returns:
      str: The generated Mermaid code, or None if there's an error.
  """
  
  predicted_type = predict_diagram_type(description)
  if predicted_type:
    logging.debug("Predicted diagram type: {}".format(predicted_type))
    mermaid_code = mermaid_generator.generate_mermaid_code(predicted_type, description)
    return mermaid_code
  else:
    print("Couldn't determine the diagram type based on your description.")
    return None

def main():
  """
  logging.debug("main function started")
  Main entry point for the application.
  """


  
  user_description = get_user_input()  # You can move this function from nlu.py if needed
  logging.debug("User description received: {}".format(user_description))
  mermaid_code = generate_diagram(user_description)
  if mermaid_code:
    print(f"\nGenerated Mermaid code:\n{mermaid_code}")
  logging.debug("main function completed")

if __name__ == "__main__":
  main()
