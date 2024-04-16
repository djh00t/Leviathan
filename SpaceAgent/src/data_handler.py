import os

def load_data(data_dir):
  """
  Loads data from a directory containing text descriptions and corresponding Mermaid code files.

  Args:
      data_dir: Path to the directory containing data files.

  Returns:
      dict: A dictionary mapping diagram types (e.g., "flowchart", "uml_class_diagram") to lists of descriptions and corresponding Mermaid code.
  """
  
  data = {}
  for filename in os.listdir(data_dir):
    if filename.endswith(".txt"):  # Assuming descriptions have .txt extension
      diagram_type = filename.split(".")[0]
      data[diagram_type] = []  # Initialize list for descriptions and corresponding code
      with open(os.path.join(data_dir, filename), "r") as file:
        description = file.read().strip()
      data[diagram_type].append(description)
    elif filename.endswith(".mmd"):  # Assuming Mermaid code has .mmd extension
      diagram_type = filename.split(".")[0]
      if diagram_type in data:  # Ensure description exists for this type
        with open(os.path.join(data_dir, filename), "r") as file:
          mermaid_code = file.read().strip()
          data[diagram_type].append(mermaid_code)
      else:
        print(f"Warning: Found Mermaid code for {diagram_type} without a corresponding description file.")
  return data

def save_data(data, data_dir):
  """
  Saves data to a directory with separate files for descriptions and corresponding Mermaid code for each diagram type.

  Args:
      data: A dictionary mapping diagram types to lists of descriptions and corresponding Mermaid code.
      data_dir: Path to the directory for saving the data.
  """
  
  os.makedirs(data_dir, exist_ok=True)  # Create directory if it doesn't exist
  for diagram_type, descriptions_and_code in data.items():
    if len(descriptions_and_code) != 2:
      print(f"Warning: Inconsistent data for {diagram_type}. Expected description and code pair, found {len(descriptions_and_code)} entries.")
      continue
    description, mermaid_code = descriptions_and_code
    with open(os.path.join(data_dir, f"{diagram_type}.txt"), "w") as file:
      file.write(description)
    with open(os.path.join(data_dir, f"{diagram_type}.mmd"), "w") as file:
      file.write(mermaid_code)

if __name__ == "__main__":
  
