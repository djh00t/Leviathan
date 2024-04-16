from fastapi import FastAPI, Body, Depends, HTTPException, status
from core.core import generate_diagram
from learning_system.feedback import update_feedback
from tests.test_tests import run_unit_tests

app = FastAPI()

class UserInput:
  def __init__(self, text_description: str):
    self.text_description = text_description

# Function to handle diagram generation requests
@app.post("/generate-diagram")
async def generate_diagram_api(input_data: UserInput = Body(...)):
    """
    API endpoint to generate a Mermaid diagram based on user input.
    """
    diagram = generate_diagram(input_data.text_description, input_data.data)
    return {"diagram": diagram}

# Function to handle user feedback submission (placeholder for now)
@app.post("/submit-feedback")
async def submit_feedback_api(feedback: Feedback = Body(...)):
    """
    API endpoint to receive user feedback on a generated diagram.
    """
    print(f"Received feedback: {feedback.comment}")  # Placeholder for processing
    return {"message": "Feedback submitted successfully"}

# Function to run all unit and end-to-end tests
async def run_all_tests():
    """
    Runs all unit and end-to-end tests for the application.
    """
    unit_test_results = run_unit_tests()
    end_to_end_results = run_end_to_end_tests()

    # Check for test failures
    if any(not result for result in [unit_test_results, end_to_end_results]):
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Tests failed. See logs for details.",
        )

# Health check endpoint
@app.get("/health")
async def health_check(run_tests: bool = Depends(run_all_tests)):
    """
    Health check endpoint to verify application health.
    """
    return {"status": "healthy"}

# Dependency to conditionally run tests before API calls
async def check_health(run_tests: bool = False):
    """
    Dependency function to conditionally run tests before API calls.
    """
    if run_tests:
        await run_all_tests()
    return None

# Decorate API endpoints with check_health dependency for optional testing
app.post("/generate-diagram").__func__ = Depends(check_health)(
    app.post("/generate-diagram")
)
app.post("/submit-feedback").__func__ = Depends(check_health)(
    app.post("/submit-feedback")
)
