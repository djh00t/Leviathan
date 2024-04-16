# This file will contain unit tests for core functionalities (empty for now)
import pytest
from core import generate_diagram

# Example unit test (replace with your specific tests)
def test_generate_diagram_simple():
  diagram = generate_diagram("This is a flowchart")
  assert "graph LR" in diagram  # Assert expected content in the diagram

# Add more unit tests for different functionalities in core.py
