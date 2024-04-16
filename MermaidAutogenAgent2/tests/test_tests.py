import subprocess

def run_unit_tests():
  """
  Runs all unit tests using pytest and returns True on success, False on failure.
  """
  result = subprocess.run(
      ["pytest", "tests/"], capture_output=True, text=True, check=True
  )
  # Print test results for debugging purposes (optional)
  print(result.stdout)
  return True

# Example usage (can be called from main.py)
# if not run_unit_tests():
#     print("Unit tests failed!")
